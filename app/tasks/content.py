from app.providers.openrouter import call_openrouter_api
from app.providers.groq import call_groq_api
from app.providers.huggingface import call_huggingface_api

def local_content_generation(topic: str, platform: str) -> str:
    return f"Basic {platform} content about {topic}."

def perform_content_generation(topic: str, platform: str, provider: str = "auto") -> str:
    prompt = f"Write a {platform} post about {topic}."
    messages = [{"role": "system", "content": "You are a social media assistant."},
                {"role": "user", "content": prompt}]
    if provider == "openrouter":
        content = call_openrouter_api(messages)
    elif provider == "groq":
        content = call_groq_api(messages)
    elif provider == "huggingface":
        hf = call_huggingface_api("gpt2", {"inputs": prompt})
        content = hf[0].get("generated_text", "").strip() if hf else None
    else:
        content = None
    return content or local_content_generation(topic, platform)
