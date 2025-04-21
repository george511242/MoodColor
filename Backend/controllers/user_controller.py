# Backend/controllers/user_controller.py
from fastapi import HTTPException
from supabase_client import supabase

def get_user_by_id(user_id: int):
    response = supabase.table("USER").select("*").eq("id", user_id).execute()

    if not response.data:
        raise HTTPException(status_code=404, detail="User not found")
    
    return response.data[0]
