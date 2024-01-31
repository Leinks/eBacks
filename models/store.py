from typing import Optional, Any
from datetime import datetime
from beanie import Document
from pydantic import BaseModel, EmailStr

class Store(Document):
    id_company: str
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
                "id_company": "64aae8d1feedeedf8444d711",
                "name": "Facebook",
                "document": "J-334442234",
                "phone": "+584145555",
                "email": "facebook@mail.com",
                "logo": "https//logo.com",
                "description": "Somos La Mejor Red Social Ven y Conectate !",
            }
        }

    class Settings:
        name = "stores"


class UpdateStoreModel(BaseModel):
    id_company: Optional[str]
    name: Optional[str]
    document:Optional[str]
    phone: Optional[str]
    email: Optional[EmailStr]
    logo: Optional[str]
    description:Optional[str]
    updated_at: Optional[datetime] = datetime.now()

    class Collection:
        name = "stores"

    class Config:
        json_schema_extra = {
            "example": {
                "id_company": "64aae8d1feedeedf8444d711",
                "name": "Facebook",
                "document": "J-334442234",
                "phone": "+584145555",
                "email": "facebook@mail.com",
                "logo": "https//logo.com",
                "description": "Somos La Mejor Red Social Ven y Conectate !",
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
