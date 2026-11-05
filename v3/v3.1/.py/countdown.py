'''
countdown.py

Owns countdown-related functionality.
'''

from datetime import (
    datetime,
    timedelta
)

from settings import settings


def update_lunch_countdown(
    ui_components
):

    root_window = (
        ui_components["root_window"]
    )

    current_time_label = (
        ui_components["current_time_label"]
    )

    lunch_time_label = (
        ui_components["lunch_time_label"]
    )

    countdown_header_label = (
        ui_components["countdown_header_label"]
    )

    countdown_value_label = (
        ui_components["countdown_value_label"]
    )

    status_message_label = (
        ui_components["status_message_label"]
    )

    current_datetime = datetime.now()

    lunch_start_datetime = current_datetime.replace(
        hour=settings["lunch"]["hour"],
        minute=settings["lunch"]["minute"],
        second=settings["lunch"]["second"],
        microsecond=0
    )

    lunch_end_datetime = (
        lunch_start_datetime
        +
        timedelta(
            minutes=settings["lunch"]["duration_minutes"]
        )
    )

    if (
        current_datetime >= lunch_start_datetime
        and
        current_datetime < lunch_end_datetime
    ):

        current_time_label.config(
            text=
            f"Current Time: "
            f"{current_datetime.strftime('%I:%M:%S %p')}"
        )

        lunch_time_label.config(
            text=
            f"Lunch Time: "
            f"{lunch_start_datetime.strftime('%I:%M:%S %p')}"
        )

        countdown_header_label.config(
            text=""
        )

        countdown_value_label.config(
            text=""
        )

        status_message_label.config(
            text="It's Lunch Time",
            font=("Arial", 16, "bold")
        )

    else:

        if current_datetime >= lunch_start_datetime:

            lunch_start_datetime += timedelta(
                days=1
            )

        time_until_lunch = (
            lunch_start_datetime
            -
            current_datetime
        )

        total_remaining_seconds = int(
            time_until_lunch.total_seconds()
        )

        hours_until_lunch = (
            total_remaining_seconds // 3600
        )

        minutes_until_lunch = (
            total_remaining_seconds % 3600
        ) // 60

        seconds_until_lunch = (
            total_remaining_seconds % 60
        )

        current_time_label.config(
            text=
            f"Current Time: "
            f"{current_datetime.strftime('%I:%M:%S %p')}"
        )

        lunch_time_label.config(
            text=
            f"Lunch Time: "
            f"{lunch_start_datetime.strftime('%I:%M:%S %p')}"
        )

        countdown_header_label.config(
            text="Time Until Lunch"
        )

        countdown_value_label.config(
            text=
            f"{hours_until_lunch:02} hrs : "
            f"{minutes_until_lunch:02} mins : "
            f"{seconds_until_lunch:02} secs"
        )

        status_message_label.config(
            text="Counting Down To Lunch",
            font=("Arial", 10)
        )

    root_window.after(
        1000,
        lambda: update_lunch_countdown(
            ui_components
        )
    )