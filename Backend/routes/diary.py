from fastapi import APIRouter
from controllers.diary_controller import add_diary_entry
from fastapi.responses import JSONResponse
from schemas.diary import DiaryEntryCreate, DiaryEntryResponse
from datetime import datetime

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