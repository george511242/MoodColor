from pydantic import BaseModel
from datetime import date

class DeleteResponse(BaseModel):
    status: str
    entry_date: date
