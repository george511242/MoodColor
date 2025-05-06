from fastapi import APIRouter, UploadFile, File, Form
from controllers.diary_controller import add_diary_entry
from controllers.google_drive_controller import upload_image_to_drive
from fastapi.responses import JSONResponse
from schemas.diary import DiaryEntryCreate, DiaryEntryResponse
from datetime import datetime
import tempfile
import os

router = APIRouter()

@router.post("/diary", response_model=DiaryEntryResponse)
async def create_diary_entry(entry: DiaryEntryCreate):
    """
    Create a new diary entry.
    
    Args:
        entry (DiaryEntryCreate): The diary entry data to create
        
    Returns:
        JSONResponse: The created diary entry or an error message
    """
    try:
        # Convert Pydantic model to dict
        entry_data = entry.dict()
        
        # Add the entry to the database
        result = add_diary_entry(entry_data)
        
        return JSONResponse(
            status_code=201,
            content={"message": "Diary entry created successfully", "entry": result}
        )
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"message": str(e)}
        )

@router.post("/diary/upload-image")
async def upload_diary_image(file: UploadFile = File(...)):
    """
    Upload an image for a diary entry.
    
    Args:
        file (UploadFile): The image file to upload
        
    Returns:
        JSONResponse: The URL of the uploaded image or an error message
    """
    try:
        # 創建臨時文件
        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
            content = await file.read()
            temp_file.write(content)
            temp_file_path = temp_file.name
        
        # 上傳到 Google Drive
        image_url = upload_image_to_drive(temp_file_path)
        
        # 刪除臨時文件
        os.unlink(temp_file_path)
        
        return JSONResponse(
            status_code=200,
            content={"message": "Image uploaded successfully", "image_url": image_url}
        )
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"message": str(e)}
        ) 