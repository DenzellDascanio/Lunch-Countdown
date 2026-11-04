# Lunch Countdown

Version: 3.0

## Overview

Lunch Countdown is a desktop application built using Python and Tkinter.

The application displays:

- Current Time
- Lunch Time
- Time Remaining Until Lunch

The countdown automatically updates every second and continues counting toward the next lunch period once the current day's lunch has passed.

Version 3.0 introduces the project's first major architectural refactor.

Rather than storing all application logic inside a single Python file, functionality is now separated into dedicated modules based on responsibility.

This refactor improves:

- Maintainability
- Readability
- Scalability
- Future feature development

---

## Major Architecture Changes

### Previous Design (v2.x)

The application previously stored:

- Settings
- Audio
- Persistence
- User Interface
- Countdown Logic

inside a single Python file.

While functional, this approach becomes more difficult to maintain as new features are added.

### New Design (v3.0)

Functionality is now separated into dedicated modules.

Each module has a clearly defined responsibility and ownership model.

---

## Project Structure

```text
v3.0
│
├── main.py
│
├── settings.py
│
├── audio.py
│
├── loadouts.py
│
├── countdown.py
│
├── loadouts
│   └── Default.json
│
└── README.md
```

---

## Executable Build

Version 3.0 successfully introduces executable packaging through PyInstaller.

Generated artifacts include:

- build/
- dist/
- main.spec

The executable can be found in:

dist/main.exe

Current deployment requires the loadouts directory to exist alongside the executable.

---

## Module Responsibilities

### main.py

Application entry point.

Current responsibilities:

- Main window creation
- Settings window creation
- Widget creation
- Color selection
- Countdown display updates

Future versions will gradually move additional responsibilities into specialized modules.

---

### settings.py

Owns all application configuration data.

Responsibilities:

- Default settings
- Active settings
- Working settings
- Application constants

Examples:

- Colors
- Audio settings
- Toggle settings
- Lunch settings

This module acts as the central source of truth for application configuration.

---

### audio.py

Owns all audio-related functionality.

Current responsibilities:

- Button click sounds

Current sound profile:

- 900 Hz tone
- 1000 Hz tone

Purpose:

Provide user feedback while keeping audio logic isolated from other application systems.

---

### loadouts.py

Owns application persistence.

Responsibilities:

- Loadout directory creation
- Loadout file creation
- JSON serialization
- JSON deserialization
- Application initialization

Current functionality:

- Automatically creates Default.json
- Automatically loads Default.json
- Automatically saves user settings

---

### countdown.py

Reserved for future countdown ownership.

Planned responsibilities:

- Countdown calculations
- Time formatting
- Countdown update loop
- Future countdown types

Version 3.0 establishes this module as part of the application's architecture.

Countdown migration is planned for a future release.

---

## Settings Persistence

### Default Loadout

The application automatically creates:

```text
loadouts/Default.json
```

when one does not already exist.

### Automatic Loading

Settings are loaded at startup.

### Automatic Saving

Settings are saved when the user selects:

```text
Save
```

within the Settings window.

---

## Current Features

### Countdown Display

Displays:

- Current Time
- Lunch Time
- Countdown Timer

### Continuous Countdown

When lunch for the current day has passed, the application automatically counts down to the next day's lunch period.

### Color Customization

Users may customize:

- Current Time Color
- Lunch Time Color
- Countdown Color
- Status Message Color

### Live Preview

Changes may be previewed before saving.

### Save / Cancel Workflow

Changes may either be:

- Saved permanently
- Discarded

### Audio Feedback

Button click sounds can be enabled or disabled.

### Toggle Settings

Current toggle options:

- Enable Button Click Sounds
- Enable Live Preview
- Always On Top

---

## Development Notes

Version 3.0 focuses on improving the internal software architecture.

Although user-facing functionality remains largely unchanged from Version 2.2, the application's codebase is now organized in a way that supports future expansion and maintenance.

The primary goal of Version 3.0 is establishing clean ownership boundaries between systems.

---

## Planned Features

### Version 3.1

- Migrate countdown functionality into countdown.py
- Begin user-interface migration into dedicated UI modules
- Reduce complexity within main.py

### Version 3.2

- Named loadouts
- Save As New Loadout
- Load Existing Loadout
- Delete Loadout

---

## Technologies Used

- Python
- Tkinter
- Datetime
- JSON
- Winsound

---

## Release Notes

### Version 3.0

Added:

- Modular project structure
- settings.py
- audio.py
- loadouts.py
- countdown.py foundation

Improved:

- Code organization
- Separation of responsibilities
- Future maintainability
- Project scalability

Prepared For:

- Countdown module migration
- UI module migration
- Advanced loadout management
- Future expansion
