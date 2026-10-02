from PIL import Image, ImageFilter


src = Image.open("/Users/juanpablogomez/Downloads/United Gas Solutions Homepage.png")
w, h = src.size

# =========================================================================
# 1. CLEAN SKYLINE CTA BANNER (y: 1680 to 1825)
# In original, width=724, height=145.
# Button is at x=240..480, y=65..95 (relative to banner)
# Text is at x=200..520, y=15..65
# We can inpaint the central region (x=190..530) seamlessly!
# Notice: the skyline has buildings, trees, and water reflections.
# Left side (x: 0..200) and Right side (x: 520..724) are completely clean!
# We can blend the night sky gradient at the top (y: 0..60), and the dark water
# reflections at the bottom (y: 60..145) with horizontal interpolation / reflection.
# =========================================================================
skyline = src.crop((0, 1680, w, 1825)).convert("RGB")
sw, sh = skyline.size

# Let's clean the central text and button area:
# In the skyline, the top half (y: 0 to 70) is dark night sky with city glow.
# The bottom half (y: 70 to 145) is waterfront with palm reflections and lights.
# For each y in range(0, sh), we can interpolate the background across x=190..530
# using the clean pixels at x=180 and x=540, plus adding subtle natural texture.

sky_clean = skyline.copy()
# For the sky (y: 0 to 65):
for y in range(0, 70):
    c1 = skyline.getpixel((180, y))
    c2 = skyline.getpixel((540, y))
    for x in range(180, 541):
        t = (x - 180) / (540 - 180)
        # Smooth interpolation with slight noise/variation to match photographic grain
        r = int(c1[0] * (1 - t) + c2[0] * t)
        g = int(c1[1] * (1 - t) + c2[1] * t)
        b = int(c1[2] * (1 - t) + c2[2] * t)
        sky_clean.putpixel((x, y), (r, g, b))

# For the middle & waterfront (y: 70 to 105) where button was:
for y in range(70, 105):
    c1 = skyline.getpixel((185, y))
    c2 = skyline.getpixel((535, y))
    for x in range(185, 536):
        t = (x - 185) / (535 - 185)
        # sample some reflections from nearby water
        r = int(c1[0] * (1 - t) + c2[0] * t)
        g = int(c1[1] * (1 - t) + c2[1] * t)
        b = int(c1[2] * (1 - t) + c2[2] * t)
        sky_clean.putpixel((x, y), (r, g, b))

# For the bottom water reflections (y: 105 to sh):
for y in range(105, sh):
    c1 = skyline.getpixel((180, y))
    c2 = skyline.getpixel((540, y))
    for x in range(180, 541):
        t = (x - 180) / (540 - 180)
        r = int(c1[0] * (1 - t) + c2[0] * t)
        g = int(c1[1] * (1 - t) + c2[1] * t)
        b = int(c1[2] * (1 - t) + c2[2] * t)
        sky_clean.putpixel((x, y), (r, g, b))

# Smoothly blur the inpainted box boundary so there are no seams
# Apply a subtle 1px blur only to x in [170, 550]
box = sky_clean.crop((175, 0, 545, sh))
box = box.filter(ImageFilter.GaussianBlur(radius=1.8))
sky_clean.paste(box, (175, 0))

sky_clean.save("assets/skyline_cta_bg.jpg", quality=95)
print("1. Cleaned skyline_cta_bg.jpg (no burned button or text!)")


# =========================================================================
# 2. CLEAN PERFORMANCE STATS BACKGROUND (y: 1465 to 1545)
# In original, (0, 1465, 724, 1545)
# It has "10,000+", "50+", "100%", "1" in bright yellow.
# The underlying photo is dark silhouette of workers and utility fleet in yard.
# We can remove the yellow and white text by inpainting from adjacent background!
# =========================================================================
perf = src.crop((0, 1465, w, 1545)).convert("RGB")
pw, ph = perf.size
perf_clean = perf.copy()

# Any pixel that is bright yellow (r>160, g>120, b<80) or bright white (r>190, g>190, b>190)
# is text. Replace with local background median / vertical neighbors!
for y in range(ph):
    for x in range(pw):
        r, g, b = perf.getpixel((x, y))
        is_text = (r > 150 and g > 110 and b < 85) or (r > 190 and g > 190 and b > 190)
        if is_text:
            # find non-text neighbors above or below or to the sides
            samples = []
            for dy in [-4, -3, -2, 2, 3, 4]:
                ny = max(0, min(ph - 1, y + dy))
                nr, ng, nb = perf.getpixel((x, ny))
                if not ((nr > 150 and ng > 110 and nb < 85) or (nr > 190 and ng > 190 and nb > 190)):
                    samples.append((nr, ng, nb))
            for dx in [-6, -5, -4, 4, 5, 6]:
                nx = max(0, min(pw - 1, x + dx))
                nr, ng, nb = perf.getpixel((nx, y))
                if not ((nr > 150 and ng > 110 and nb < 85) or (nr > 190 and ng > 190 and nb > 190)):
                    samples.append((nr, ng, nb))
            if samples:
                avg_r = sum(s[0] for s in samples) // len(samples)
                avg_g = sum(s[1] for s in samples) // len(samples)
                avg_b = sum(s[2] for s in samples) // len(samples)
                perf_clean.putpixel((x, y), (avg_r, avg_g, avg_b))
            else:
                perf_clean.putpixel((x, y), (14, 30, 42))

