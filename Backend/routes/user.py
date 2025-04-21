# Backend/routes/user.py
from fastapi import APIRouter
from controllers.user_controller import get_user_by_id, add_user
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    email: str
    password_hash: str

class UserResponse(BaseModel):
    username: str
    email: str
    password_hash: str
    created_at: datetime

@router.get("/user/{user_id}")
def read_user(user_id: int):
    return get_user_by_id(user_id)

@router.post("/user", response_model=UserResponse)
async def create_user(user: UserCreate):
    try:
        # Convert Pydantic model to dict and add timestamp
        user_data = user.dict()
        user_data["created_at"] = datetime.now().isoformat()
        
        # Call the controller to add the user
        result = add_user(user_data)
        return JSONResponse(
            status_code=201,
            content={"message": "User created successfully", "user": result}
        )
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"message": str(e)}
        )