from PIL import Image
import os

assets = [
    "assets/hero_visual.jpg",
    "assets/who_we_are_technician.jpg",
    "assets/safety_worker.jpg",
    "assets/tech_dispatcher.jpg",
    "assets/built_differently_crew.jpg",
    "assets/us_map_coverage.png",
    "assets/utility_partners_facility.jpg",
    "assets/performance_stats_bg.jpg",
    "assets/careers_team_sunset.jpg",
    "assets/skyline_cta_bg.jpg"
]

for a in assets:
    if not os.path.exists(a):
        continue
    im = Image.open(a)
    # Check for yellow button color (r>190, g>140, b<70)
    yellows = 0
    # Check for bright white text pixels (r>235, g>235, b>235) in dark images
    whites = 0
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, *alpha = im.getpixel((x, y))
            if r > 190 and g > 140 and b < 70:
                yellows += 1
            if r > 240 and g > 240 and b > 240:
                whites += 1
    print(f"{a:35s}: size={im.size}, yellow_px={yellows:5d}, white_px={whites:5d}")
