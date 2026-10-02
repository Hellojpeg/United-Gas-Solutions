from PIL import Image
import os

images = [
    "ugs_logo.png", "ugs_footer_logo.png", "veriforce_logo.png",
    "who_we_are_technician.jpg", "card_1_gas_service_operations.jpg",
    "card_8_managed_field_operations.jpg", "safety_worker.jpg",
    "tech_dispatcher.jpg", "us_map_coverage.png", "utility_partners_facility.jpg",
    "careers_team_sunset.jpg", "skyline_cta_bg.jpg", "performance_stats_bg.jpg"
]

for name in images:
    path = os.path.join("assets", name)
    if os.path.exists(path):
        im = Image.open(path)
        print(f"{name:35s}: {im.size}")
    else:
        print(f"{name:35s}: MISSING")
