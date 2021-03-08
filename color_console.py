"""
Test module color_console. Requires Python 3.
"""

import color_console as cons
import sys


def test():
    """Simple Python test for color."""
    default_colors = cons.get_text_attr()
    default_bg = default_colors & 0x0070
    default_fg = default_colors & 0x0007
    cons.set_text_attr(cons.FOREGROUND_BLUE | default_bg | cons.FOREGROUND_INTENSITY)
    print("===========================================")
    cons.set_text_attr(
        cons.FOREGROUND_BLUE
        | cons.BACKGROUND_GREY
        | cons.FOREGROUND_INTENSITY
        | cons.BACKGROUND_INTENSITY
    )
    print("And Now for Something", end=" ")
    sys.stdout.flush()  # Force writing first part of the line in blue
    cons.set_text_attr(
        cons.FOREGROUND_RED
        | cons.BACKGROUND_GREY
        | cons.FOREGROUND_INTENSITY
        | cons.BACKGROUND_INTENSITY
    )
    print("Completely Different!")
    cons.set_text_attr(default_colors)
    cons.set_text_attr(cons.FOREGROUND_RED | default_bg | cons.FOREGROUND_INTENSITY)
    print("===========================================")
    cons.set_text_attr(default_colors)


if __name__ == "__main__":
    test()
