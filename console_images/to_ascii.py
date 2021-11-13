import typing

from dataclasses import dataclass
from PIL import Image, ImageSequence
from time import sleep

from symbol_table import SymbolTable
from term import get_terminal_size, clear_term
from palette import color_it_full

__all__: typing.Sequence = ["generate_image",
                            "print_image",
                            "print_images",
                            "show_gif",
                            "TextImage"]

ascii_table: SymbolTable = SymbolTable([' ', '.', ':', "'",
                                        ',', '-', ';', '_',
                                        '"', '+', '°', '•',
                                        '^', '=', '|', '(',
                                        '[', '{', "∆", '©',
                                        '®', '&', "$", "@",
                                        '%', '#', '¶'])
block_table: SymbolTable = SymbolTable([" ", "▂", "▃", "▄",
                                        "▅", "▆", "▇", "█"])


@dataclass
class TextImage:
    image: Image
    size: typing.Tuple[int, int]
    table: SymbolTable = block_table

    def to_convertable(self) -> Image:
        """Make image ready to text convert"""
        image = self.image.convert("RGB")
        image = image.resize(self.size)

        return image


def print_image(text_image: TextImage,
                color_function: typing.Callable[
                    [typing.Tuple
                     [int, int, int]], str] = color_it_full
                ) -> None:
    """Print one image"""
    image: Image \
        = text_image.to_convertable()
    image_grayscale: Image.Image = image.convert("L")
    for i in range(0, image.height):
        for j in range(0, image.width):
            print(color_function(image.getpixel((j, i))) +
                  text_image.table.get_symbol(
                      image_grayscale.getpixel((j, i))),
                  end='')
        print()


def print_images(*text_images: typing.Sequence[TextImage],
                 sep: str = ""):
    image_generators: typing.Sequence[typing.Generator] = \
        list(map(lambda t_image: generate_image(t_image), text_images))
    max_size: int = \
        max(list(map(lambda t_image: t_image.size[1], text_images)))

    for current_line in range(max_size):
        print(*list(
            map(lambda img_generator:
                img_generator.__next__(), image_generators)),
              sep=sep)


def generate_image(text_image: TextImage,
                   color_function: typing.Callable[
                       [typing.Tuple
                        [int, int, int]], str] = color_it_full
                   ) -> typing.Generator:
    """String generator of image"""
    image: Image = text_image.to_convertable()
    image_grayscale: Image.Image = image.convert("L")
    for i in range(0, image.height):
        result: str = ""
        for j in range(0, image.width):
            result += color_function(image.getpixel((j, i))) + \
                      text_image.table.get_symbol(
                          image_grayscale.getpixel((j, i)))
        yield result


def show_gif(path: str,
             frame_rate: int = 30,
             table: SymbolTable = block_table,
             color_function: typing.Callable[
                 [typing.Tuple
                  [int, int, int]], str] = color_it_full
             ) -> None:
    """Slideshow in a console, doesnt work with mp4"""
    gif: Image.Image = Image.open(path)
    while True:
        for image in ImageSequence.Iterator(gif):
            columns, rows = get_terminal_size()
            text_image: TextImage = TextImage(image,
                                              (columns, rows),
                                              table=table)
            image: Image = text_image.to_convertable()
            image_grayscale: Image = image.convert("L")
            for i in range(0, image.height):
                for j in range(0, image.width):
                    print(
                        color_function(image.getpixel((j, i))) +
                        table.get_symbol(
                            image_grayscale.getpixel((j, i))),
                        end='')
                print()

            sleep(1 / frame_rate)
            clear_term()
