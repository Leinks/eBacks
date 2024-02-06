from fastapi import APIRouter, Body
from controllers.role import *
from models.role import *

router = APIRouter()

@router.get("/", response_description="Roles retrieved", response_model=Response)
async def get_roles():
    roles = await retrieve_roles()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Roles data retrieved successfully",
        "data": roles,
    }


@router.get("/{id}", response_description="Roles data retrieved", response_model=Response)
async def get_role_data(id: PydanticObjectId):
    role = await retrieve_role(id)
    if role:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Roles data retrieved successfully",
            "data": role,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Roles doesn't exist",
    }


@router.post("/", response_description="Roles data added into the database", response_model=Response,)
async def add_role_data(role: Role = Body(...)):
    new_role = await add_role(role)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Roles created successfully",
        "data": new_role,
    }

@router.put("/{id}", response_model=Response)
async def update_role(id: PydanticObjectId, req: UpdateRoleModel = Body(...)):
    updated_role = await update_role_data(id, req.model_dump())
    if updated_role:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Roles with ID: {} updated".format(id),
            "data": updated_role,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Roles with ID: {} not found".format(id),
        "data": False,
    }
    
@router.delete("/{id}", response_description="Roles data deleted from the database")
async def delete_role_data(id: PydanticObjectId):
    deleted_role = await delete_role(id)
    if deleted_role:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Roles with ID: {} removed".format(id),
            "data": deleted_role,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Roles with id {0} doesn't exist".format(id),
        "data": False,
    }


