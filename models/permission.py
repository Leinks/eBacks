from typing import Optional, Any
from datetime import datetime
from beanie import Document
from pydantic import BaseModel

class Permission(Document):
    id_role: str
    name: str
    description: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        schema_extra = {
            "example": {
                "id_role": "q2312eqwdqwe1",
                "name": "Admin",
                "description": "Total Access",
                "created_at": datetime.now(),
                "updated_at": datetime.now(),

            }
        }

    class Settings:
        name = "permissions"


class UpdatePermissionModel(BaseModel):
    id_role: Optional[str]
    name: Optional[str]
    description: Optional[str]
    updated_at:  Optional[datetime]

    class Collection:
        name = "permissions"

    class Config:
        schema_extra = {
            "example": {
                "id_role": "q2312eqwdqwe1",
                "name": "Admin",
                "description": "Total Access",
                "updated_at": datetime.now(),
            }
        }


class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data",
            }
        }
