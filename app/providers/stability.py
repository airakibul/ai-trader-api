import requests
from app.config import STABILITY_API_KEY, STABILITY_API_URL

def call_stability_api(prompt: str, height: int = 512, width: int = 512):
    if not STABILITY_API_KEY:
        return None
    headers = {"Authorization": f"Bearer {STABILITY_API_KEY}", "Content-Type": "application/json"}
    payload = {"text_prompts": [{"text": prompt}], "height": height, "width": width, "steps": 30}
    try:
        response = requests.post(STABILITY_API_URL, headers=headers, json=payload, timeout=60)
        if response.status_code == 200:
            return response.content
    except Exception as e:
        print(f"Stability API Exception: {str(e)}")
    return None
