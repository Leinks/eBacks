from typing import Optional, Any
from datetime import datetime
from beanie import Document
from pydantic import BaseModel

class Product(Document):
    id_category: str
    name: str
    description:str
    price:int
    ref:int
    photo: Optional[str] = None
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()

    class Config:
        json_schema_extra = {
            "example": {
                "id_category": "64aaecf52d549fa85eb93395",
                "name": "Hamburguesa La Reina",
                "description": "Hamburguesa Rellena de 100gr de Carne, Papas fritas, Huevo, Lechuga, Tomate Queso, Salsa de Tomate y Mayonesa",
                "price": "200",
                "ref": "6",
                "photo": "https//photo.com",
            }
        }

    class Settings:
        name = "products"


class UpdateProductModel(BaseModel):
    id_category: Optional[str]
    name: Optional[str]
    description:Optional[str]
    price:Optional[str]
    ref:Optional[str]
    photo: Optional[str]
    updated_at: Optional[datetime] = datetime.now()

    class Collection:
        name = "products"

    class Config:
        json_schema_extra = {
            "example": {
                "id_category": "64aaecf52d549fa85eb93395",
                "name": "Hamburguesa La Reina",
                "description": "Hamburguesa Rellena de 100gr de Carne, Papas fritas, Huevo, Lechuga, Tomate Queso, Salsa de Tomate y Mayonesa",
                "price": "200",
                "ref": "6",
                "photo": "https//photo.com",
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
