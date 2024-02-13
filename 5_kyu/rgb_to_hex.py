def rgb(r, g, b):
    # Clamp values to the valid range (0-255)
    r = max(0, min(255, round(r)))
    g = max(0, min(255, round(g)))
    b = max(0, min(255, round(b)))

    # Convert decimal values to hexadecimal strings with leading zeros
    hex_r = format(r, "02X")
    hex_g = format(g, "02X")
    hex_b = format(b, "02X")

    # Combine hexadecimal strings and return the complete color code
    return f"{hex_r}{hex_g}{hex_b}".upper()
