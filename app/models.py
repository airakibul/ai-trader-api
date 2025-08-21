from pydantic import BaseModel
from typing import Optional

class AITaskRequest(BaseModel):
    task: str
    query: Optional[str] = None
    prompt: Optional[str] = None
    platform: Optional[str] = None
    topic: Optional[str] = None
    provider: Optional[str] = "auto"

class TokenRequest(BaseModel):
    username: str
    password: str
