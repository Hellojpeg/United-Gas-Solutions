from PIL import Image

src = Image.open("/Users/juanpablogomez/Downloads/United Gas Solutions Homepage.png")

# 1. Look at utility_partners_facility.jpg:
# In the original image:
# y=1320..1465.
# At x=365..470, y=1400..1425 is the button "DISCUSS A PROJECT →"
# But utility facility was cropped at (570, 1320, 724, 1465).
# Wait, did it touch the button or worker? In utility facility, x starts at 570, but the worker is at x=575..670!
# At x=365..470, "DISCUSS A PROJECT" is outside (570..724). BUT in our HTML, the button was coded on the left, and maybe on desktop it overlapped or looked different!

# 2. Look at skyline_cta_bg.jpg:
# y=1680 to 1825.
# IN THE ORIGINAL IMAGE:
# The text "THE LEADER BY DESIGN." is at y=1700
# "BUILT TO PERFORM. READY TO SCALE." is at y=1725
# The button "PARTNER WITH UNITED GAS SOLUTIONS →" is at y=1750..1780!
# AND IN OUR HTML, WE HAD HTML TEXT AND HTML BUTTON OVERLAYED ON TOP OF THE IMAGE THAT ALREADY HAD THE TEXT AND BUTTON BURNED IN!
print("Skyline image definitely has the burned text and button!")

# 3. Look at hero_visual.jpg:
# x=260 to 724, y=0 to 308.
# At x=260, does it catch the edge of "PEOPLE. SAFETY. TECHNOLOGY"?
# At y=100..150, does it catch the edge of "THE LEADER BY DESIGN"?
# Let's inspect x=260 in hero

# 4. Look at safety_worker.jpg:
# (260, 755, 545, 975)
# In safety section, does it catch "OUR SAFETY STANDARDS →" or Veriforce text?
# The button "OUR SAFETY STANDARDS →" is at x=25..170, y=920..945.
# So x=260..545 avoids that button. BUT did it have any other text?

# 5. Look at tech_dispatcher.jpg:
# (240, 975, 595, 1145)
# The button "THE UGS ADVANTAGE →" is at x=25..160, y=1095..1120.
# So x=240 avoids that.

# 6. Look at careers_team_sunset.jpg:
# (295, 1545, w, 1680)
# Button "EXPLORE CAREERS →" is at x=25..155, y=1640..1665.

