import typing

import colorama

__all__: typing.List[str] = \
    [
        "color_it_full",
        "color_it216",
        "color_it48"
    ]

pal: typing.List = [0, 95, 135, 175, 215, 255]

colors: typing.Dict[str, typing.List[str]] = \
    {"GREEN": [colorama.Style.DIM + colorama.Fore.GREEN,
               colorama.Fore.GREEN,
               colorama.Style.BRIGHT + colorama.Fore.GREEN,
               colorama.Style.DIM + colorama.Fore.LIGHTGREEN_EX,
               colorama.Fore.LIGHTGREEN_EX, colorama.Style.BRIGHT +
               colorama.Fore.LIGHTGREEN_EX
               ],
     "RED": [colorama.Style.DIM + colorama.Fore.RED,
             colorama.Fore.RED,
             colorama.Style.BRIGHT + colorama.Fore.RED,
             colorama.Style.DIM + colorama.Fore.LIGHTRED_EX,
             colorama.Fore.LIGHTRED_EX,
             colorama.Style.BRIGHT + colorama.Fore.LIGHTRED_EX
             ],
     "YELLOW": [colorama.Style.DIM + colorama.Fore.YELLOW,
                colorama.Fore.YELLOW,
                colorama.Style.BRIGHT + colorama.Fore.YELLOW,
                colorama.Style.DIM + colorama.Fore.LIGHTYELLOW_EX,
                colorama.Fore.LIGHTYELLOW_EX, colorama.Style.BRIGHT +
                colorama.Fore.LIGHTYELLOW_EX
                ],
     "MAGENTA": [colorama.Style.DIM + colorama.Fore.MAGENTA,
                 colorama.Fore.MAGENTA,
                 colorama.Style.BRIGHT + colorama.Fore.MAGENTA,
                 colorama.Style.DIM + colorama.Fore.LIGHTMAGENTA_EX,
                 colorama.Fore.LIGHTMAGENTA_EX, colorama.Style.BRIGHT +
                 colorama.Fore.LIGHTMAGENTA_EX
                 ],
     "CYAN": [colorama.Style.DIM + colorama.Fore.CYAN,
              colorama.Fore.CYAN,
              colorama.Style.BRIGHT + colorama.Fore.CYAN,
              colorama.Style.DIM + colorama.Fore.LIGHTCYAN_EX,
              colorama.Fore.LIGHTCYAN_EX,
              colorama.Style.BRIGHT + colorama.Fore.LIGHTCYAN_EX
              ],
     "WHITE": [colorama.Style.DIM + colorama.Fore.WHITE,
               colorama.Fore.WHITE,
               colorama.Style.BRIGHT + colorama.Fore.WHITE,
               colorama.Style.DIM + colorama.Fore.LIGHTWHITE_EX,
               colorama.Fore.LIGHTWHITE_EX,
               colorama.Style.BRIGHT + colorama.Fore.LIGHTWHITE_EX
               ],
     "BLACK": [colorama.Style.DIM + colorama.Fore.BLACK,
               colorama.Fore.BLACK,
               colorama.Style.BRIGHT + colorama.Fore.BLACK,
               colorama.Style.DIM + colorama.Fore.LIGHTBLACK_EX,
               colorama.Fore.LIGHTBLACK_EX, colorama.Style.BRIGHT +
               colorama.Fore.LIGHTBLACK_EX
               ],
     "BLUE": [colorama.Style.DIM + colorama.Fore.BLACK,
              colorama.Fore.BLACK,
              colorama.Style.BRIGHT + colorama.Fore.BLACK,
              colorama.Style.DIM + colorama.Fore.LIGHTBLACK_EX,
              colorama.Fore.LIGHTBLACK_EX,
              colorama.Style.BRIGHT + colorama.Fore.LIGHTBLACK_EX
              ]
     }


def get_pal(color: typing.Tuple[int, int, int]) -> typing.List[int]:
    col_data: typing.List[int] = []
    for col in color:
        added: bool = False
        for i in enumerate(pal[1:]):
            added = False
            if (col - pal[i[0]]) / (i[1] - pal[i[0]]) < 0.5:
                col_data.append(i[0])
                added = True
                break
        if not added:
            col_data.append(len(pal) - 1)
    return col_data


def color_it48(color: typing.Tuple[int, int, int]):
    if all([col > 240 for col in color]) and\
            color[0] * 3 - 10 < sum(color) < color[0] * 3 + 10:
        return colors["WHITE"][
            round((len(colors["WHITE"]) - 1)
                  / 255 * (color[1] + color[2]) / 2)]
    if all([col < 30 for col in color]) and\
            color[0] * 3 - 10 < sum(color) < color[0] * 3 + 10:
        return colors["BLACK"][
            round((len(colors["BLACK"]) - 1)
                  / 255 * (color[1] + color[2]) / 2)]
    if max(color) == color[1] and color[1] > 200:
        return colors["GREEN"][
            round((len(colors["GREEN"]) - 1)
                  / 255 * color[1])]
    if max(color) == color[0] and color[0] > 200:
        return colors["RED"][
            round((len(colors["RED"]) - 1)
                  / 255 * color[0])]
    if max(color) == color[2] and color[2] > 200:
        return colors["BLUE"][
            round((len(colors["BLUE"]) - 1)
                  / 255 * color[0])]
    if color[1] + color[2] > color[0] * 2 + 40:
        return colors["CYAN"][
            round((len(colors["CYAN"]) - 1)
                  / 255 * (color[1] + color[2]) / 2)]
    if color[0] + color[2] > color[1] * 2 + 40:
        return colors["MAGENTA"][
            round((len(colors["MAGENTA"]) - 1)
                  / 255 * (color[2] + color[1]) / 2)]
    if sum(color[0:2]) > color[2] * 2 + 40:
        return colors["YELLOW"][
            round((len(colors["YELLOW"]) - 1)
                  / 255 * (color[1] + color[0]) / 2)]
    return ""


def color_it216(color: typing.Tuple[int, int, int]) -> str:
    color_data: typing.List[int] = get_pal(color)
    return f"\033[05;38;02;" \
           f"{6 ** 2 * color_data[0] + 6 * color_data[1] + color_data[2]}"


def color_it_full(color: typing.Tuple[int, int, int]) -> str:
    return f"\033[38;02;{color[0]};{color[1]};{color[2]}m"
