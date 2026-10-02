from PIL import Image

im = Image.open("assets/hero_visual.jpg")
# The crop starts at x=260 in original
# Let's find coordinates of yellow pixels in hero_visual:
yellow_x = []
yellow_y = []
for y in range(im.height):
    for x in range(im.width):
        r, g, b, *a = im.getpixel((x, y))
        if r > 190 and g > 140 and b < 70:
            yellow_x.append(x)
            yellow_y.append(y)

print(f"Yellow x range in hero_visual: [{min(yellow_x)}, {max(yellow_x)}], y range: [{min(yellow_y)}, {max(yellow_y)}]")
