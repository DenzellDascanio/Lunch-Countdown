import tkinter as tk
import copy

from tkinter.colorchooser import askcolor

from settings import (
    settings,
    DEFAULT_LOADOUT_NAME
)

from audio import play_button_click

from loadouts import (
    save_loadout,
    initialize_application
)

from countdown import (
    update_lunch_countdown
)

from ui import (
    create_main_window,
    create_settings_window
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

    settings.clear()

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

    settings_window = create_settings_window(
        root_window
    )

    tk.Label(
        settings_window,
        text="Settings",
        font=("Arial", 14, "bold")
    ).pack(
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

    tk.Button(
        color_settings_frame,
        text="Current Time Color",
        command=choose_current_time_color
    ).pack(
        fill="x",
        padx=10,
        pady=2
    )

    tk.Button(
        color_settings_frame,
        text="Lunch Time Color",
        command=choose_lunch_time_color
    ).pack(
        fill="x",
        padx=10,
        pady=2
    )

    tk.Button(
        color_settings_frame,
        text="Countdown Color",
        command=choose_countdown_color
    ).pack(
        fill="x",
        padx=10,
        pady=2
    )

    tk.Button(
        color_settings_frame,
        text="Status Message Color",
        command=choose_status_message_color
    ).pack(
        fill="x",
        padx=10,
        pady=2
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
        text="Custom two-tone click sound enabled."
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
        text="Default loadout persistence is enabled."
    ).pack(
        pady=10
    )

    # =================================================
    # Save / Cancel Buttons
    # =================================================

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
# Main Window Creation
# =====================================================

ui_components = create_main_window(
    open_settings_window
)

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


# =====================================================
# Toggle Variables
# =====================================================

button_sound_enabled = tk.BooleanVar()

live_preview_enabled = tk.BooleanVar()

always_on_top_enabled = tk.BooleanVar()


# =====================================================
# Startup
# =====================================================

initialize_application()

apply_saved_settings()

update_lunch_countdown(
    ui_components
)

root_window.mainloop()