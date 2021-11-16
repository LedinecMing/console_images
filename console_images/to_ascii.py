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

import colorama

from dataclasses import dataclass
from PIL import Image, ImageSequence
from time import sleep

from .symbol_table import SymbolTable
from .term import get_terminal_size, clear_term
from .palette import color_it_full

colorama.init()

__all__: typing.Sequence[str] = ["generate_image",
                                 "print_image",
                                 "print_images",
                                 "show_gif",
                                 "show_gifs",
                                 "TextImage",
                                 "ascii_table",
                                 "block_table",
                                 "fucking_big_table"]

ascii_table: SymbolTable = SymbolTable([' ', '.', ':', "'",
                                        ',', '-', ';', '_',
                                        '"', '+', '°', '•',
                                        '^', '=', '|', '(',
                                        '[', '{', "∆", '©',
                                        '®', '&', "$", "@",
                                        '%', '#', '¶'])
block_table: SymbolTable = SymbolTable([" ", "▂", "▃", "▄",
                                        "▅", "▆", "▇", "█"])
fucking_big_table: SymbolTable = SymbolTable([char
                                              for
                                              char in
                                              (".¨´·',:`¯¸-;_~°|¬³¹÷/=\\^¦²" +
                                               "*+×!<>ºª()?¡¤±¿vIc{}Jr¢ìíïF" +
                                               "LTV[]eimow»¼½¾ÌÍÏæî7Cjnsz©«" +
                                               "Îç&1WXYltx§®Þèéëòóö%£êôø#24" +
                                               "EGOZyÇÝàáäAKÐßâõ3MPSafuBDNQ" +
                                               "Ubhkµ¶ÒÓÖØû8RpÀÁÄÈÉËÔãñýÿ0d" +
                                               "ÛðÃgq¥ÂÊÙÅþÑÚÜå$HÆÕ")[::-1]])


@dataclass
class TextImage:
    image: Image.Image
    size: typing.Tuple[int, int]
    table: SymbolTable = block_table

    def to_convertable(self) -> Image.Image:
        """Make image ready to text convert"""
        image = self.image.convert("RGB")
        image = image.resize(self.size)

        return image


def print_image(text_image: TextImage,
                color_function: typing.Callable[
                    [typing.Tuple
                     [int, int, int],
                     bool], str] = color_it_full,
                dizering: bool = False
                ) -> None:
    """Print one image"""
    image: Image.Image \
        = text_image.to_convertable()
    image_grayscale: Image.Image = image.convert("L")
    for i in range(0, image.height):
        result: str = ""
        for j in range(0, image.width):
            result += color_function(image.getpixel((j, i)),
                                     dizering) + \
                      text_image.table.get_symbol(
                          image_grayscale.getpixel((j, i)))
        print(result)
    print(colorama.Style.RESET_ALL)


def print_images(*text_images: TextImage,
                 sep: str = "",
                 color_function: typing.Callable[
                     [typing.Tuple
                      [int, int, int],
                      bool], str] = color_it_full,
                 dizering: bool = False
                 ) -> None:
    """Print many images separated by sep"""
    image_generators: typing.Dict[typing.Generator[
                                      str, None, None], TextImage] = \
        {generate_image(t_image[1],
                        color_function=color_function,
                        dizering=dizering): t_image[1]
         for t_image in enumerate(text_images)}
    max_size: int = max([t_image.size[1] for t_image in text_images])

    for current_line in range(max_size):
        print(*[next(img_generator)
                for img_generator, t_image_index
                in image_generators.items()],
              sep=sep)
    print(colorama.Style.RESET_ALL)


def generate_image(text_image: TextImage,
                   color_function: typing.Callable[
                       [typing.Tuple
                        [int, int, int],
                        bool], str] = color_it_full,
                   dizering: bool = False
                   ) -> typing.Generator[str, None, None]:
    """String generator of image"""
    image: Image.Image = text_image.to_convertable()
    image_grayscale: Image.Image = image.convert("L")
    for i in range(0, image.height):
        result: str = ""
        for j in range(0, image.width):
            result += color_function(image.getpixel((j, i)),
                                     dizering) + \
                      text_image.table.get_symbol(
                          image_grayscale.getpixel((j, i)))
        yield result


def show_gif(path: str,
             frame_rate: int = 30,
             table: SymbolTable = block_table,
             color_function: typing.Callable[
                 [typing.Tuple
                  [int, int, int],
                  bool], str] = color_it_full,
             dizering: bool = False
             ) -> None:
    """Slideshow in a console, doesnt work with mp4"""
    gif: Image.Image = Image.open(path)
    while True:
        for image in ImageSequence.Iterator(gif):
            columns, rows = get_terminal_size()
            text_image: TextImage = TextImage(image,
                                              (columns, rows),
                                              table=table)
            image = text_image.to_convertable()
            image_grayscale: Image.Image = image.convert("L")
            for i in range(0, image.height):
                for j in range(0, image.width):
                    print(
                        color_function(
                            image.getpixel((j, i)), dizering) +
                        table.get_symbol(
                            image_grayscale.getpixel((j, i))),
                        end='')
                print()

            sleep(1 / frame_rate)
            clear_term()


def show_gifs(*gif_paths: str,
              size: tuple[int, int],
              sep: str = "",
              frame_rate: int = 30,
              table: SymbolTable = block_table,
              color_function: typing.Callable[
                 [typing.Tuple
                  [int, int, int],
                  bool], str] = color_it_full,
              dizering: bool = False
              ) -> None:
    """Many slideshows!"""
    gifs: list[Image.Image] = [Image.open(path) for path in gif_paths]
    while True:
        gifs_iters: list[ImageSequence.Iterator] = \
            [ImageSequence.Iterator(gif) for gif in gifs]

        for image in gifs_iters[0]:
            clear_term()
            print_images(
                *[TextImage(image, size, table=table)] +
                 [TextImage(next(gif_iter),
                            size,
                            table=table)
                  for gif_iter in gifs_iters[1:]],
                sep=sep,
                color_function=color_function,
                dizering=dizering)
            sleep(1 / frame_rate)
