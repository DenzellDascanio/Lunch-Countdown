# Lunch Countdown

Version: 2.1

## Overview

Lunch Countdown is a desktop application built with Python and Tkinter that displays:

- Current Time
- Lunch Time
- Time Remaining Until Lunch

The application automatically updates every second and continues counting toward the next lunch period after the current day's lunch has passed.

Version 2.1 introduces the application's first user customization framework, including color customization, live preview functionality, save/cancel workflows, and audio feedback.

---

## Features

### Time Display

Displays the computer's current local system time.

### Lunch Time Display

Displays the configured lunch time.

### Continuous Countdown

The application continuously calculates the time remaining until lunch.

When the configured lunch time has already passed for the current day, the application automatically counts down to the next day's lunch period.

### Automatic Refresh

The display updates once every second.

---

## User Interface

### Main Window

Displays:

- Current Time
- Lunch Time
- Time Until Lunch
- Countdown Value
- Application Status Message

### Settings Window

Provides access to application customization features.

Current sections include:

- Lunch Settings
- Color Settings
- Audio Settings
- Toggle Settings
- Loadout Management (Future Version)

---

## Color Customization

### Current Time Color

Allows the user to change the display color of the Current Time label.

### Lunch Time Color

Allows the user to change the display color of the Lunch Time label.

### Countdown Color

Allows the user to change the display color of the countdown timer.

### Status Message Color

Allows the user to change the display color of the status message.

### Windows Color Picker

Uses the Windows color picker dialog to provide a large range of selectable colors.

---

## Live Preview System

Changes may be previewed before being saved.

When Live Preview is enabled:

- Color selections are immediately shown within the application window.
- Changes remain temporary until saved.

This allows experimentation without permanently changing the current configuration.

---

## Audio Feedback

### Button Click Sounds

The application includes audible button feedback.

Current implementation uses a custom two-tone click effect:

- 1200 Hz for 15 milliseconds
- 1500 Hz for 10 milliseconds

### Audio Toggle

Button sounds may be enabled or disabled using the Toggle Settings section.

---

## Toggle Settings

Current toggle options include:

- Enable Button Click Sounds
- Enable Live Preview
- Always On Top

Additional toggle options will be added in future versions.

---

## Save and Cancel Workflow

### Save

Applies current settings to the application.

### Cancel

Discards any unsaved changes and restores the most recently saved settings.

---

## Technical Improvements

### Working Settings Architecture

Version 2.1 introduces a temporary settings container:

working_settings

This allows modifications to be tested before becoming permanent.

### Single Settings Window

Only one Settings window may exist at a time.

Attempting to reopen Settings while the window is already active will bring the existing Settings window to the front rather than creating duplicates.

### Modular Settings Structure

Settings are organized into logical categories:

- Lunch
- Audio
- Toggles
- Colors

This architecture simplifies future feature development.

---

## Planned Features

### Version 2.2

- Settings persistence
- JSON configuration files
- Loadout creation
- Loadout saving
- Loadout loading
- Loadout deletion

### Version 2.3

- Additional color customization
- Settings frame customization
- Theme presets
- Reset to Default colors

---

## Known Limitations

Current settings only exist during the application's execution.

Closing the application resets all settings to their default values.

Persistent settings and loadouts are planned for a future release.

---

## Technologies Used

- Python
- Tkinter
- Datetime
- Timedelta
- Winsound

---

## Release Notes

### Version 2.1

Added:

- Color Picker Integration
- Current Time Color Customization
- Lunch Time Color Customization
- Countdown Color Customization
- Status Message Color Customization
- Live Preview Support
- Save / Cancel Workflow
- Single Settings Window Enforcement
- Custom Two-Tone Audio Feedback

Improved:

- Settings Architecture
- Future Expandability
- User Customization Framework

Prepared For:

- JSON-Based Settings Storage
- Loadout Management

- Versions 2.2 and 2.3 cancelled --> Major update --> version 3.0
- Theme System
