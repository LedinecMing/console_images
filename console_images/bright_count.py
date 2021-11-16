from PIL import Image, ImageDraw

"""GIVES YOU BRIGHT TABLE"""

s: dict[str, int] = {}
for i in range(12, 10000):
    image: Image = Image.new("L", (10, 14))
    try:
        ImageDraw.Draw(image).text((0, 0), chr(i), 255)
    except UnicodeError:
        continue
    c = 0
    for x in range(image.height):
        for y in range(image.width):
            if image.getpixel((y, x)) == 255:
                c += 1
    if c not in s.items():
        s[chr(i)] = c
for i in sorted(s.items(), key=lambda n: n[1]):
    print(i[0], end="")
