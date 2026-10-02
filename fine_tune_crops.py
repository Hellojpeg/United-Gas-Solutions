from PIL import Image

src = "/Users/juanpablogomez/Downloads/United Gas Solutions Homepage.png"
img = Image.open(src)
w, h = img.size

# 1. Hero right-side visual (worker + fleet at sunset)
hero_visual = img.crop((260, 0, w, 308))
hero_visual.save("assets/hero_visual.jpg", quality=95)

# Also full hero banner
full_hero = img.crop((0, 0, w, 308))
full_hero.save("assets/hero_full.jpg", quality=95)

# 2. Who We Are technician working on gas pipes
# Let's crop just the photo cleanly (no white border)
who_we_are = img.crop((0, 360, 350, 574))
who_we_are.save("assets/who_we_are_technician.jpg", quality=95)

# 3. 8 Services cards:
# Let's inspect the cards row:
# y starts at 624, ends at 748.
# Let's save both the photo part and the full card with title
card_coords = [
    (14, 624, 98, 748),
    (101, 624, 185, 748),
    (188, 624, 272, 748),
    (275, 624, 359, 748),
    (362, 624, 446, 748),
    (449, 624, 533, 748),
    (536, 624, 620, 748),
    (623, 624, 707, 748)
]

service_slugs = [
    "gas_service_operations",
    "meter_services",
    "turn_ons_reconnects",
    "disconnect_shutoff",
    "meter_renewals",
    "field_inspections",
    "utility_workforce_support",
    "managed_field_operations"
]

for idx, (x1, y1, x2, y2) in enumerate(card_coords):
    slug = service_slugs[idx]
    # Full card
    card_img = img.crop((x1, y1, x2, y2))
    card_img.save(f"assets/card_{slug}.jpg", quality=95)
    # Photo only (top part, before the black label box at the bottom)
    # The black label box starts around y = y1 + 90
    photo_img = img.crop((x1, y1, x2, y1 + 92))
    photo_img.save(f"assets/service_{slug}.jpg", quality=95)

# 4. Safety & Compliance:
# Worker in high-vis vest and hard hat facing back
# Center/right side
safety_visual = img.crop((260, 755, 545, 975))
safety_visual.save("assets/safety_worker.jpg", quality=95)
# Full safety background
safety_full = img.crop((0, 755, w, 975))
safety_full.save("assets/safety_full.jpg", quality=95)

# Veriforce logo
# Let's find exact coordinates of Veriforce logo in the safety section
# It is around x=550..670, y=765..795
veriforce = img.crop((548, 765, 672, 795))
veriforce.save("assets/veriforce_logo.png")

# 5. Technology Operations:
# Center dispatcher photo looking at GIS and work order screens
tech_photo = img.crop((240, 975, 595, 1145))
tech_photo.save("assets/tech_dispatcher.jpg", quality=95)
tech_full = img.crop((0, 975, w, 1145))
tech_full.save("assets/tech_full.jpg", quality=95)

# 6. Built Differently & Map
# Left side photo: crew and truck in yard (x: 0..360, y: 1145..1315)
built_diff_photo = img.crop((0, 1145, 360, 1315))
built_diff_photo.save("assets/built_differently_crew.jpg", quality=95)

# Right side map: US map with Florida glowing (x: 520..715, y: 1148..1295)
us_map = img.crop((524, 1148, 715, 1295))
us_map.save("assets/us_map_coverage.png")

# 7. Utility & Infrastructure Partners
# Right side industrial gas facility with worker overlooking at sunset (x: 575..724, y: 1320..1465)
partners_photo = img.crop((570, 1320, w, 1465))
partners_photo.save("assets/utility_partners_facility.jpg", quality=95)

# 8. Performance stats background
perf_bg = img.crop((0, 1465, w, 1545))
perf_bg.save("assets/performance_stats_bg.jpg", quality=95)

# 9. Careers section
# 4 workers walking towards fleet at sunset
careers_photo = img.crop((295, 1545, w, 1680))
careers_photo.save("assets/careers_team_sunset.jpg", quality=95)

# 10. Pre-footer Skyline CTA Banner
# Illuminated South Florida palm trees and skyline at dusk
skyline_banner = img.crop((0, 1680, w, 1825))
skyline_banner.save("assets/skyline_cta_bg.jpg", quality=95)

# 11. Footer Logo
footer_logo = img.crop((25, 1870, 132, 1945))
footer_logo.save("assets/ugs_footer_logo.png")

# 12. Header Logo
header_logo = img.crop((24, 6, 132, 33))
header_logo.save("assets/ugs_header_logo.png")

print("Fine-tuned crops completed!")