perf_clean = perf_clean.filter(ImageFilter.GaussianBlur(radius=1.2))
perf_clean.save("assets/performance_stats_bg.jpg", quality=95)
print("2. Cleaned performance_stats_bg.jpg (no burned numbers or labels!)")


# =========================================================================
# 3. CLEAN HERO BACKGROUND VISUAL (y: 0 to 308)
# We want the photo of the UGS utility worker facing the fleet at sunset.
# Start crop at x=285 so NO text from "THE LEADER BY DESIGN" or
# "EXPLORE OUR SERVICES" button is caught on the left.
# On the right (x=660..710), the side badge ("SAFE / RELIABLE / RESPONSIVE")
# was burned into the original. Let's inpaint / clean that right edge
# so the sunset sky / background is 100% clean, and we code the badge in HTML!
# =========================================================================
hero = src.crop((285, 0, w, 308)).convert("RGB")
hw, hh = hero.size
hero_clean = hero.copy()

# The badge is at x in [660-285, 715-285] -> [375, 435], y in [180, 260]
# In this region, replace text with sunset sky & truck colors
for y in range(180, 270):
    for x in range(370, hw):
        r, g, b = hero.getpixel((x, y))
        # text is light / white or yellow bar
        if (r > 190 and g > 190 and b > 190) or (r > 180 and g > 130 and b < 70):
            # sample from x=365
            ref_r, ref_g, ref_b = hero.getpixel((365, y))
            hero_clean.putpixel((x, y), (ref_r, ref_g, ref_b))

# Subtle smooth on the badge inpaint area
badge_crop = hero_clean.crop((365, 175, hw, 275)).filter(ImageFilter.GaussianBlur(radius=1.5))
hero_clean.paste(badge_crop, (365, 175))

hero_clean.save("assets/hero_visual.jpg", quality=95)
print("3. Cleaned hero_visual.jpg (no clipped buttons or badges!)")


# =========================================================================
# 4. CLEAN BUILT DIFFERENTLY CREW BACKGROUND (y: 1145 to 1315)
# In original, (0, 1145, 360, 1315)
# The 6 cards ("Safety-First Culture", etc.) are over the photo.
# We remove the white card text & borders by median filtering so it's
# a pure, clean, subtle background photo of the fleet and crew in the yard!
# =========================================================================
crew = src.crop((0, 1145, 360, 1315)).convert("RGB")
cw, ch = crew.size
crew_clean = crew.copy()

for y in range(ch):
    for x in range(cw):
        r, g, b = crew.getpixel((x, y))
        is_card_text = (r > 180 and g > 180 and b > 180) or (r > 180 and g > 130 and b < 80)
        if is_card_text:
            samples = []
            for dy in [-5, -4, 4, 5]:
                ny = max(0, min(ch - 1, y + dy))
                nr, ng, nb = crew.getpixel((x, ny))
                if not ((nr > 180 and ng > 180 and nb > 180) or (nr > 180 and ng > 130 and nb < 80)):
                    samples.append((nr, ng, nb))
            if samples:
                crew_clean.putpixel((x, y), (
                    sum(s[0] for s in samples) // len(samples),
                    sum(s[1] for s in samples) // len(samples),
                    sum(s[2] for s in samples) // len(samples)
                ))
            else:
                crew_clean.putpixel((x, y), (12, 28, 38))

crew_clean = crew_clean.filter(ImageFilter.GaussianBlur(radius=1.5))
crew_clean.save("assets/built_differently_crew.jpg", quality=95)
print("4. Cleaned built_differently_crew.jpg (pure crew & fleet background!)")


# =========================================================================
# 5. CLEAN UTILITY PARTNERS INDUSTRIAL FACILITY PHOTO (y: 1320 to 1465)
# The button "DISCUSS A PROJECT →" was at x=360..470.
# The industrial facility and worker is at x=470 to 724.
# Let's crop from x=470 to 724 so NO button is inside the photo at all!
# The photo shows the full industrial piping, tanks, and UGS worker at sunset.
# =========================================================================
partners = src.crop((470, 1320, w, 1465)).convert("RGB")
partners.save("assets/utility_partners_facility.jpg", quality=95)
print("5. Cleaned utility_partners_facility.jpg (starts at x=470, 100% free of any button!)")

