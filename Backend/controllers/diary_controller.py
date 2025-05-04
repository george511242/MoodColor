from supabase_client import supabase
from datetime import datetime
from typing import Dict, Any, List
from schemas.diary import DiaryEntry, DiaryEntryCreate, DiaryEntryResponse
from controllers.color_controller import generate_color_from_text
from fastapi import HTTPException
import logging
from controllers.google_drive_controller import upload_image_to_drive
import os
import tempfile

# 設置日誌
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_user_exists(user_id: int) -> bool:
    """
    檢查用戶是否存在
    
    Args:
        user_id (int): 用戶 ID
        
    Returns:
        bool: 用戶是否存在
    """
    try:
        response = supabase.table("USER").select("id").eq("id", user_id).execute()
        return len(response.data) > 0
    except Exception as e:
        logger.error(f"檢查用戶存在性時發生錯誤: {str(e)}")
        return False

def create_diary_entry(entry: DiaryEntryCreate) -> DiaryEntry:
    """
    創建新的日記條目
    
    Args:
        entry (DiaryEntryCreate): 包含日記內容的對象
        
    Returns:
        DiaryEntry: 創建後的日記條目
    """
    try:
        logger.info(f"開始創建用戶 {entry.user_id} 的日記條目")
        
        # 檢查用戶是否存在
        if not check_user_exists(entry.user_id):
            raise HTTPException(
                status_code=404,
                detail=f"User with id {entry.user_id} not found"
            )
        
        # 生成顏色代碼
        hex_color_code = generate_color_from_text(entry.content)
        logger.info(f"生成的顏色代碼: {hex_color_code}")
        
        # 準備插入數據
        diary_data = {
            "user_id": entry.user_id,
            "entry_date": entry.entry_date.isoformat(),
            "content_text": entry.content,
            "mood_icon_code": entry.mood_icon_code,
            "hex_color_code": hex_color_code
        }
        
        # 插入數據到資料庫
        response = supabase.table("DIARY_ENTRY").insert(diary_data).execute()
        
        if not response.data:
            logger.error("創建日記條目失敗")
            raise HTTPException(
                status_code=500,
                detail="Failed to create diary entry"
            )
        
        logger.info("日記條目創建成功")
        return DiaryEntry(**response.data[0])
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"創建日記條目時發生錯誤: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error creating diary entry: {str(e)}"
        )

def add_diary_entry(entry_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Add a new diary entry to the database.
    
    Args:
        entry_data (Dict[str, Any]): Dictionary containing diary entry data
        
    Returns:
        Dict[str, Any]: The created diary entry with additional fields
    """
    try:
        # 驗證輸入數據
        diary_entry = DiaryEntryCreate(**entry_data)
        
        # 檢查用戶是否存在
        if not check_user_exists(diary_entry.user_id):
            raise HTTPException(
                status_code=404,
                detail=f"User with id {diary_entry.user_id} not found"
            )
        
        # 生成顏色代碼
        hex_color_code = generate_color_from_text(diary_entry.content)
        logger.info(f"生成的顏色代碼: {hex_color_code}")
        
        # 轉換為字典並處理特殊欄位
        data = {
            "user_id": diary_entry.user_id,
            "entry_date": diary_entry.entry_date.isoformat(),
            "content_text": diary_entry.content,
            "mood_icon_code": diary_entry.mood_icon_code,
            "hex_color_code": hex_color_code,
            "created_at": datetime.now().isoformat()
        }
        
        # Insert the entry into the database
        result = supabase.table("DIARY_ENTRY").insert(data).execute()
        
        if not result.data:
            # Check if there's an error in the result
            if hasattr(result, 'error') and result.error:
                raise HTTPException(
                    status_code=500,
                    detail=f"Database error: {result.error}"
                )
            else:
                raise HTTPException(
                    status_code=500,
                    detail="Failed to create diary entry: No data returned and no error message"
                )
            
        return result.data[0]
    except HTTPException:
        raise
    except Exception as e:
        # Print the full error for debugging
        print(f"Full error details: {str(e)}")
        print(f"Entry data that caused the error: {entry_data}")
        raise HTTPException(
            status_code=500,
            detail=f"Error creating diary entry: {str(e)}"
        )

def create_diary():
    try:
        data = request.form.to_dict()
        image_file = request.files.get('image')
        
        # 處理圖片上傳
        image_url = None
        if image_file:
            # 創建臨時文件
            with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
                image_file.save(temp_file.name)
                # 上傳到 Google Drive
                image_url = upload_image_to_drive(temp_file.name)
                # 刪除臨時文件
                os.unlink(temp_file.name)
        
        # 生成顏色代碼
        hex_color_code = generate_color_from_text(data.get('content', ''))
        logger.info(f"生成的顏色代碼: {hex_color_code}")
        
        # 創建日記條目
        diary_entry = DiaryEntry(
            content=data.get('content'),
            mood_icon_code=data.get('mood_icon_code'),
            image_url=image_url,
            hex_color_code=hex_color_code
        )
        
        # 保存到數據庫
        diary_entry.save()
        
        return jsonify({
            "status": "success",
            "message": "日記創建成功",
            "data": {
                "id": str(diary_entry.id),
                "content": diary_entry.content,
                "mood_icon_code": diary_entry.mood_icon_code,
                "image_url": diary_entry.image_url,
                "hex_color_code": diary_entry.hex_color_code,
                "created_at": diary_entry.created_at.isoformat()
            }
        }), 201
        
    except Exception as e:
        logger.error(f"創建日記時發生錯誤: {str(e)}")
        return jsonify({
            "status": "error",
            "message": f"創建日記失敗: {str(e)}"
        }), 500 