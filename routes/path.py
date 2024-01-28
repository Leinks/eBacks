from fastapi import APIRouter, Body

from controllers.path import *
from models.path import *

router = APIRouter()

@router.get("/", response_description="Path retrieved", response_model=Response)
async def get_paths():
    paths = await retrieve_paths()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Path data retrieved successfully",
        "data": paths,
    }


@router.get("/{id}", response_description="Path item retrieved", response_model=Response)
async def get_path_data(id: PydanticObjectId):
    path = await retrieve_path(id)
    if path:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Path item retrieved successfully",
            "data": path,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Path doesn't exist",
    }


@router.post("/", response_description="Path data added into the database", response_model=Response,)
async def add_path_data(path: Path = Body(...)):
    new_path = await add_path(path)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Path created successfully",
        "data": new_path,
    }

@router.put("/{id}", response_model=Response)
async def update_path(id: PydanticObjectId, req: UpdatePathModel = Body(...)):
    updated_path = await update_path_data(id, req.dict())
    if updated_path:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Path with ID: {} updated".format(id),
            "data": updated_path,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Path with ID: {} not found".format(id),
        "data": False,
    }
    
@router.delete("/{id}", response_description="Path data deleted from the database")
async def delete_path_data(id: PydanticObjectId):
    deleted_path = await delete_path(id)
    if deleted_path:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Path with ID: {} removed".format(id),
            "data": deleted_path,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Path with id {0} doesn't exist".format(id),
        "data": False,
    }


