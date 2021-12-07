import random
from PIL import Image

flag = 0
while flag == 0:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    if r != 0 and b != 0 and g != 0:
        flag = 1

top = Image.open("WalppaperIn.png")
ultatop = Image.new("RGBA", top.size, (0, 0, 0, 100))
back = Image.new("RGB", top.size, color=(r, g, b))
back.paste(top, (0, 0), top)
back.paste(ultatop, (0, 0), ultatop)

#back.show()
back.save("Wallpaper.jpg")



