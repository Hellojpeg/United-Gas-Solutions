from PIL import Image

logo = Image.open("assets/ugs_logo.png")
print("Logo size:", logo.size, logo.mode)
# Look at corner pixel color
print("Top left pixel:", logo.getpixel((0, 0)))

# Let's inspect footer logo
footer_logo = Image.open("assets/ugs_footer_logo.png")
print("Footer logo size:", footer_logo.size, footer_logo.mode)
print("Footer logo top left:", footer_logo.getpixel((0, 0)))
