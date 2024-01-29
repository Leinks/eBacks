from typing import Optional, Any
from datetime import datetime
from beanie import Document
from pydantic import BaseModel

class Path(Document):
    path: str
    active: Optional[bool] = True
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()

    class Config:
        json_schema_extra = {
            "example": {
                "path": "companys",
                "active": True
            }
        }

    class Settings:
        name = "path"


class UpdatePathModel(BaseModel): 
    path: Optional[str]
    active: Optional[bool]
    updated_at: Optional[datetime] = datetime.now()
    
    class Collection:
        name = "path"

    class Config:
        json_schema_extra = {
            "example": {
                "path": "companys",
                "active": True
            }
        }


class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        json_schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Path success !",
            }
        }
