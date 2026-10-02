from PIL import Image
import os

src = Image.open("/Users/juanpablogomez/Downloads/United Gas Solutions Homepage.png")

# Let's inspect skyline_cta_bg:
# y=1680 to 1825.
# Button is at x=250..470, y=1745..1770
# Text "THE LEADER BY DESIGN." is at y=1700..1720, x=220..500
# Text "BUILT TO PERFORM. READY TO SCALE." is at y=1725..1740, x=250..470
# What is to the left and right of the button/text?
# At x=0..220 and x=500..724, we have the illuminated night skyline, trees, and water reflections!
# We can cleanly remove the text and button by inpainting using the water texture and skyline gradient, OR we can reconstruct a seamless panoramic night skyline!

# Let's check utility_partners_facility.jpg:
# In the original design:
# The facility photo is on the right.
# Where is the button "DISCUSS A PROJECT →"?
# Let's check exact coordinates of "DISCUSS A PROJECT →"
for y in range(1390, 1435):
    for x in range(350, 480):
        r, g, b, *a = src.getpixel((x, y))
        # Button border or text is light on dark background
