import requests
from app.config import GROQ_API_KEY, GROQ_API_URL

def call_groq_api(messages: list, model: str = "llama3-8b-8192", max_tokens: int = 300):
    if not GROQ_API_KEY:
        return None
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    payload = {"model": model, "messages": messages, "max_tokens": max_tokens, "temperature": 0.7}
    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=30)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"Groq API Exception: {str(e)}")
    return None
