# Backend/routes/user.py
from fastapi import APIRouter
from controllers.user_controller import get_user_by_id

router = APIRouter()

@router.get("/user/{user_id}")
def read_user(user_id: int):
    return get_user_by_id(user_id)
