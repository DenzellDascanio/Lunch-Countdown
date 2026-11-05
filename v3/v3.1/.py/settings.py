'''
settings.py

Owns application settings and configuration data.

Responsibilities:
- Application constants
- Factory-default settings
- Active settings
- Temporary working settings
'''

import copy


# =====================================================
# Application Constants
# =====================================================

LOADOUT_DIRECTORY = "loadouts"

DEFAULT_LOADOUT_NAME = "Default"


# =====================================================
# Default Settings
# =====================================================

# Factory defaults.
# These should never be modified directly.

default_settings = {

    "lunch": {

        "hour": 12,
        "minute": 0,
        "second": 0,

        # Duration of lunch period.
        "duration_minutes": 60

    },

    "audio": {

        "button_click_enabled": True

    },

    "toggles": {

        "live_preview_enabled": True,

        "always_on_top": True

    },

    "colors": {

        "current_time": "green",

        "lunch_time": "blue",

        "countdown": "black",

        "status_message": "red"

    },

    "appearance": {

        "icon_theme": "white"

    }


}


# Active application settings.
# The running application reads settings from here.

settings = copy.deepcopy(
    default_settings
)


# Temporary settings used while editing settings.
# Changes are previewed here until the user saves.

working_settings = None