from PIL import Image

for f in ["assets/veriforce_logo.png", "assets/ugs_header_logo.png", "assets/ugs_footer_logo.png", "assets/us_map_coverage.png"]:
    im = Image.open(f)
    print(f, im.size, im.mode)
