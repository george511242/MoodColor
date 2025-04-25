# Backend/main.py
from fastapi import FastAPI
from routes.user import router as user_router
from routes.diary import router as diary_router

app = FastAPI()

# Include routers
app.include_router(user_router, prefix="/api")
app.include_router(diary_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to MoodColor API"}
