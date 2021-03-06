# console_images
# [Russian docs](https://github.com/LedinecMing/console_images/blob/main/docs/Russian.md)
Console images in 48 colors, 216 colors and full rgb
# [PYPI PROJECT](https://pypi.org/project/console-images/)
# Full RGB
![Full rgb](https://raw.githubusercontent.com/LedinecMing/console_images/main/examples/full_rgb.png)  
# 216 colors
![216 colors](https://raw.githubusercontent.com/LedinecMing/console_images/main/examples/216%20colors.png)  
# 48 colors
![48 colors](https://raw.githubusercontent.com/LedinecMing/console_images/main/examples/48%20colors.jpeg)  
If it does not work maybe you should change color_function to color_it48 or color_it216 (maybe you use windows)

Console color schemes:  
[216 colors](https://robotmoon.com/256-colors/)  
[Full RGB](https://gist.github.com/XVilka/8346728)
# Color circles
![Full RGB](/examples/color-circle.png)
![216](/examples/color-circle1.png)
![48](/examples/color-circle2.png)

To create your own use this instruction ->
```py
from PIL import Image
from console_images import print_image, TextImage
print_image(TextImage(Image.open("filepath.ext"), (width, height)))
```
Or for gifs
```py
from console_images import show_gif
show_gif("filepath.gif", framerate = 30)
```
Many images at time
```py
from PIL import Image
from console_images import print_images, TextImage
print_images(TextImage(...), TextImage(...))
```
Many gifs at time
```py
from console_images import show_gifs
show_gifs("filepath.ext", "filepath1.ext", size = (width, height))
```
If this does not work then try to use other color_function
```py
from PIL import Image
from console_images import print_image
from console_images.palette import color_it_48bit
print_image(TextImage(Image.open("filepath.ext"), (width, height)), color_function = color_it_48bit)
```
