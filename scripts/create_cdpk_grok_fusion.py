import math
from PIL import Image, ImageDraw, ImageFilter, ImageOps

def create_fusion():
    width, height = 1024, 1024
    scale = 2
    sw, sh = width * scale, height * scale
    
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 1. Dark squircle container
    bg_box = [32, 32, width - 32, height - 32]
    corner_radius = 210
    # Rich deep obsidian dark gradient
    draw.rounded_rectangle(bg_box, radius=corner_radius, fill=(15, 17, 23, 255))
    # Subtle inner border
    draw.rounded_rectangle(bg_box, radius=corner_radius, outline=(255, 255, 255, 25), width=4)

    # 2. Load and process CP mark
    cp_raw = Image.open("assets/cdpk_cp_mark.png").convert("RGBA")
    
    # Crop tightly to non-transparent pixels
    bbox = cp_raw.getbbox()
    if bbox:
        cp_raw = cp_raw.crop(bbox)
        
    # Scale CP mark nicely into center
    target_dim = 620
    ratio = min(target_dim / cp_raw.width, target_dim / cp_raw.height)
    new_size = (int(cp_raw.width * ratio), int(cp_raw.height * ratio))
    cp_resized = cp_raw.resize(new_size, Image.Resampling.LANCZOS)
    
    # Position CP mark
    pos_x = (width - cp_resized.width) // 2
    pos_y = (height - cp_resized.height) // 2 - 10
    
    # Composite CP mark
    img.paste(cp_resized, (pos_x, pos_y), cp_resized)
    
    # 3. Add Grok signature dynamic diagonal slash cutting through
    # Super-sampled slash layer
    slash_img = Image.new("RGBA", (sw, sh), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(slash_img)
    
    cx, cy = sw // 2, sh // 2
    
    # Diagonal beam with sharp spear tips
    # White with subtle glow
    slash_poly = [
        (cx - 390 * scale, cy + 340 * scale),  # bottom left tip
        (cx - 55 * scale, cy + 25 * scale),    # waist left
        (cx + 420 * scale, cy - 380 * scale),  # top right tip
        (cx + 70 * scale, cy - 35 * scale),    # waist right
    ]
    sdraw.polygon(slash_poly, fill=(255, 255, 255, 255))
    
    # Inner dynamic cut in the slash (xAI Grok style)
    cut_poly = [
        (cx - 150 * scale, cy + 130 * scale),
        (cx - 20 * scale, cy + 10 * scale),
        (cx + 170 * scale, cy - 150 * scale),
        (cx + 30 * scale, cy - 20 * scale),
    ]
    sdraw.polygon(cut_poly, fill=(15, 17, 23, 230))
    
    slash_img = slash_img.resize((width, height), Image.Resampling.LANCZOS)
    img = Image.alpha_composite(img, slash_img)
    
    # Save 1024 and 512
    img.save("assets/cdpk_grok_logo_vector_1024.png", "PNG")
    img_512 = img.resize((512, 512), Image.Resampling.LANCZOS)
    img_512.save("assets/cdpk_grok_logo_vector_512.png", "PNG")
    print("Vector fusion saved successfully!")

if __name__ == "__main__":
    create_fusion()
