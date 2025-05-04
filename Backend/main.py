# Backend/main.py
from fastapi import FastAPI
from routes import user
from routes import journal
from routes import mood_tree

app = FastAPI()

app.include_router(user.router, prefix="/api")
app.include_router(journal.router, prefix="/api")
app.include_router(mood_tree.router, prefix="/api")