from PIL import Image

img = Image.open("/Users/juanpablogomez/Downloads/United Gas Solutions Homepage.png")

# Let's inspect rows:
# Print average RGB of each 20-pixel vertical slice
for y in range(0, img.height, 30):
    total_r, total_g, total_b = 0, 0, 0
    samples = 50
    for x in range(0, img.width, img.width // samples):
        r, g, b, *a = img.getpixel((x, y))
        total_r += r
        total_g += g
        total_b += b
    ar = total_r // samples
    ag = total_g // samples
    ab = total_b // samples
    print(f"y={y:4d}: avg rgb=({ar:3d},{ag:3d},{ab:3d})")
