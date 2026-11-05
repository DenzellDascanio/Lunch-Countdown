# Lunch Countdown Changelog

All notable changes to this project are documented here.

---

# Version 3.1

Release Date: 2026-11-05

## Added

### Countdown Architecture

- Moved countdown ownership into `countdown.py`
- Introduced separation between countdown behavior and application startup
- Reduced responsibilities of `main.py`

### UI Architecture

- Introduced `ui.py`
- Moved main window creation into dedicated UI module
- Introduced centralized `ui_components` collection
- Established ownership boundaries between UI creation and application logic

### Lunch State System

Added dedicated lunch-state behavior:

- Pre-Lunch State
- Lunch State
- Post-Lunch State

### Lunch Mode

During the active lunch period:

- Countdown Header is hidden
- Countdown Timer is hidden
- Countdown Status Message is hidden

Displays:

```text
It's Lunch Time
```

using bold formatting.

### Countdown Display Format

Previous format:

```text
01:23:45
```

New format:

```text
01 hrs : 23 mins : 45 secs
```

to improve readability.

### Lunch Duration Setting

Added:

```python
duration_minutes
```

to lunch configuration settings.

Default:

```python
60
```

Future versions may expose this through the Settings interface.

### Application Icon Foundation

Added support for application icon architecture.

Created icon theme collection:

- White
- Blue
- Brown
- Cyan
- Green
- Grey
- Magenta
- Orange
- Purple
- Red
- Yellow

Default icon:

```text
icon_utensil-clock_white_BG.ico
```

### Appearance Settings

Added:

```python
settings["appearance"]["icon_theme"]
```

for future icon customization support.

Default:

```python
white
```

---

## Changed

### Architecture

Project responsibilities are now organized as:

```text
settings.py
    Settings Data

audio.py
    Audio Logic

loadouts.py
    Persistence

countdown.py
    Countdown Logic

ui.py
    User Interface

main.py
    Application Startup
```

### Main Entry Point

Main application logic was simplified and responsibilities reduced.

### User Interface

User interface creation and countdown behavior are now fully separated.

---

## Removed

### Build Directory

The `build` directory included in Version 3.0 is no longer retained within the project structure.

The folder was preserved in Version 3.0 for educational purposes and documentation of the PyInstaller build process.

---

## Planned

### Version 3.2

- Runtime icon selection
- Audio customization
- Audio frequency controls
- Audio duration controls
- Audio loudness controls
- Lunch start/end sounds
- Font customization
- Loadout management expansion

---

# Version 3.0

Release Date: 2026-11-04

## Added

### Modular Project Structure

Introduced dedicated application modules:

- settings.py
- audio.py
- loadouts.py
- countdown.py
- ui.py

### Persistence System

Added JSON-based settings persistence.

Created:

```text
loadouts/
    Default.json
```

### PyInstaller Support

Added executable build workflow.

Generated:

```text
build/
dist/
main.spec
```

### Audio Feedback

Added custom button-click audio feedback.

Current implementation:

- 900 Hz
- 1000 Hz

### Settings Persistence

Application now automatically:

- Loads settings on startup
- Saves settings to disk
- Restores settings after restart

### Loadout Foundation

Created the underlying architecture required for future loadout management.

---

## Changed

### Settings Architecture

Settings now use:

```python
default_settings
settings
working_settings
```

to support previews and future customization.

### Project Architecture

Refactored project into dedicated ownership modules.

### Build Workflow

Introduced executable packaging through PyInstaller.

---

## Planned

### Version 3.1

- Countdown migration
- UI migration
- Icon support
- Lunch-state behavior

---

# Version 2.2

Release Date: 2026-11-03

## Added

### Settings Persistence

Implemented JSON-based settings storage.

### Loadout Directory

Added automatic creation of:

```text
loadouts/
```

directory.

### Default Configuration

Added automatic creation of:

```text
Default.json
```

on first startup.

### Startup Initialization

Application now:

- Creates required data files
- Loads settings automatically

---

## Changed

### Save Workflow

Save now writes configuration to disk.

### Application Startup

Settings are automatically restored when the application launches.

---

## Planned

### Version 3.0

- Modular architecture
- PyInstaller support
- Dedicated modules

---

# Version 2.1

Release Date: 2026-11-03

## Added

### Color Picker Integration

Added Windows color picker support.

Added customization for:

- Current Time
- Lunch Time
- Countdown Display
- Status Message

### Preview System

Added:

```python
working_settings
```

architecture.

### Save / Cancel Workflow

Users can now:

- Preview settings
- Save settings
- Cancel changes

### Single Settings Window

Prevents multiple Settings windows from opening simultaneously.

---

## Changed

### Settings Management

Settings edits now occur through temporary working copies before permanent application.

---

## Planned

### Version 2.2

- JSON persistence
- Loadouts
- Automatic settings loading

---

# Version 2.0

Release Date: 2026-11-03

## Added

### Audio System

Added button click sounds.

### Toggle Settings

Introduced:

- Button Click Sounds
- Live Preview
- Always On Top

### Modular Settings Architecture

Introduced:

```python
settings = {}
```

foundation.

### Audio Settings Section

Added dedicated audio settings category.

### Toggle Settings Section

Added dedicated toggle management section.

---

## Changed

### Project Direction

Shifted application from a simple countdown timer toward a fully customizable desktop utility.

---

## Planned

### Version 2.1

- Color picker support
- Save/Cancel
- Preview functionality

---

# Version 1.1

Release Date: 2026-11-02

## Added

- Continuous countdown functionality
- Settings button
- Settings window
- Settings categories using LabelFrames
- Modular settings architecture
- Independent display labels

## Changed

- Refactored display structure
- Moved application settings into a centralized settings dictionary
- Prepared application for future customization

## Planned

- Color picker support
- Settings persistence
- Theme support

---

# Version 1.0

Release Date: 2026-11-02

## Initial Release

### Added

- Current time display
- Lunch time display
- Live countdown timer
- Automatic refresh every second

### Technologies

- Python
- Tkinter
- Datetime

### Purpose

Proof-of-concept desktop application for tracking time remaining until lunch.