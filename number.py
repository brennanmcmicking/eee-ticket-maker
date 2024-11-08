from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import sys

if len(sys.argv) < 2:
    n = 150
else:
    n = int(sys.argv[1])

front = Image.open("front.png").convert("RGB")
reverse = Image.open("reverse.png").convert("RGBA")

font = ImageFont.truetype("DMSerifDisplay-Regular.ttf", 72)

images = []

for i in range(1, n + 1):
    print(i)
    reverse_text = Image.new("RGBA", reverse.size, (255, 255, 255, 0))

    reverse_draw = ImageDraw.Draw(reverse_text)
    reverse_draw.text((80, 435), f"#{i:03}", (163, 67, 104, 50), font=font)
    reverse_draw.text((75, 430), f"#{i:03}", (163, 67, 104, 100), font=font)
    reverse_draw.text((70, 425), f"#{i:03}", (255, 255, 255), font=font)

    r = Image.alpha_composite(reverse, reverse_text).convert("RGB")

    images.append(front)
    images.append(r)

print("saving pdf")
images[0].save(
    "output.pdf", "PDF", resolution=100.0, save_all=True, append_images=images[1:]
)
print("done saving pdf")

front.close()
reverse.close()

print("done everything")