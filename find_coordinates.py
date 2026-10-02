from PIL import Image
import numpy as np

img = Image.open("/Users/juanpablogomez/Downloads/United Gas Solutions Homepage.png")
w, h = img.size

# Let's crop test slices at reasonable estimations and verify them
# Header: 0 to ~60
# Hero: 0 to ~300
# Trust bar: ~295 to ~350
# Who We Are: ~350 to ~570
# Services: ~570 to ~750
# Safety & Compliance: ~750 to ~970
# Tech Ops: ~970 to ~1150
# Built Differently & Map: ~1150 to ~1320
# Utility Partners: ~1320 to ~1460
# Performance stats: ~1460 to ~1540
# Careers: ~1540 to ~1680
# Pre-footer CTA: ~1680 to ~1820
# Footer: ~1820 to 2172

print("Analyzing image landmarks...")
