"""
ui.py

Owns user-interface components.

Responsibilities:

- Main Window Creation
- Settings Window Creation
- Label Creation
- Button Creation
"""

import tkinter as tk
import os


def create_main_window(
    open_settings_window
):

    root_window = tk.Tk()
    
    current_directory = os.path.dirname(
        os.path.abspath(__file__)
    )

    icon_path = os.path.join(
        current_directory,
        "..",
        "assets",
        "icons",
        "icon_utensil-clock_white_BG.ico"
    )

    root_window.title(
        "Lunch Countdown v3.1"
    )

    root_window.geometry(
        "500x325"
    )
    
    # Try to grab the icon, but during build this breaks
    try:

        root_window.iconbitmap(
            icon_path
        )

    except Exception:

        pass

    # Create labels

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
        font=("Arial", 18)
    )

    countdown_value_label.pack(
        pady=5
    )

    status_message_label = tk.Label(
        root_window,
        font=("Arial", 10)
    )

    status_message_label.pack(
        pady=10
    )

    settings_button = tk.Button(
        root_window,
        text="Settings",
        command=open_settings_window
    )

    settings_button.pack(
        pady=15
    )

    ui_components = {

        "root_window":
            root_window,

        "current_time_label":
            current_time_label,

        "lunch_time_label":
            lunch_time_label,

        "countdown_header_label":
            countdown_header_label,

        "countdown_value_label":
            countdown_value_label,

        "status_message_label":
            status_message_label,

        "settings_button":
            settings_button
    }

    return ui_components


def create_settings_window(
    root_window
):

    settings_window = tk.Toplevel(
        root_window
    )

    settings_window.title(
        "Settings"
    )

    settings_window.geometry(
        "550x650"
    )

    return settings_window
