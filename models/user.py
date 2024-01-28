from typing import Optional, Any
from datetime import datetime
from beanie import Document
from pydantic import BaseModel, EmailStr

class User(Document):
    name: str
    email: EmailStr
    password: str
    photo: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Samuel David Tovar",
                "email": "Samuelt@mail.com",
                "password": "secret",
                "photo": "https://images.pexels.com/photos/4804267/pexels-photo-4804267.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                "created_at": datetime.now(),
                "updated_at": datetime.now(),
            }
        }

    class Settings:
        name = "users"


class UpdateUserModel(BaseModel):
    name: Optional[str]
    photo: Optional[str]
    updated_at: Optional[datetime]

    class Collection:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "name": "Abdulazeez Abdulazeez",
                "email": "abdul@school.com",
                "photo": "https://images.pexels.com/photos/4804267/pexels-photo-4804267.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                "updated_at": datetime.now(),
            }
        }

class UpdateUserPassword(BaseModel):
    password: str
    updated_at: Optional[datetime] = None
    class Config:
        schema_extra = {
            "example": {
                "password": "secret",
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
