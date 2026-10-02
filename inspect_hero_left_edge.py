from PIL import Image

src = Image.open("/Users/juanpablogomez/Downloads/United Gas Solutions Homepage.png")

# Check x=240..300, y=50..250
# The title "THE LEADER BY DESIGN" is large bold text.
# Let's see how far right the letters extend:
title_x = []
for y in range(40, 160):
    for x in range(20, 350):
        r, g, b, *a = src.getpixel((x, y))
        if r > 240 and g > 240 and b > 240:
            title_x.append(x)

if title_x:
    print(f"Hero title text extends from x={min(title_x)} to x={max(title_x)}")

desc_x = []
for y in range(160, 220):
    for x in range(20, 350):
        r, g, b, *a = src.getpixel((x, y))
        if r > 180 and g > 180 and b > 180:
            desc_x.append(x)

if desc_x:
    print(f"Hero description text extends from x={min(desc_x)} to x={max(desc_x)}")

# Secondary button "EXPLORE OUR SERVICES":
# In hero, next to "PARTNER WITH US":
# Let's find "EXPLORE OUR SERVICES" button border/text:
sec_btn_x = []
for y in range(220, 255):
    for x in range(140, 320):
        r, g, b, *a = src.getpixel((x, y))
        if r > 200 and g > 200 and b > 200:
            sec_btn_x.append(x)

if sec_btn_x:
    print(f"Secondary button 'EXPLORE OUR SERVICES' extends from x={min(sec_btn_x)} to x={max(sec_btn_x)}")

# What about the side badge "SAFE / RELIABLE / RESPONSIVE / BUILT TO SCALE"?
badge_x = []
for y in range(190, 260):
    for x in range(600, 724):
        r, g, b, *a = src.getpixel((x, y))
        if r > 220 and g > 220 and b > 220:
            badge_x.append(x)

if badge_x:
    print(f"Side badge text extends from x={min(badge_x)} to x={max(badge_x)}")

