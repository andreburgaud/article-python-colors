"""
Test module color. Requires Python 3.
"""

import sys
import color


def test():
    """Simple Python test for color."""
    default_colors = color.get_text_attr()  # Save default attributes to reset later
    _, _, bg_color, bg_intensity = color.get_distinct_attr()
    color.set_text_attr(
        bg_color | bg_intensity | color.FOREGROUND_BLUE | color.FOREGROUND_INTENSITY
    )
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
    color.set_text_attr(
        bg_color | bg_intensity | color.FOREGROUND_RED | color.FOREGROUND_INTENSITY
    )
    print("===========================================")
    color.set_text_attr(default_colors)  # Reset to default console attributes


if __name__ == "__main__":
    test()
