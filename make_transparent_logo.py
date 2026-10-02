from PIL import Image

def make_transparent(input_path, output_path, bg_color=(1, 16, 27), tolerance=35):
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()
    new_data = []
    br, bg, bb = bg_color
    for item in datas:
        r, g, b, a = item
        # Calculate color distance to background
        dist = ((r - br)**2 + (g - bg)**2 + (b - bb)**2)**0.5
        if dist < tolerance:
            # smooth alpha falloff
            alpha = int(255 * (dist / tolerance)**2)
            new_data.append((r, g, b, alpha))
        else:
            new_data.append(item)
    img.putdata(new_data)
    img.save(output_path, "PNG")

make_transparent("assets/ugs_header_logo.png", "assets/ugs_logo_transparent.png", bg_color=(1, 16, 27), tolerance=30)
make_transparent("assets/ugs_footer_logo.png", "assets/ugs_footer_logo_transparent.png", bg_color=(7, 24, 35), tolerance=28)
make_transparent("assets/veriforce_logo.png", "assets/veriforce_logo_transparent.png", bg_color=(14, 29, 39), tolerance=25)
print("Created transparent logos!")
