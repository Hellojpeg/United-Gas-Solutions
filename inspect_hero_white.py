from PIL import Image

im = Image.open("assets/hero_visual.jpg")
white_x = []
white_y = []
for y in range(im.height):
    for x in range(im.width):
        r, g, b, *a = im.getpixel((x, y))
        if r > 240 and g > 240 and b > 240:
            white_x.append(x)
            white_y.append(y)

print(f"White x range in hero_visual: [{min(white_x)}, {max(white_x)}], y range: [{min(white_y)}, {max(white_y)}]")
