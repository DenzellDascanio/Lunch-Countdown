import tkinter as tk
import winsound

from datetime import datetime, timedelta


# =====================================================
# Application Settings
# =====================================================

settings = {

    "lunch": {

        "hour": 12,
        "minute": 0,
        "second": 0

    },

    "audio": {

        "button_click_enabled": True

    },

    "toggles": {

        "live_preview_enabled": True,
        "always_on_top": False

    },

    "colors": {

        "current_time": "green",
        "lunch_time": "blue",
        "countdown": "black",
        "status_message": "red"

    }

}


# =====================================================
# Audio Functions
# =====================================================

def play_button_click():

    if settings["audio"]["button_click_enabled"]:

        winsound.MessageBeep()


# =====================================================
# Settings Functions
# =====================================================

def save_settings():

    settings["audio"]["button_click_enabled"] = (
        button_sound_enabled.get()
    )

    settings["toggles"]["live_preview_enabled"] = (
        live_preview_enabled.get()
    )

    settings["toggles"]["always_on_top"] = (
        always_on_top_enabled.get()
    )

    root_window.attributes(
        "-topmost",
        settings["toggles"]["always_on_top"]
    )

    play_button_click()


# =====================================================
# Settings Window
# =====================================================

def open_settings_window():

    play_button_click()

    settings_window = tk.Toplevel(root_window)

    settings_window.title("Settings")

    settings_window.geometry("500x500")

    settings_title_label = tk.Label(
        settings_window,
        text="Settings",
        font=("Arial", 14, "bold")
    )

    settings_title_label.pack(
        pady=10
    )

    # =================================================
    # Lunch Settings
    # =================================================

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
    ).pack(
        pady=10
    )

    # =================================================
    # Color Settings
    # =================================================

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
    ).pack(
        pady=10
    )

    # =================================================
    # Audio Settings
    # =================================================

    audio_settings_frame = tk.LabelFrame(
        settings_window,
        text="Audio Settings"
    )

    audio_settings_frame.pack(
        fill="x",
        padx=10,
        pady=5
    )

    tk.Label(
        audio_settings_frame,
        text="Windows system sounds currently in use."
    ).pack(
        pady=10
    )

    # =================================================
    # Toggle Settings
    # =================================================

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
    ).pack(
        anchor="w",
        padx=10,
        pady=2
    )

    tk.Checkbutton(
        toggle_settings_frame,
        text="Enable Live Preview",
        variable=live_preview_enabled
    ).pack(
        anchor="w",
        padx=10,
        pady=2
    )

    tk.Checkbutton(
        toggle_settings_frame,
        text="Always On Top",
        variable=always_on_top_enabled
    ).pack(
        anchor="w",
        padx=10,
        pady=2
    )

    # =================================================
    # Loadout Management
    # =================================================

    loadout_settings_frame = tk.LabelFrame(
        settings_window,
        text="Loadout Management"
    )

    loadout_settings_frame.pack(
        fill="x",
        padx=10,
        pady=5
    )

    tk.Label(
        loadout_settings_frame,
        text="Loadout system planned for future version."
    ).pack(
        pady=10
    )

    # =================================================
    # Save Button
    # =================================================

    save_button = tk.Button(
        settings_window,
        text="Save",
        command=save_settings
    )

    save_button.pack(
        pady=15
    )


# =====================================================
# Countdown Function
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

        lunch_datetime = (
            lunch_datetime +
            timedelta(days=1)
        )

    time_until_lunch = (
        lunch_datetime -
        current_datetime
    )

    total_remaining_seconds = int(
        time_until_lunch.total_seconds()
    )

    current_time_string = (
        current_datetime.strftime(
            "%I:%M:%S %p"
        )
    )

    lunch_time_string = (
        lunch_datetime.strftime(
            "%I:%M:%S %p"
        )
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

    root_window.after(
        1000,
        update_lunch_countdown
    )


# =====================================================
# Main Window
# =====================================================

root_window = tk.Tk()

root_window.title(
    "Lunch Countdown v2.0"
)

root_window.geometry(
    "400x300"
)


# =====================================================
# Toggle Variables
# =====================================================

button_sound_enabled = tk.BooleanVar(
    value=settings["audio"]["button_click_enabled"]
)

live_preview_enabled = tk.BooleanVar(
    value=settings["toggles"]["live_preview_enabled"]
)

always_on_top_enabled = tk.BooleanVar(
    value=settings["toggles"]["always_on_top"]
)


# =====================================================
# Display Labels
# =====================================================

current_time_label = tk.Label(
    root_window,
    font=("Arial", 12),
    fg=settings["colors"]["current_time"]
)

current_time_label.pack(
    pady=(15, 5)
)

lunch_time_label = tk.Label(
    root_window,
    font=("Arial", 12),
    fg=settings["colors"]["lunch_time"]
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
    font=("Arial", 20),
    fg=settings["colors"]["countdown"]
)

countdown_value_label.pack(
    pady=5
)

status_message_label = tk.Label(
    root_window,
    font=("Arial", 10),
    fg=settings["colors"]["status_message"]
)

status_message_label.pack(
    pady=5
)


# =====================================================
# Buttons
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
