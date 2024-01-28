from fastapi import APIRouter, Body

from controllers.permission import *
from models.permission import *

router = APIRouter()


@router.get("/", response_description="Permissions retrieved", response_model=Response)
async def get_permissions():
    permissions = await retrieve_permissions()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Permissions data retrieved successfully",
        "data": permissions,
    }


@router.get(
    "/{id}", response_description="Permissions data retrieved", response_model=Response
)
async def get_permission_data(id: PydanticObjectId):
    permission = await retrieve_permission(id)
    if permission:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Permissions data retrieved successfully",
            "data": permission,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Permissions doesn't exist",
    }


@router.post("/", response_description="Permissions data added into the database",response_model=Response,)
async def add_permission_data(permission: Permission = Body(...)):
    new_permission = await add_permission(permission)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Permissions created successfully",
        "data": new_permission,
    }


@router.delete("/{id}", response_description="Permissions data deleted from the database")
async def delete_permission_data(id: PydanticObjectId):
    deleted_permission = await delete_permission(id)
    if deleted_permission:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Permissions with ID: {} removed".format(id),
            "data": deleted_permission,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Permissions with id {0} doesn't exist".format(id),
        "data": False,
    }


@router.put("/{id}", response_model=Response)
async def update_permission(id: PydanticObjectId, req: UpdatePermissionModel = Body(...)):
    updated_permission = await update_permission_data(id, req.dict())
    if updated_permission:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Permissions with ID: {} updated".format(id),
            "data": updated_permission,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. permissions with ID: {} not found".format(id),
        "data": False,
    }
