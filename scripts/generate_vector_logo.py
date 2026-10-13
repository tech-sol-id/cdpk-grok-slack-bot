import os
import math
from PIL import Image, ImageDraw, ImageFilter

def create_grok_slack_logo(output_path_1024="assets/grok_slack_logo_1024.png", output_path_512="assets/grok_slack_logo_512.png"):
    os.makedirs("assets", exist_ok=True)
    width, height = 1024, 1024
    
    # High resolution canvas
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 1. Background: Deep obsidian rounded app icon container
    # Slack dark theme bg is #1A1D21
    bg_box = [32, 32, width - 32, height - 32]
    corner_radius = 210
    draw.rounded_rectangle(bg_box, radius=corner_radius, fill=(22, 25, 34, 255))
    
    # Subtle border highlight
    draw.rounded_rectangle(bg_box, radius=corner_radius, outline=(255, 255, 255, 30), width=4)
    
    # 2. Slack 4 Colors
    colors = {
        "blue": (54, 197, 240, 255),    # #36C5F0
        "green": (46, 182, 125, 255),   # #2EB67D
        "yellow": (236, 178, 46, 255),  # #ECB22E
        "red": (224, 30, 90, 255)       # #E01E5A
    }
    
    # We will create an overlay layer with antialiasing
    scale = 2
    sw, sh = width * scale, height * scale
    super_img = Image.new("RGBA", (sw, sh), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(super_img)
    
    cx, cy = sw // 2, sh // 2
    outer_r = 340 * scale
    inner_r = 240 * scale
    thickness = outer_r - inner_r
    
    # 4 Arcs representing Slack colors mapped onto Grok orbital ring
    # Top: Blue, Right: Green, Bottom: Yellow, Left: Red
    # With angled separation matching Grok slash angle (~ -45 deg / 135 deg)
    
    arc_segments = [
        ("blue", 140, 220),    # Top-Left to Top
        ("green", 230, 310),   # Top to Right
        ("yellow", 320, 40),   # Bottom-Right to Bottom
        ("red", 50, 130),      # Bottom to Left
    ]
    
    for cname, start_deg, end_deg in arc_segments:
        col = colors[cname]
        # Draw thick arc
        bbox = [cx - outer_r, cy - outer_r, cx + outer_r, cy + outer_r]
        sdraw.arc(bbox, start=start_deg, end=end_deg, fill=col, width=int(thickness))
        
        # Rounded caps at ends of arcs (Slack style pills)
        for deg in [start_deg, end_deg]:
            rad = math.radians(deg)
            cap_r = (outer_r + inner_r) / 2
            cap_x = cx + cap_r * math.cos(rad)
            cap_y = cy + cap_r * math.sin(rad)
            dot_r = thickness / 2
            sdraw.ellipse([cap_x - dot_r, cap_y - dot_r, cap_x + dot_r, cap_y + dot_r], fill=col)
            
    # 3. Grok central futuristic slash (diagonal beam from bottom-left to top-right)
    # The slash extends beyond the ring with tapered spear ends
    slash_color = (255, 255, 255, 255)
    
    # Polygon points for the dynamic slash
    slash_points = [
        (cx - 380 * scale, cy + 340 * scale),  # bottom left tip
        (cx - 50 * scale, cy + 30 * scale),    # center left
        (cx + 420 * scale, cy - 380 * scale),  # top right tip
        (cx + 80 * scale, cy - 40 * scale),    # center right
    ]
    sdraw.polygon(slash_points, fill=slash_color)
    
    # Inner glow / gradient around the slash
    slash_glow = [
        (cx - 200 * scale, cy + 180 * scale),
        (cx + 240 * scale, cy - 220 * scale),
    ]
    
    # Downsample for crisp anti-aliasing
    super_img = super_img.resize((width, height), Image.Resampling.LANCZOS)
    img.alpha_composite(super_img)
    
    # Save 1024x1024
    img.save(output_path_1024, "PNG")
    print(f"Saved: {output_path_1024}")
    
    # Save 512x512 (ideal for Slack App Icon upload)
    img_512 = img.resize((512, 512), Image.Resampling.LANCZOS)
    img_512.save(output_path_512, "PNG")
    print(f"Saved: {output_path_512}")

if __name__ == "__main__":
    create_grok_slack_logo()
