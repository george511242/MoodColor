from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class DiaryEntryCreate(BaseModel):
    user_id: int
    content_text: str
    photo_url: Optional[str] = None
    hex_color_code: str
    mood_icon_url: str
    entry_date: date

class DiaryEntryResponse(BaseModel):
    id: int
    user_id: int
    content_text: str
    photo_url: Optional[str]
    hex_color_code: str
    mood_icon_url: str
    entry_date: date
    created_at: datetime 