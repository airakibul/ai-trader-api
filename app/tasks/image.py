import base64, io
from PIL import Image, ImageDraw
from app.providers.stability import call_stability_api
from app.providers.huggingface import call_huggingface_api

def local_image_generation(prompt: str) -> str:
    img = Image.new("RGB", (256,256), color="black")
    draw = ImageDraw.Draw(img)
    draw.text((10,120), prompt[:20], fill="white")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()

def perform_image_generation(prompt: str, provider: str = "auto") -> str:
    if provider == "stability":
        img = call_stability_api(prompt)
        if img: return "data:image/png;base64," + base64.b64encode(img).decode()
    elif provider == "huggingface":
        hf = call_huggingface_api("runwayml/stable-diffusion-v1-5", {"inputs": prompt})
        if hf and "binary_data" in hf:
            return "data:image/png;base64," + base64.b64encode(hf["binary_data"]).decode()
    return local_image_generation(prompt)
