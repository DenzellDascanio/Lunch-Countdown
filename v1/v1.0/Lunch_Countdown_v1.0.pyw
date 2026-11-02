import tkinter as tk
from datetime import datetime

# Lunch time configuration
lunch_hour = 12
lunch_minute = 0
lunch_second = 0


def update_lunch_countdown():
    """
    Updates all information displayed in the window.
    This function runs once every second.
    """

    # Variable for the current date and time
    current_datetime = datetime.now()

    # Take current time info and convert it to match the lunch settings
    lunch_datetime = current_datetime.replace(
        hour=lunch_hour,
        minute=lunch_minute,
        second=lunch_second,
        microsecond=0
    )

    # Calculate the difference in time from now until lunch time
    time_until_lunch = lunch_datetime - current_datetime

    # Convert the time difference object into a total number of seconds
    remaining_seconds = int(time_until_lunch.total_seconds())

    # Change the format
    current_time_string = current_datetime.strftime("%I:%M:%S %p")
    lunch_time_string = lunch_datetime.strftime("%I:%M:%S %p")

    if remaining_seconds > 0:

        # Convert from secs to hrs by dividing the secs by 3600 --> integer division result is the hours
        hours_until_lunch = remaining_seconds // 3600

        # Convert from secs to mins by finding the remainder of secs in the within the hour, then convert from secs to mins by dividing my 60
        minutes_until_lunch = (
            remaining_seconds % 3600
        ) // 60

        # Convert from total remaining seconds to a bounded-range seconds [0, 59] by finding the remainder value of seconds (reset every 60 secs)
        seconds_until_lunch = (
            remaining_seconds % 60
        )

        # Display the times until lunch
        display_time_text = (
            f"Current Time: {current_time_string}\n\n"
            f"Lunch Time: {lunch_time_string}\n\n"
            f"Time Until Lunch:\n"
            f"{hours_until_lunch:02}:"
            f"{minutes_until_lunch:02}:"
            f"{seconds_until_lunch:02}"
        )

    else:

        # Display the times at lunchtime
        display_time_text = (
            f"Current Time: {current_time_string}\n\n"
            f"Lunch Time: {lunch_time_string}\n\n"
            f"Lunch Time Has Arrived!"
        )

    countdown_label.config(text=display_time_text)

    # Update/Refresh the window every 1000 ms (1 sec) --> live clock, re-call the countown function
    root_window.after(1000, update_lunch_countdown)


# Create the main window
root_window = tk.Tk()

# Create a title
root_window.title("Lunch Countdown")

# Create size of window (w-pixels wide by h-pixels tall, "w x h")
root_window.geometry("350x220")

# Create label that displays information
countdown_label = tk.Label(
    root_window,
    font=("Arial", 14),
    justify="center"
)

countdown_label.pack(expand=True)

# Start updates
update_lunch_countdown()

# Keep window running
root_window.mainloop()
