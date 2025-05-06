from pydantic import BaseModel, Field, validator
from datetime import date, datetime
from typing import Optional

class DiaryEntryCreate(BaseModel):
    """
    創建日記條目的請求模型
    """
    user_id: int
    entry_date: date
    content: str  # 前端使用 content
    mood_icon_code: str

class DiaryEntry(DiaryEntryCreate):
    """
    日記條目的完整模型，包含所有欄位
    """
    id: int
    hex_color_code: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True

class DiaryEntryResponse(BaseModel):
    """
    日記條目的響應模型
    """
    id: int
    user_id: int
    content_text: str  # 資料庫使用 content_text
    hex_color_code: Optional[str]
    mood_icon_code: str
    entry_date: date
    created_at: datetime
    updated_at: Optional[datetime] = None 