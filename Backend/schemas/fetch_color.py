from pydantic import BaseModel
from typing import Optional

class FetchColor(BaseModel):
    hex: str
    owner_name: Optional[str] = None  # owner_name 可以為 null
