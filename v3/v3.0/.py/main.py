import tkinter as tk
import copy

from tkinter.colorchooser import askcolor
from datetime import datetime, timedelta

from settings import (
    settings,
    DEFAULT_LOADOUT_NAME
)

from audio import play_button_click

from loadouts import (
    save_loadout,
    initialize_application
)


# =====================================================
# Working Variables
# =====================================================

working_settings = None

settings_window = None


# =====================================================
# Apply Saved Settings
# =====================================================

def apply_saved_settings():

    current_time_label.config(
        fg=settings["colors"]["current_time"]
    )

    lunch_time_label.config(
        fg=settings["colors"]["lunch_time"]
    )

    countdown_value_label.config(
        fg=settings["colors"]["countdown"]
    )

    status_message_label.config(
        fg=settings["colors"]["status_message"]
    )

    root_window.attributes(
        "-topmost",
        settings["toggles"]["always_on_top"]
    )

    button_sound_enabled.set(
        settings["audio"]["button_click_enabled"]
    )

    live_preview_enabled.set(
        settings["toggles"]["live_preview_enabled"]
    )

    always_on_top_enabled.set(
        settings["toggles"]["always_on_top"]
    )


# =====================================================
# Preview Functions
# =====================================================

def apply_preview_settings():

    current_time_label.config(
        fg=working_settings["colors"]["current_time"]
    )

    lunch_time_label.config(
        fg=working_settings["colors"]["lunch_time"]
    )

    countdown_value_label.config(
        fg=working_settings["colors"]["countdown"]
    )

    status_message_label.config(
        fg=working_settings["colors"]["status_message"]
    )


# =====================================================
# Color Picker Functions
# =====================================================

def choose_current_time_color():

    play_button_click()

    selected_color = askcolor()[1]

    if selected_color:

        working_settings["colors"]["current_time"] = (
            selected_color
        )

        if live_preview_enabled.get():

            apply_preview_settings()


def choose_lunch_time_color():

    play_button_click()

    selected_color = askcolor()[1]

    if selected_color:

        working_settings["colors"]["lunch_time"] = (
            selected_color
        )

        if live_preview_enabled.get():

            apply_preview_settings()


def choose_countdown_color():

    play_button_click()

    selected_color = askcolor()[1]

    if selected_color:

        working_settings["colors"]["countdown"] = (
            selected_color
        )

        if live_preview_enabled.get():

            apply_preview_settings()


def choose_status_message_color():

    play_button_click()

    selected_color = askcolor()[1]

    if selected_color:

        working_settings["colors"]["status_message"] = (
            selected_color
        )

        if live_preview_enabled.get():

            apply_preview_settings()


# =====================================================
# Settings Functions
# =====================================================

def save_settings():

    global settings_window

    # This is done because settings.py shares the same dictionary object --> avoids new dictionary object interference
    settings.clear()

    # Updates rather than creates a new dictionary in settings.py
    settings.update(
        copy.deepcopy(
            working_settings
        )
    )

    settings["audio"]["button_click_enabled"] = (
        button_sound_enabled.get()
    )

    settings["toggles"]["live_preview_enabled"] = (
        live_preview_enabled.get()
    )

    settings["toggles"]["always_on_top"] = (
        always_on_top_enabled.get()
    )

    save_loadout(
        DEFAULT_LOADOUT_NAME
    )

    apply_saved_settings()

    play_button_click()

    settings_window.destroy()

    settings_window = None


def cancel_settings():

    global working_settings
    global settings_window

    working_settings = copy.deepcopy(
        settings
    )

    apply_saved_settings()

    play_button_click()

    settings_window.destroy()

    settings_window = None


# =====================================================
# Settings Window
# =====================================================

