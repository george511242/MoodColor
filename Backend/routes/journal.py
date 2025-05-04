from fastapi import APIRouter, HTTPException
from datetime import date
from schemas.delete_response import DeleteResponse
from controllers.journal_controller import delete_journal_by_date

router = APIRouter()

@router.delete("/delete/{journal_date}", response_model=DeleteResponse)
async def delete_journey(journal_date: date):
    result = delete_journal_by_date(journal_date)
    
    if result["status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])
    
    return result
