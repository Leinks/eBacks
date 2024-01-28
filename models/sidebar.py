from typing import Optional, Any
from datetime import datetime
from beanie import Document
from pydantic import BaseModel

class Sidebar(Document):
    path: str
    title:str
    icon: str
    main_icon_id: Optional[str] = None
    icon_opened: Optional[str] = None
    icon_close: Optional[str] = None
    children: Optional[bool] = False
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "path": "companys",
                "title": "Companys",
                "icon": "Building",
                "main_icon_id": "mqwreg5ffgsdq",
                "icon_opened": "ChevronRight",
                "icon_close": "ChevronDown",
                "children": True
            }
        }

    class Settings:
        name = "sidebar"


class UpdateSidebarModel(BaseModel): 
    path: Optional[str]
    title:Optional[str]
    icon: Optional[str]
    main_icon_id: Optional[str]
    icon_opened: Optional[str]
    icon_close: Optional[str]
    children: Optional[bool]
    updated_at: Optional[datetime] = datetime.now()
    
    class Collection:
        name = "sidebar"

    class Config:
        schema_extra = {
            "example": {
                "path": "companys",
                "title": "Companys",
                "icon": "Building",
                "main_icon_id": "mqwreg5ffgsdq",
                "icon_opened": "ChevronRight",
                "icon_close": "ChevronDown",
                "children": True
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
                "data": "sidebar success !",
            }
        }
