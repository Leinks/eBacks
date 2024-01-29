from typing import Optional, Any
from datetime import datetime
from beanie import Document
from pydantic import BaseModel, EmailStr

class Company(Document):
    id_admin: str
    name: str
    document:str
    phone: Optional[str] = None
    email: EmailStr
    logo: Optional[str] = None
    description:str
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()

    class Config:
        json_schema_extra = {
            "example": {
                "id_admin": "64bdb5ddda64b6c168da6f42",
                "name": "Meta",
                "document": "J-366959589",
                "phone": "+584149999",
                "email": "meta@mail.com",
                "logo": "https//logo.com",
                "description": "Empresa dedicada a la Técnologia",
            }
        }

    class Settings:
        name = "companys"


class UpdateCompanyModel(BaseModel): 
    id_admin: Optional[str]
    name: Optional[str]
    document:Optional[str]
    phone: Optional[str]
    email: Optional[EmailStr]
    logo: Optional[str] 
    description:Optional[str]
    updated_at: Optional[datetime] = datetime.now()

    class Collection:
        name = "companys"

    class Config:
        json_schema_extra = {
            "example": {
                "id_admin": "64bdb5ddda64b6c168da6f42",
                "name": "Meta",
                "document": "J-366959589",
                "phone": "+584149999",
                "email": "meta@mail.com",
                "logo": "https//logo.com",
                "description": "Empresa dedicada a la Técnologia",
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
                "data": "Company success !",
            }
        }
