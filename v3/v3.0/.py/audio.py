import winsound

from settings import settings


# =====================================================
# Audio Functions
# =====================================================

def play_button_click():

    # Only play audio if the user has enabled it
    if settings["audio"]["button_click_enabled"]:

        winsound.Beep(
            900,
            20
        )

        winsound.Beep(
            1000,
            20
        )
