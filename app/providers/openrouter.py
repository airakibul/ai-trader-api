import requests
from app.config import OPENROUTER_API_KEY, OPENROUTER_API_URL

def call_openrouter_api(messages: list, model: str = "openai/gpt-3.5-turbo", max_tokens: int = 300):
    if not OPENROUTER_API_KEY:
        return None
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://softvence-omega-ai-trader.com",
        "X-Title": "AI Trader API"
    }
    payload = {"model": model, "messages": messages, "max_tokens": max_tokens, "temperature": 0.7}
    try:
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload, timeout=30)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"OpenRouter API Exception: {str(e)}")
    return None
