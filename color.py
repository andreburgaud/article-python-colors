"""
Colors text in console mode application (win32).
Uses ctypes and Win32 methods SetConsoleTextAttribute and
GetConsoleScreenBufferInfo.
"""

import ctypes

SHORT = ctypes.c_short
WORD = ctypes.c_ushort


class COORD(ctypes.Structure):
    """struct in wincon.h."""

    _fields_ = [("X", SHORT), ("Y", SHORT)]


class SMALL_RECT(ctypes.Structure):
    """struct in wincon.h."""

    _fields_ = [("Left", SHORT), ("Top", SHORT), ("Right", SHORT), ("Bottom", SHORT)]


class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
    """struct in wincon.h."""

    _fields_ = [
        ("dwSize", COORD),
        ("dwCursorPosition", COORD),
        ("wAttributes", WORD),
        ("srWindow", SMALL_RECT),
        ("dwMaximumWindowSize", COORD),
    ]


# winbase.h
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

# wincon.h
FOREGROUND_BLACK = 0x0000
FOREGROUND_BLUE = 0x0001
FOREGROUND_GREEN = 0x0002
FOREGROUND_CYAN = 0x0003
FOREGROUND_RED = 0x0004
FOREGROUND_MAGENTA = 0x0005
FOREGROUND_YELLOW = 0x0006
FOREGROUND_GREY = 0x0007
FOREGROUND_INTENSITY = 0x0008  # foreground color is intensified.

BACKGROUND_BLACK = 0x0000
BACKGROUND_BLUE = 0x0010
BACKGROUND_GREEN = 0x0020
BACKGROUND_CYAN = 0x0030
BACKGROUND_RED = 0x0040
BACKGROUND_MAGENTA = 0x0050
BACKGROUND_YELLOW = 0x0060
BACKGROUND_GREY = 0x0070
BACKGROUND_INTENSITY = 0x0080  # background color is intensified.

stdout_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
SetConsoleTextAttribute = ctypes.windll.kernel32.SetConsoleTextAttribute
GetConsoleScreenBufferInfo = ctypes.windll.kernel32.GetConsoleScreenBufferInfo


def get_text_attr() -> WORD:
    """Returns the character attributes (colors) of the console screen
    buffer."""
    csbi = CONSOLE_SCREEN_BUFFER_INFO()
    GetConsoleScreenBufferInfo(stdout_handle, ctypes.byref(csbi))
    return csbi.wAttributes


def get_distinct_attr() -> (WORD, WORD, WORD, WORD):
    """Returns a tuple with 4 values: foreground color, foreground intensity,
    background color, and background intensity"""
    attr = get_text_attr()
    return (
        attr & FOREGROUND_GREY,
        attr & FOREGROUND_INTENSITY,
        attr & BACKGROUND_GREY,
        attr & BACKGROUND_INTENSITY,
    )


def set_text_attr(color: int) -> None:
    """Sets the character attributes (colors) of the console screen
    buffer. Color is a combination of foreground and background color,
    foreground and background intensity."""
    SetConsoleTextAttribute(stdout_handle, color)
