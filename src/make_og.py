"""Generates assets/img/og.png (social share image)."""
import glob, os
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def font(name, size):
    f = glob.glob(f"/usr/share/fonts/**/{name}", recursive=True)
    return ImageFont.truetype(f[0], size) if f else ImageFont.load_default()
W, H = 1200, 630
im = Image.new("RGB", (W, H), "#447766"); d = ImageDraw.Draw(im)
big, sm, xs = font("DejaVuSansMono-Bold.ttf", 150), font("DejaVuSans-Bold.ttf", 46), font("DejaVuSans-Bold.ttf", 30)
d.rectangle([0, 0, W, 14], fill="#C8102E")
x = 110
for ch in "447766":
    col = "#9fb8ae" if ch == "4" else ("#ffffff" if ch == "7" else "#D4A017")
    d.rounded_rectangle([x, 150, x + 150, 350], radius=22, fill="#2f5a4c")
    d.text((x + 75, 250), ch, font=big, fill=col, anchor="mm"); x += 170
d.text((W // 2, 430), "The Lucky Number Lab", font=sm, fill="#ffffff", anchor="mm")
d.text((W // 2, 500), "Chinese meanings · luck scores · angel numbers — decode any number", font=xs, fill="#dbe9e3", anchor="mm")
os.makedirs(os.path.join(ROOT, "assets/img"), exist_ok=True)
im.save(os.path.join(ROOT, "assets/img/og.png"), optimize=True)
