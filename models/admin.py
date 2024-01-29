from typing import Optional
from beanie import Document
from datetime import datetime
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr

class Admin(Document):
    name: str
    email: EmailStr
    password: str
    photo: Optional[str] = None
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Engelbert Tovar",
                "email": "admin@mail.dev",
                "password": "secreto",
                "photo": "https://images.pexels.com/photos/4804267/pexels-photo-4804267.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            }
        }

    class Settings:
        name = "admin"


class AdminSignIn(HTTPBasicCredentials):
    class Config:
        json_schema_extra = {
            "example": {"username": "admin@mail.dev", "password": "secreto"}
        }


class AdminData(BaseModel):
    name: str
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Engelbert Tovar",
                "email": "admin@mail.dev",
            }
        }
