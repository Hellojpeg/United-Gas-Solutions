from PIL import Image

src = Image.open("/Users/juanpablogomez/Downloads/United Gas Solutions Homepage.png")

# Let's inspect where the hero buttons are:
# In the original image, "PARTNER WITH US →" is a yellow button around y=220..250
# Let's find its x-span
for y in range(220, 250, 5):
    row = []
    for x in range(0, 320, 10):
        r, g, b, *a = src.getpixel((x, y))
        # yellow is high r, high g, low b
        if r > 180 and g > 140 and b < 80:
            row.append(x)
    if row:
        print(f"Hero button yellow detected at y={y}, x in [{min(row)}, {max(row)}]")

# Look at "DISCUSS A PROJECT →" in partners section:
# y=1390..1430
for y in range(1390, 1435, 5):
    for x in range(350, 500, 5):
        r, g, b, *a = src.getpixel((x, y))
        # It's a dark button with white text and border
# Look at "OUR SAFETY STANDARDS →" in safety section:
for y in range(910, 945, 5):
    row = []
    for x in range(20, 200, 5):
        r, g, b, *a = src.getpixel((x, y))
        if r > 180 and g > 140 and b < 80:
            row.append(x)
    if row:
        print(f"Safety button yellow detected at y={y}, x in [{min(row)}, {max(row)}]")

# Look at "THE UGS ADVANTAGE →" in tech section:
for y in range(1090, 1125, 5):
    row = []
    for x in range(20, 200, 5):
        r, g, b, *a = src.getpixel((x, y))
        if r > 180 and g > 140 and b < 80:
            row.append(x)
    if row:
        print(f"Tech button yellow detected at y={y}, x in [{min(row)}, {max(row)}]")

# Look at "OUR COVERAGE →" in coverage section:
for y in range(1250, 1285, 5):
    row = []
    for x in range(350, 500, 5):
        r, g, b, *a = src.getpixel((x, y))
        if r > 180 and g > 140 and b < 80:
            row.append(x)
    if row:
        print(f"Coverage button yellow detected at y={y}, x in [{min(row)}, {max(row)}]")

# Look at "EXPLORE CAREERS →" in careers section:
for y in range(1630, 1665, 5):
    row = []
    for x in range(20, 200, 5):
        r, g, b, *a = src.getpixel((x, y))
        if r > 180 and g > 140 and b < 80:
            row.append(x)
    if row:
        print(f"Careers button yellow detected at y={y}, x in [{min(row)}, {max(row)}]")

# Look at "PARTNER WITH UNITED GAS SOLUTIONS →" in skyline CTA:
for y in range(1740, 1785, 5):
    row = []
    for x in range(200, 520, 10):
        r, g, b, *a = src.getpixel((x, y))
        if r > 180 and g > 140 and b < 80:
            row.append(x)
    if row:
        print(f"Skyline CTA button yellow detected at y={y}, x in [{min(row)}, {max(row)}]")

