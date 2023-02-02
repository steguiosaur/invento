from PIL import Image, ImageDraw
from pathlib import Path
import random

def generate_box_image(username):
    size = (128, 128)
    box_size = size[0] // 8
    white = (255, 255, 255)
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    image = Image.new("RGB", size, white)
    draw = ImageDraw.Draw(image)

    for i in range(4):
        for j in range(8):
            if random.choice([True, False]):
                color = random_color
            else:
                color = white
            x1 = i * box_size
            y1 = j * box_size
            x2 = (i + 1) * box_size
            y2 = (j + 1) * box_size
            draw.rectangle([x1, y1, x2, y2], fill=color)
            draw.rectangle([(size[0] - x2), y1, (size[0] - x1), y2], fill=color)

    path = Path("assets/image") / (username + ".png")
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path)
