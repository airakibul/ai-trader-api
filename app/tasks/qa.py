import datetime
from app.providers.openrouter import call_openrouter_api
from app.providers.groq import call_groq_api
from app.providers.huggingface import call_huggingface_api

latest_answers = []

def local_qa_response(question: str) -> str:
    q = question.lower()
    responses = {
        "trading": "Algorithmic trading uses computer programs...",
        "ai": "AI in trading uses machine learning...",
        "risk": "Risk management involves position sizing...",
        "market": "Financial markets are influenced by...",
        "strategy": "Successful trading strategies combine..."
    }
    for k,v in responses.items():
        if k in q: return v
    return f"Regarding '{question}': This topic involves multiple factors in algorithmic trading."

def perform_qa(query: str, provider: str = "auto") -> str:
    messages = [{"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": query}]
    if provider == "openrouter":
        answer = call_openrouter_api(messages)
    elif provider == "groq":
        answer = call_groq_api(messages)
    elif provider == "huggingface":
        hf = call_huggingface_api("microsoft/DialoGPT-medium", {"inputs": query})
        answer = hf[0].get("generated_text", "").replace(query, "").strip() if hf else None
    else:
        answer = None
    result = answer or local_qa_response(query)
    latest_answers.append({"query": query, "answer": result, "timestamp": datetime.datetime.utcnow().isoformat()})
    if len(latest_answers) > 10: latest_answers.pop(0)
    return result
