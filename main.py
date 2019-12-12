import random
import sys
from PIL import Image

assert len(sys.argv) == 3, "Please specify an input path and output path"

input_path = sys.argv[1]
output_path = sys.argv[2]

img = Image.open(input_path)
width, height = img.size

new_img = Image.new("RGB", (width, height), "white")

for i in range(width // 4, (width * 3) // 4):
    for j in range(1, height - 1):
        r, g, b = img.getpixel((i, j))
        avg = (r + g + b) // 3
        new_img.putpixel((i, j), (avg, avg, avg))

new_img.save(output_path)
