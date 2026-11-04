import json
import os

from settings import (
    settings,
    default_settings,
    LOADOUT_DIRECTORY,
    DEFAULT_LOADOUT_NAME
)


# =====================================================
# Loadout Functions
# =====================================================

def create_loadout_directory():

    os.makedirs(
        LOADOUT_DIRECTORY,
        exist_ok=True
    )


def get_loadout_path(loadout_name):

    return os.path.join(
        LOADOUT_DIRECTORY,
        f"{loadout_name}.json"
    )


def save_loadout(loadout_name):

    create_loadout_directory()

    loadout_path = get_loadout_path(
        loadout_name
    )

    with open(
        loadout_path,
        "w"
    ) as loadout_file:

        json.dump(
            settings,
            loadout_file,
            indent=4
        )


def load_loadout(loadout_name):

    loadout_path = get_loadout_path(
        loadout_name
    )

    with open(
        loadout_path,
        "r"
    ) as loadout_file:

        loaded_settings = json.load(
            loadout_file
        )

    settings.clear()

    settings.update(
        loaded_settings
    )


def initialize_default_loadout():

    create_loadout_directory()

    default_path = get_loadout_path(
        DEFAULT_LOADOUT_NAME
    )

    if not os.path.exists(
        default_path
    ):

        with open(
            default_path,
            "w"
        ) as loadout_file:

            json.dump(
                default_settings,
                loadout_file,
                indent=4
            )


def initialize_application():

    initialize_default_loadout()
    
    load_loadout(DEFAULT_LOADOUT_NAME)
