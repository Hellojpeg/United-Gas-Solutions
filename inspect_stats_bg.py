from PIL import Image

im = Image.open("assets/performance_stats_bg.jpg")
print("performance_stats_bg size:", im.size)
# Check for yellow pixels (r>180, g>140, b<80)
yellows = []
for y in range(im.height):
    for x in range(im.width):
        r, g, b, *a = im.getpixel((x, y))
        if r > 180 and g > 140 and b < 80:
            yellows.append((x, y))

print("Yellow pixels in performance_stats_bg:", len(yellows))
