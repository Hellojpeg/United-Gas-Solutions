from PIL import Image

for i, name in enumerate([
    "gas_service_operations", "meter_services", "turn_ons_reconnects",
    "disconnect_shutoff", "meter_renewals", "field_inspections",
    "utility_workforce_support", "managed_field_operations"
]):
    im = Image.open(f"assets/service_{name}.jpg")
    print(f"service_{name}: {im.size}")
    # Check bottom 10 rows for black or text
    bottom_r = [im.getpixel((im.width//2, y))[0] for y in range(im.height - 10, im.height)]
    print(f"  bottom rows r-vals: {bottom_r}")

