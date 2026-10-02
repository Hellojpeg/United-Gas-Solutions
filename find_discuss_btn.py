from PIL import Image

src = Image.open("/Users/juanpablogomez/Downloads/United Gas Solutions Homepage.png")

# Search for the button "DISCUSS A PROJECT" in y=1380..1440
# The button is dark navy/black background with white border and text
btn_pixels = []
for y in range(1380, 1445):
    for x in range(300, 560):
        r, g, b, *a = src.getpixel((x, y))
        # Look for white text pixels
        if r > 200 and g > 200 and b > 200:
            btn_pixels.append((x, y))

if btn_pixels:
    min_x = min(p[0] for p in btn_pixels)
    max_x = max(p[0] for p in btn_pixels)
    min_y = min(p[1] for p in btn_pixels)
    max_y = max(p[1] for p in btn_pixels)
    print(f"Discuss button text detected at x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]")
else:
    print("Not found in search range")
