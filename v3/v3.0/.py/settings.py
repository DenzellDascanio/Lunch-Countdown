import copy


# =====================================================
# Application Constants
# =====================================================

LOADOUT_DIRECTORY = "loadouts"

DEFAULT_LOADOUT_NAME = "Default"


# =====================================================
# Default Settings
# =====================================================

default_settings = {

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


settings = copy.deepcopy(
    default_settings
)


working_settings = None
