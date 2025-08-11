from PIL import Image
import base64
from io import BytesIO

def img_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def generate_image_html(img, caption):
    w, h = img.size
    img_b64 = img_to_base64(img)
    html = f"""
    <div style="
        width:{w}px;
        height:{h}px;
        overflow:auto;
        border: 2px solid #4CAF50;
        margin-bottom: 10px;
        ">
        <img src="data:image/png;base64,{img_b64}" width="{w}" height="{h}"/>
    </div>
    <div style="font-weight:bold; margin-bottom:20px;">{caption} ({w}×{h} px)</div>
    """
    return html

# Load original image
original_image = Image.open("path/to/original.jpg")
# Resize image
resized_image = original_image.resize((390, 510))  # example size

# Generate HTML snippets
original_html = generate_image_html(original_image, "Original")
resized_html = generate_image_html(resized_image, "Resized")

# Combine for full HTML page (optional)
full_html = f"""
<html>
<head><title>Image Preview</title></head>
<body>
<h2>Original vs Resized Images</h2>
<div style="display:flex; gap:20px;">
<div>{original_html}</div>
<div>{resized_html}</div>
</div>
</body>
</html>
"""

# Save to file or output
with open("image_preview.html", "w") as f:
    f.write(full_html)

print("HTML preview saved to image_preview.html")
