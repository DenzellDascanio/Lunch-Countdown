# Lunch Countdown

Version: 1.1

## Overview

This version expands the original countdown application by introducing a modular architecture designed to support future customization and user settings.

---

## New Features

### Continuous Countdown

When today's lunch period has passed, the application automatically calculates the countdown to tomorrow's lunch period.

The countdown never stops running.

### Settings Window

Added a dedicated Settings button.

Added a Settings window using Tkinter Toplevel.

### Settings Sections

Added organized settings categories using LabelFrames.

Current sections include:

- Lunch Settings
- Color Settings
- Future Features

### Modular Settings Architecture

Introduced a centralized settings dictionary.

Future settings can be added without significant code restructuring.

### Independent Display Labels

The display was refactored from a single label into multiple labels:

- Current Time
- Lunch Time
- Countdown Title
- Countdown Value
- Status Message

This change prepares the application for future:

- Color customization
- Font customization
- Visibility options

---

## Technologies Used

- Python
- Tkinter
- DateTime
- Timedelta

---

## Version Notes

Version 1.1 focuses primarily on architecture and scalability.

The groundwork was established for future user customization and persistent settings.
