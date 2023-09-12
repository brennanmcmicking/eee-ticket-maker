from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import sys

if len(sys.argv) < 2:
    n = 150
else:
    n = int(sys.argv[1])

front = Image.open("front.png").convert("RGB")
reverse = Image.open("reverse.png").convert("RGB")

font = ImageFont.truetype("font.otf", 72)

images = []

for i in range(1, n + 1):
    r = reverse.copy()
    reverse_draw = ImageDraw.Draw(r)
    reverse_draw.text((70, 425), f"#{i:03}", (0, 0, 0), font=font)
    images.append(front)
    images.append(r)

images[0].save(
    "output.pdf", "PDF", resolution=100.0, save_all=True, append_images=images[1:]
)

front.close()
reverse.close()
