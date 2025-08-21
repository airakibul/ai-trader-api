from fastapi import APIRouter, Depends, HTTPException
from app.models import AITaskRequest
from app.auth import verify_jwt_token
from app.tasks.qa import perform_qa, latest_answers
from app.tasks.content import perform_content_generation
from app.tasks.image import perform_image_generation
import datetime

router = APIRouter()

@router.post("/ai-task")
async def handle_ai_task(request: AITaskRequest, user: str = Depends(verify_jwt_token)):
    if request.task == "qa":
        if not request.query: raise HTTPException(400, "Query required")
        answer = perform_qa(request.query, request.provider)
        return {"task": "qa", "query": request.query, "answer": answer, "user": user}
    elif request.task == "content_generation":
        if not request.topic or not request.platform: raise HTTPException(400, "Topic/platform required")
        return {"task": "content_generation", "content": perform_content_generation(request.topic, request.platform, request.provider)}
    elif request.task == "image_generation":
        if not request.prompt: raise HTTPException(400, "Prompt required")
        return {"task": "image_generation", "image_url": perform_image_generation(request.prompt, request.provider)}
    elif request.task == "latest_answer":
        return {"latest": latest_answers[-1] if latest_answers else None}
    raise HTTPException(400, "Invalid task")
