from typing import Optional, Any
from datetime import datetime
from beanie import Document
from pydantic import BaseModel

class Role(Document):
    name: str
    description: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Admin",
                "description": "Este Role Hace Tal Vaina",
                "created_at": datetime.now(),
                "updated_at": datetime.now(),
            }
        }

    class Settings:
        name = "roles"


class UpdateRoleModel(BaseModel):
    name: Optional[str]
    description: Optional[str]
    updated_at: Optional[datetime] = None

    class Collection:
        name = "roles"

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Admin",
                "description": "Este Role Hace Tal Vaina",
                "updated_at": datetime.now(),
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
                "data": "Sample data",
            }
        }
