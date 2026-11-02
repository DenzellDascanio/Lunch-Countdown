import tkinter as tk
from datetime import datetime, timedelta


# =====================================================
# Application Settings
# =====================================================

settings = {

    "lunch_hour": 12,
    "lunch_minute": 0,
    "lunch_second": 0,

    "current_time_color": "green",
    "lunch_time_color": "blue",
    "countdown_color": "black",
    "status_message_color": "red"

}


# =====================================================
# Settings Window
# =====================================================

def open_settings_window():

    settings_window = tk.Toplevel(root_window)

    settings_window.title("Settings")

    settings_window.geometry("450x400")

    settings_title_label = tk.Label(
        settings_window,
        text="Settings",
        font=("Arial", 14, "bold")
    )

    settings_title_label.pack(pady=10)

    # ---------------------------------------------
    # Lunch Settings Section
    # ---------------------------------------------

    lunch_settings_frame = tk.LabelFrame(
        settings_window,
        text="Lunch Settings"
    )

    lunch_settings_frame.pack(
        fill="x",
        padx=10,
        pady=5
    )

    tk.Label(
        lunch_settings_frame,
        text="Future lunch settings will go here."
    ).pack(pady=10)

    # ---------------------------------------------
    # Color Settings Section
    # ---------------------------------------------

    color_settings_frame = tk.LabelFrame(
        settings_window,
        text="Color Settings"
    )

    color_settings_frame.pack(
        fill="x",
        padx=10,
        pady=5
    )

    tk.Label(
        color_settings_frame,
        text="Future color customization options will go here."
    ).pack(pady=10)

    # ---------------------------------------------
    # Future Features Section
    # ---------------------------------------------

    future_features_frame = tk.LabelFrame(
        settings_window,
        text="Future Features"
    )

    future_features_frame.pack(
        fill="x",
        padx=10,
        pady=5
    )

    tk.Label(
        future_features_frame,
        text="Reserved for future settings."
    ).pack(pady=10)


# =====================================================
# Countdown Logic
# =====================================================

def update_lunch_countdown():

    # Current date/time from the local computer
    current_datetime = datetime.now()

    # Create today's lunch datetime
    lunch_datetime = current_datetime.replace(
        hour=settings["lunch_hour"],
        minute=settings["lunch_minute"],
        second=settings["lunch_second"],
        microsecond=0
    )

    # If lunch already occurred today
    # move lunch to tomorrow
    if current_datetime >= lunch_datetime:

        lunch_datetime = lunch_datetime + timedelta(days=1)

    # Calculate time difference
    time_until_lunch = lunch_datetime - current_datetime

    # Convert time difference into seconds
    total_remaining_seconds = int(
        time_until_lunch.total_seconds()
    )

    # Convert date/time values to display format
    current_time_string = current_datetime.strftime(
        "%I:%M:%S %p"
    )

    lunch_time_string = lunch_datetime.strftime(
        "%I:%M:%S %p"
    )

    # Convert seconds into H:M:S
    hours_until_lunch = (
        total_remaining_seconds // 3600
    )

    minutes_until_lunch = (
        total_remaining_seconds % 3600
    ) // 60

    seconds_until_lunch = (
        total_remaining_seconds % 60
    )

    # Update Labels

    current_time_label.config(
        text=f"Current Time: {current_time_string}"
    )

    lunch_time_label.config(
        text=f"Lunch Time: {lunch_time_string}"
    )

    countdown_value_label.config(
        text=(
            f"{hours_until_lunch:02}:"
            f"{minutes_until_lunch:02}:"
            f"{seconds_until_lunch:02}"
        )
    )

    status_message_label.config(
        text="Counting Down To Lunch"
    )

    # Refresh every second
    root_window.after(
        1000,
        update_lunch_countdown
    )


# =====================================================
# Main Window
# =====================================================

root_window = tk.Tk()

root_window.title(
    "Lunch Countdown v1.1"
)

root_window.geometry(
    "400x300"
)


# =====================================================
# Current Time Label
# =====================================================

current_time_label = tk.Label(
    root_window,
    font=("Arial", 12),
    fg=settings["current_time_color"]
)

current_time_label.pack(
    pady=(15, 5)
)


# =====================================================
# Lunch Time Label
# =====================================================

lunch_time_label = tk.Label(
    root_window,
    font=("Arial", 12),
    fg=settings["lunch_time_color"]
)

lunch_time_label.pack(
    pady=5
)


# =====================================================
# Countdown Header
# =====================================================

countdown_header_label = tk.Label(
    root_window,
    text="Time Until Lunch",
    font=("Arial", 12, "bold")
)

countdown_header_label.pack(
    pady=(15, 5)
)


# =====================================================
# Countdown Value
# =====================================================

countdown_value_label = tk.Label(
    root_window,
    font=("Arial", 20),
    fg=settings["countdown_color"]
)

countdown_value_label.pack(
    pady=5
)


# =====================================================
# Status Message
# =====================================================

status_message_label = tk.Label(
    root_window,
    font=("Arial", 10),
    fg=settings["status_message_color"]
)

status_message_label.pack(
    pady=5
)


# =====================================================
# Settings Button
# =====================================================

settings_button = tk.Button(
    root_window,
    text="Settings",
    command=open_settings_window
)

settings_button.pack(
    pady=15
)


# =====================================================
# Start Application
# =====================================================

update_lunch_countdown()

root_window.mainloop()
