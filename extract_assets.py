from PIL import Image

src = "/Users/juanpablogomez/Downloads/United Gas Solutions Homepage.png"
img = Image.open(src)
w, h = img.size

# Let's write precision extraction functions
# 1. Logo from header
# Let's crop header logo around x=20..130, y=5..30
logo = img.crop((20, 5, 135, 33))
logo.save("assets/ugs_logo.png")

# 2. Hero background/worker
# Hero section is roughly y=0 to y=308. Full width.
hero = img.crop((0, 0, w, 308))
hero.save("assets/hero_banner.jpg", quality=95)

# Hero worker detail crop (just in case)
hero_worker = img.crop((320, 50, 570, 300))
hero_worker.save("assets/hero_worker.jpg", quality=95)

# 3. Who We Are - Technician working on gas meters
# In y=355 to 575. Left photo is roughly x=20..350, y=365..565
who_we_are_worker = img.crop((0, 355, 350, 575))
who_we_are_worker.save("assets/who_we_are_technician.jpg", quality=95)

# 4. The 8 services cards
# Services section is y=620 to 745
# There are 8 cards across width 724.
# Card width is around 80-85px, with gaps.
# Let's crop the full services band first, and individual cards
services_band = img.crop((0, 615, w, 750))
services_band.save("assets/services_band.jpg", quality=95)

# Let's check card boundaries:
# Margin left ~15px, card width ~82px, gap ~5px:
# 15 + 8*(82+5) ~ 711
card_y1 = 620
card_y2 = 745
card_w = 82
card_gap = 5
start_x = 15

service_names = [
    "gas_service_operations",
    "meter_services",
    "turn_ons_reconnects",
    "disconnect_shutoff",
    "meter_renewals",
    "field_inspections",
    "utility_workforce_support",
    "managed_field_operations"
]

# We can crop the photo area of each card (excluding the text label or including it)
for i, name in enumerate(service_names):
    # let's crop just the photo (top of card)
    cx1 = int(15 + i * 87.2)
    cx2 = int(cx1 + 83)
    card_full = img.crop((cx1, card_y1, cx2, card_y2))
    card_full.save(f"assets/card_{i+1}_{name}.jpg", quality=95)
    # also just the photo part (card_y1 to card_y1 + 95)
    card_photo = img.crop((cx1, card_y1, cx2, card_y1 + 92))
    card_photo.save(f"assets/service_{i+1}_{name}_photo.jpg", quality=95)

# 5. Safety & Compliance Section
# y=755 to 975
safety_bg = img.crop((0, 755, w, 975))
safety_bg.save("assets/safety_section.jpg", quality=95)

# Safety worker crop
safety_worker = img.crop((260, 755, 520, 975))
safety_worker.save("assets/safety_worker.jpg", quality=95)

# Veriforce logo crop
veriforce_logo = img.crop((545, 765, 660, 805))
veriforce_logo.save("assets/veriforce_logo.png")

# 6. Technology-Powered Operations
# y=975 to 1145
tech_bg = img.crop((0, 975, w, 1145))
tech_bg.save("assets/tech_operations_bg.jpg", quality=95)

# Center dispatcher photo
tech_dispatcher = img.crop((230, 980, 580, 1145))
tech_dispatcher.save("assets/tech_dispatcher.jpg", quality=95)

# 7. Built Differently & Map
# y=1145 to 1315
built_diff_bg = img.crop((0, 1145, 360, 1315))
built_diff_bg.save("assets/built_differently_crew.jpg", quality=95)

us_map = img.crop((520, 1150, 715, 1290))
us_map.save("assets/us_map_coverage.png")

# 8. Utility & Infrastructure Partners
# y=1315 to 1465
partners_facility = img.crop((570, 1320, 724, 1465))
partners_facility.save("assets/utility_partners_facility.jpg", quality=95)

# 9. Performance stats background
perf_bg = img.crop((0, 1465, w, 1545))
perf_bg.save("assets/performance_stats_bg.jpg", quality=95)

# 10. Careers Section
# y=1545 to 1680
careers_team = img.crop((300, 1545, w, 1680))
careers_team.save("assets/careers_team_sunset.jpg", quality=95)

# 11. Pre-footer Skyline Banner
# y=1680 to 1825
skyline_cta = img.crop((0, 1680, w, 1825))
skyline_cta.save("assets/skyline_cta_bg.jpg", quality=95)

# 12. Footer logo
footer_logo = img.crop((25, 1870, 135, 1945))
footer_logo.save("assets/ugs_footer_logo.png")

print("All base assets cropped! Verifying files...")
