from fastapi import APIRouter, HTTPException
from datetime import datetime, timedelta
from schemas.mood_tree_color import MoodTreeColorResponse
from controllers.mood_tree_controller import get_yesterday_mood_color

router = APIRouter()

@router.get("/mood_tree_color/{user_id}", response_model=MoodTreeColorResponse)
async def get_mood_tree_color(user_id: int):
    # 獲取昨天的日期
    yesterday = datetime.now() - timedelta(days=1)
    yesterday_date = yesterday.date()  # 只保留日期，不包含時間
    
    # 從控制器中獲取昨天的情緒顏色資料
    result = get_yesterday_mood_color(yesterday_date, user_id)  # 假設 user_id 為 1，實際情況中應從請求中獲取
    
    # 假設返回結果的格式是 { "hex": "#FF5733", "owner_name": "John Doe" }
    return result
