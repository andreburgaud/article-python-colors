"""
Test module color. Requires Python 3.
"""


import sys
import color


def test():
    """Simple Python test for color."""
    default_colors = color.get_text_attr()
    default_bg = default_colors & 0x0070
    color.set_text_attr(color.FOREGROUND_BLUE | default_bg | color.FOREGROUND_INTENSITY)
    print("===========================================")
    color.set_text_attr(
        color.FOREGROUND_BLUE
        | color.BACKGROUND_GREY
        | color.FOREGROUND_INTENSITY
        | color.BACKGROUND_INTENSITY
    )
    print("And Now for Something", end=" ")
    sys.stdout.flush()  # Force writing first part of the line in blue
    color.set_text_attr(
        color.FOREGROUND_RED
        | color.BACKGROUND_GREY
        | color.FOREGROUND_INTENSITY
        | color.BACKGROUND_INTENSITY
    )
    print("Completely Different!")
    color.set_text_attr(default_colors)
    color.set_text_attr(color.FOREGROUND_RED | default_bg | color.FOREGROUND_INTENSITY)
    print("===========================================")
    color.set_text_attr(default_colors)


if __name__ == "__main__":
    test()
