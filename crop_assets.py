from PIL import Image
import os

img = Image.open("/Users/juanpablogomez/Downloads/United Gas Solutions Homepage.png")
w, h = img.size
os.makedirs("assets", exist_ok=True)

# Let's inspect rows with average color or scan for specific banners
# Let's write a small script that outputs thumbnail sections every 100px so we know exact bounds

for y in range(0, h, 100):
    box = (0, y, w, min(y + 100, h))
    crop = img.crop(box)
    crop.save(f"assets/slice_{y}_{min(y+100, h)}.jpg", quality=85)

print("Saved reference slices!")
