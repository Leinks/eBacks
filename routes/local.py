from fastapi import APIRouter, Body, HTTPException
from controllers.local import *
from models.local import *

router = APIRouter()


@router.get("/", response_description="Local retrieved", response_model=Response)
async def get_locals():
    locals = await retrieve_locals()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Locals data retrieved successfully",
        "data": locals,
    }


@router.get("/{id}", response_description="Local data retrieved", response_model=Response)
async def get_local_data(id: PydanticObjectId):
    local = await retrieve_local(id)
    if local:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Local data retrieved successfully",
            "data": local,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Local doesn't exist",
    }


@router.post("/", response_description="Local data added into the database", response_model=Response,)
async def add_local_data(local: Local = Body(...)):
    local_exists = await Local.find_one(Local.email == local.email)
    if local_exists:
        raise HTTPException(
            status_code=409, detail="Local with email supplied already exists"
        )
    new_local = await add_local(local)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Local created successfully",
        "data": new_local,
    }


@router.put("/{id}", response_model=Response)
async def update_local(id: PydanticObjectId, req: UpdateLocalModel = Body(...)):
    updated_local = await update_local_data(id, req.dict())
    if updated_local:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Local with ID: {} updated".format(id),
            "data": updated_local,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Local with ID: {} not found".format(id),
        "data": False,
    }
    
@router.delete("/{id}", response_description="Local data deleted from the database")
async def delete_local_data(id: PydanticObjectId):
    deleted_local = await delete_local(id)
    if deleted_local:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Local with ID: {} removed".format(id),
            "data": deleted_local,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Local with id {0} doesn't exist".format(id),
        "data": False,
    }


