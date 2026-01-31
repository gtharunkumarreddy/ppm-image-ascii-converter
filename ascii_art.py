ASCII_CHARS = "@%#*+=-:. "

def read_ppm_p3(filename):
    tokens = []

    # Read file and ignore comments
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("#") or line == "":
                continue
            tokens.extend(line.split())

    # Check format
    if tokens[0] != "P3":
        raise ValueError("Not a P3 ASCII PPM file")

    width = int(tokens[1])
    height = int(tokens[2])
    max_val = int(tokens[3])  # usually 255

    pixel_data = list(map(int, tokens[4:]))

    image = []
    idx = 0
    for _ in range(height):
        row = []
        for _ in range(width):
            r = pixel_data[idx]
            g = pixel_data[idx + 1]
            b = pixel_data[idx + 2]
            idx += 3

            gray = (r + g + b) // 3
            row.append(gray)
        image.append(row)

    return image


def to_ascii(image):
    ascii_img = []
    scale = len(ASCII_CHARS) - 1

    for row in image:
        line = ""
        for px in row:
            line += ASCII_CHARS[px * scale // 255]
        ascii_img.append(line)

    return ascii_img


# -------- MAIN --------
image = read_ppm_p3("face.ppm")
ascii_image = to_ascii(image)

with open("ascii_output.txt", "w") as f:
    for line in ascii_image:
        f.write(line + "\n")

print("ASCII art created: ascii_output.txt")
