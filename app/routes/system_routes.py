from fastapi import APIRouter
from app.config import OPENROUTER_API_KEY, GROQ_API_KEY, HUGGINGFACE_TOKEN, STABILITY_API_KEY
import datetime
from app.tasks.qa import latest_answers

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "AI Trader API v4.0", "status": "running"}

@router.get("/providers")
async def list_providers():
    return {
        "openrouter": bool(OPENROUTER_API_KEY),
        "groq": bool(GROQ_API_KEY),
        "huggingface": bool(HUGGINGFACE_TOKEN),
        "stability": bool(STABILITY_API_KEY),
        "local": True
    }

@router.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.datetime.utcnow().isoformat(), "latest_answers_count": len(latest_answers)}
