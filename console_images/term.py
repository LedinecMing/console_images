"""
Copyright 2021 LedinecMing (https://github.com/LedinecMing)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


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
