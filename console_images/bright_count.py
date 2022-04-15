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

from PIL import Image, ImageDraw

__all__: list[str] = ["get_brightness_table",
           "get_brightness"]

def get_brightness(char) -> int:
    image: Image = Image.new("L", (10, 14))

    try:
        ImageDraw.Draw(image).text((0, 0), chr(i), 255)
    except UnicodeError:
        return -1

    weight = 0
    for x in range(image.height):
        for y in range(image.width):
            if image.getpixel((y, x)) == 255:
                weight += 1
    return weight


def get_brightness_table(range_: range = range(12, 10000) -> dict[str, int]:
    char_weight: dict[str, int] = {}

    for char in range_:
        weight: int = get_brightness(chr(char))
        if weight == -1:
            continue
        elif weight not in s.items():
            char_weight[chr(char)] = weight
        
    return char_weight

                         
if __name__ == "__main__":
    print(get_brightness_table())
                         
