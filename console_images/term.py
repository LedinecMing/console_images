import typing

import os
import platform

import warnings

BASE_SIZE: typing.Tuple[int, int] = (100, 70)


def clear_term() -> None:
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")


def get_terminal_size() -> typing.Tuple[int, int]:
    columns: int
    rows: int
    try:
        columns, rows = os.get_terminal_size(0)
    except OSError:
        columns, rows = BASE_SIZE
        warnings.warn("Can not get terminal size, going to use BASE_SIZE")
    return columns, rows
