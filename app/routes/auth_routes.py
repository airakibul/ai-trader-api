from fastapi import APIRouter, HTTPException
from app.models import TokenRequest
from app.auth import create_jwt_token

router = APIRouter()

@router.post("/auth/token")
async def login(request: TokenRequest):
    valid_users = {"demo": "password", "softvence": "omega2025", "trader": "ai123"}
    if request.username in valid_users and valid_users[request.username] == request.password:
        token = create_jwt_token(request.username)
        return {"access_token": token, "token_type": "bearer", "username": request.username}
    raise HTTPException(status_code=401, detail="Invalid credentials")
