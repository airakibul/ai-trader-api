import requests, time, json
from app.config import HUGGINGFACE_TOKEN, HUGGINGFACE_API_URL

def call_huggingface_api(model_name: str, payload: dict, timeout: int = 30):
    if not HUGGINGFACE_TOKEN:
        return None
    headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}", "Content-Type": "application/json"}
    url = f"{HUGGINGFACE_API_URL}/{model_name}"
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=timeout)
        if response.status_code == 200:
            try:
                return response.json()
            except json.JSONDecodeError:
                return {"binary_data": response.content}
        elif response.status_code == 503:
            wait_time = response.json().get('estimated_time', 20)
            time.sleep(min(wait_time, 30))
            return call_huggingface_api(model_name, payload, timeout)
    except Exception as e:
        print(f"HuggingFace API Exception: {str(e)}")
    return None
