# Backend/controllers/user_controller.py
from fastapi import HTTPException
from supabase_client import supabase
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

router = APIRouter()

def get_user_by_id(user_id: int):
    response = supabase.table("USER").select("*").eq("id", user_id).execute()

    if not response.data:
        raise HTTPException(status_code=404, detail="User not found")
    
    return response.data[0]

class UserCreate(BaseModel):
    username: str
    email: str
    password_hash: str
    created_at: Optional[datetime] = None

def add_user(user_data: dict):
    response = supabase.table("USER").insert(user_data).execute()

    if not response.data:
        raise HTTPException(status_code=400, detail="Failed to add user")
    
    return response.data[0]
