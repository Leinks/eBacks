from fastapi import APIRouter, Body, HTTPException
from passlib.context import CryptContext

from controllers.user import *
from models.user import *

router = APIRouter()
hash_helper = CryptContext(schemes=["bcrypt"])

@router.get("/", response_description="Users retrieved", response_model=Response)
async def get_users():
    users = await retrieve_users()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Users data retrieved successfully",
        "data": users,
    }


@router.get("/{id}", response_description="Users data retrieved", response_model=Response)
async def get_user_data(id: PydanticObjectId):
    user = await retrieve_user(id)
    if user:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Users data retrieved successfully",
            "data": user,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Users doesn't exist",
    }


# @router.post("/", response_description="Users data added into the database", response_model=Response,)
# async def add_user_data(user: User = Body(...)):
#     new_user = await add_user(user)
#     return {
#         "status_code": 200,
#         "response_type": "success",
#         "description": "Users created successfully",
#         "data": new_user,
#     }


@router.post("/", response_model=Response)
async def add_user_data(user: User = Body(...)):
    user_exists = await User.find_one(User.email == user.email)
    if user_exists:
        raise HTTPException(
            status_code=409, detail="Users with email supplied already exists"
        )

    user.password = hash_helper.encrypt(user.password)
    new_user = await add_user(user)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Users created successfully",
        "data": new_user,
    }

@router.delete("/{id}", response_description="Users data deleted from the database")
async def delete_user_data(id: PydanticObjectId):
    deleted_user = await delete_user(id)
    if deleted_user:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Users with ID: {} removed".format(id),
            "data": deleted_user,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Users with id {0} doesn't exist".format(id),
        "data": False,
    }


@router.put("/{id}", response_model=Response)
async def update_user(id: PydanticObjectId, req: UpdateUserModel = Body(...)):
    updated_user = await update_user_data(id, req.dict())
    if updated_user:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Users with ID: {} updated".format(id),
            "data": updated_user,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Users with ID: {} not found".format(id),
        "data": False,
    }



