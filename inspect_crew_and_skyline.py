from PIL import Image

src = Image.open("/Users/juanpablogomez/Downloads/United Gas Solutions Homepage.png")

# Let's inspect built_differently_crew.jpg
# (0, 1145, 360, 1315)
# In this region:
# Did it have the text "BUILT DIFFERENTLY." and the 6 cards?
# Let's check text / white pixels in (0..360, 1145..1315)
# In the original design, the 6 cards are rendered directly over the background photo of the workers and trucks!
print("Built differently in original design:")
# The title "BUILT DIFFERENTLY." is at y=1160..1180
# The 6 cards are at y=1200..1300