def open_settings_window():

    global working_settings
    global settings_window

    if settings_window is not None:

        if settings_window.winfo_exists():

            settings_window.lift()

            return

    play_button_click()

    working_settings = copy.deepcopy(
        settings
    )

    settings_window = tk.Toplevel(
        root_window
    )

    settings_window.title(
        "Settings"
    )

    settings_window.geometry(
        "550x650"
    )

    tk.Label(
        settings_window,
        text="Settings",
        font=("Arial", 14, "bold")
    ).pack(
        pady=10
    )

    color_settings_frame = tk.LabelFrame(
        settings_window,
        text="Color Settings"
    )

    color_settings_frame.pack(
        fill="x",
        padx=10,
        pady=5
    )

    tk.Button(
        color_settings_frame,
        text="Current Time Color",
        command=choose_current_time_color
    ).pack(fill="x", padx=10, pady=2)

    tk.Button(
        color_settings_frame,
        text="Lunch Time Color",
        command=choose_lunch_time_color
    ).pack(fill="x", padx=10, pady=2)

    tk.Button(
        color_settings_frame,
        text="Countdown Color",
        command=choose_countdown_color
    ).pack(fill="x", padx=10, pady=2)

    tk.Button(
        color_settings_frame,
        text="Status Message Color",
        command=choose_status_message_color
    ).pack(fill="x", padx=10, pady=2)

    toggle_settings_frame = tk.LabelFrame(
        settings_window,
        text="Toggle Settings"
    )

    toggle_settings_frame.pack(
        fill="x",
        padx=10,
        pady=5
    )

    tk.Checkbutton(
        toggle_settings_frame,
        text="Enable Button Click Sounds",
        variable=button_sound_enabled
    ).pack(anchor="w", padx=10)

    tk.Checkbutton(
        toggle_settings_frame,
        text="Enable Live Preview",
        variable=live_preview_enabled
    ).pack(anchor="w", padx=10)

    tk.Checkbutton(
        toggle_settings_frame,
        text="Always On Top",
        variable=always_on_top_enabled
    ).pack(anchor="w", padx=10)

    button_frame = tk.Frame(
        settings_window
    )

    button_frame.pack(
        pady=15
    )

    tk.Button(
        button_frame,
        text="Save",
        width=15,
        command=save_settings
    ).pack(
        side="left",
        padx=10
    )

    tk.Button(
        button_frame,
        text="Cancel",
        width=15,
        command=cancel_settings
    ).pack(
        side="left",
        padx=10
    )


# =====================================================
# Countdown Logic
# =====================================================

def update_lunch_countdown():

    current_datetime = datetime.now()

    lunch_datetime = current_datetime.replace(
        hour=settings["lunch"]["hour"],
        minute=settings["lunch"]["minute"],
        second=settings["lunch"]["second"],
        microsecond=0
    )

    if current_datetime >= lunch_datetime:

        lunch_datetime += timedelta(
            days=1
        )

    time_until_lunch = (
        lunch_datetime -
        current_datetime
    )

    total_remaining_seconds = int(
        time_until_lunch.total_seconds()
    )

    current_time_label.config(
        text=f"Current Time: "
             f"{current_datetime.strftime('%I:%M:%S %p')}"
    )

    lunch_time_label.config(
        text=f"Lunch Time: "
             f"{lunch_datetime.strftime('%I:%M:%S %p')}"
    )

    hours = total_remaining_seconds // 3600

    minutes = (
        total_remaining_seconds % 3600
    ) // 60

    seconds = (
        total_remaining_seconds % 60
    )

    countdown_value_label.config(
        text=f"{hours:02}:{minutes:02}:{seconds:02}"
    )

    status_message_label.config(
        text="Counting Down To Lunch"
    )

    root_window.after(
        1000,
        update_lunch_countdown
    )


# =====================================================
# Main Window
# =====================================================

root_window = tk.Tk()

root_window.title(
    "Lunch Countdown v3.0"
)

root_window.geometry(
    "400x300"
)


button_sound_enabled = tk.BooleanVar()

live_preview_enabled = tk.BooleanVar()

always_on_top_enabled = tk.BooleanVar()


current_time_label = tk.Label(
    root_window,
    font=("Arial", 12)
)

current_time_label.pack(
    pady=(15, 5)
)

lunch_time_label = tk.Label(
    root_window,
    font=("Arial", 12)
)

lunch_time_label.pack(
    pady=5
)

countdown_header_label = tk.Label(
    root_window,
    text="Time Until Lunch",
    font=("Arial", 12, "bold")
)

countdown_header_label.pack(
    pady=(15, 5)
)

countdown_value_label = tk.Label(
    root_window,
    font=("Arial", 20)
)

countdown_value_label.pack(
    pady=5
)

status_message_label = tk.Label(
    root_window,
    font=("Arial", 10)
)

status_message_label.pack(
    pady=5
)

settings_button = tk.Button(
    root_window,
    text="Settings",
    command=open_settings_window
)

settings_button.pack(
    pady=15
)


# =====================================================
# Startup
# =====================================================

initialize_application()

apply_saved_settings()

update_lunch_countdown()

root_window.mainloop()
