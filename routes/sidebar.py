from fastapi import APIRouter, Body

from controllers.sidebar import *
from models.sidebar import *

router = APIRouter()

@router.get("/", response_description="Local retrieved", response_model=Response)
async def get_sidebars():
    sidebars = await retrieve_sidebars()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Sidebars data retrieved successfully",
        "data": sidebars,
    }


@router.get("/{id}", response_description="SideBar item retrieved", response_model=Response)
async def get_sidebar_data(id: PydanticObjectId):
    sidebar = await retrieve_sidebar(id)
    if sidebar:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "SideBar item retrieved successfully",
            "data": sidebar,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Sidebar doesn't exist",
    }


@router.post("/", response_description="Sidebar data added into the database", response_model=Response,)
async def add_sidebar_data(sidebar: Sidebar = Body(...)):
    new_sidebar = await add_sidebar(sidebar)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Sidebar created successfully",
        "data": new_sidebar,
    }

@router.put("/{id}", response_model=Response)
async def update_sidebar(id: PydanticObjectId, req: UpdateSidebarModel = Body(...)):
    updated_sidebar = await update_sidebar_data(id, req.dict())
    if updated_sidebar:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Sidebar with ID: {} updated".format(id),
            "data": updated_sidebar,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Sidebar with ID: {} not found".format(id),
        "data": False,
    }
    
@router.delete("/{id}", response_description="Sidebar data deleted from the database")
async def delete_sidebar_data(id: PydanticObjectId):
    deleted_sidebar = await delete_sidebar(id)
    if deleted_sidebar:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Sidebar with ID: {} removed".format(id),
            "data": deleted_sidebar,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Sidebar with id {0} doesn't exist".format(id),
        "data": False,
    }


