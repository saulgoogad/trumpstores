from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import os

def generate_shop_image(items):
    font = ImageFont.load_default()
    cell_width, cell_height = 300, 300
    cols = 5
    rows = (len(items) + cols - 1) // cols
    width, height = cell_width * cols, cell_height * rows

    background = Image.new("RGBA", (width, height), (0, 51, 153))

    draw_bg = ImageDraw.Draw(background)
    for x in range(0, width, 200):
        for y in range(0, height, 100):
            draw_bg.text((x, y), "DONAT TRUMP", fill=(255, 255, 255, 25))

    draw = ImageDraw.Draw(background)

    for idx, item in enumerate(items):
        x = (idx % cols) * cell_width
        y = (idx // cols) * cell_height

        try:
            response = requests.get(item['image_url'])
            icon = Image.open(BytesIO(response.content)).convert("RGBA")
            icon = icon.resize((150, 150))
            background.paste(icon, (x + 75, y + 10), icon)
        except:
            continue

        draw.text((x + 10, y + 170), item['name'], font=font, fill="white")
        draw.text((x + 10, y + 200), f"{item['price']} Вбаксов", font=font, fill="white")

    output_path = "/tmp/shop_output.png"
    background.save(output_path)
    return output_path