from fastapi import APIRouter, HTTPException
from controllers.emoji_controller import get_this_month_emoji
from schemas.emoji import ThisMonthEmojiResponse
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/this_month_emoji/{year_month}", response_model=ThisMonthEmojiResponse)
async def get_monthly_emoji(year_month: str):
    """
    獲取指定月份的每日 emoji 數據
    
    Args:
        year_month (str): 格式為 "YYYY-MM" 的月份字符串
        
    Returns:
        ThisMonthEmojiResponse: 包含該月份所有日期的 emoji 數據
    """
    try:
        logger.info(f"收到請求: /this_month_emoji/{year_month}")
        
        # 驗證年月格式
        try:
            year, month = map(int, year_month.split('-'))
            if not (1 <= month <= 12):
                raise ValueError("Month must be between 1 and 12")
        except ValueError as e:
            logger.error(f"無效的年月格式: {year_month}")
            raise HTTPException(
                status_code=400,
                detail="Invalid year_month format. Expected format: YYYY-MM"
            )
        
        result = get_this_month_emoji(year_month)
        logger.info(f"成功返回數據: {result}")
        return result
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"處理請求時發生錯誤: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=str(e)
        ) 