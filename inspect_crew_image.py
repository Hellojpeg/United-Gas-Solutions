from PIL import Image

im = Image.open("assets/built_differently_crew.jpg")
print("built_differently_crew size:", im.size)
# Sample points where tiles would be
# Tile 1 is around (60, 80)
print("Pixel at 60,80:", im.getpixel((60, 80)))
print("Pixel at 180,80:", im.getpixel((180, 80)))
