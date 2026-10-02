from PIL import Image

src = Image.open("/Users/juanpablogomez/Downloads/United Gas Solutions Homepage.png")

# Let's inspect partners section (y=1315 to 1465)
# In the original design:
# Where does the photo start?
# Let's find where the background changes from light gray to the dark industrial photo
for x in range(300, 720, 10):
    r, g, b, *a = src.getpixel((x, 1380))
    print(f"x={x}: rgb=({r},{g},{b})")

