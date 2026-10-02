from PIL import Image

img = Image.open("/Users/juanpablogomez/Downloads/United Gas Solutions Homepage.png")

# Let's inspect colors along y to detect section transitions
# Sample the middle x=362 or left x=50
transitions = []
prev_color = None
for y in range(0, img.height, 2):
    r, g, b, *a = img.getpixel((50, y))
    # print significant color shifts
