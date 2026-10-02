from PIL import Image

src_path = "/Users/juanpablogomez/Downloads/United Gas Solutions Homepage.png"
img = Image.open(src_path)
w, h = img.size
print(f"Source image size: {w}x{h}")

# Let's inspect vertical divisions
# We can save crops for all key visual assets:
# 1. Hero background & worker
# 2. Who We Are technician working on gas pipes
# 3. 8 Service photos
# 4. Safety & Compliance worker with UGS back
# 5. Technology Dispatch room / screens & dispatcher
# 6. Built Differently worker/fleet background
# 7. US Map graphic with South Florida highlighted
# 8. Utility & Infrastructure facility sunset + worker
# 9. Performance stats background
# 10. Careers 4 workers walking towards fleet
# 11. Pre-footer South Florida skyline at night
# 12. UGS Logos (Header, Footer)
# 13. Veriforce Logo

