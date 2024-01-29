from fastapi import APIRouter, Body
from controllers.category import *
from models.category import *

router = APIRouter()


@router.get("/", response_description="Categories retrieved", response_model=Response)
async def get_categories():
    categories = await retrieve_categories()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Categories data retrieved successfully",
        "data": categories,
    }


@router.get(
    "/{id}", response_description="Categories data retrieved", response_model=Response
)
async def get_category_data(id: PydanticObjectId):
    category = await retrieve_category(id)
    if category:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Categories data retrieved successfully",
            "data": category,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Categories doesn't exist",
    }

@router.get("/admin/{id}", response_description="Categorys locals data retrieved", response_model=Response)
async def get_admin_category_data(id_local: str):
    categorys = await retrieve_categorys_locals(id_local)
    if categorys:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Locals admin data retrieved successfully",
            "data": categorys,
        }
    return {
    "status_code": 404,
    "response_type": "error",
    "description": "Locals doesn't exist",
    }


@router.post(
    "/",
    response_description="categorys data added into the database",
    response_model=Response,
)
async def add_category_data(category: Category = Body(...)):
    new_category = await add_category(category)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Categories created successfully",
        "data": new_category,
    }


@router.delete("/{id}", response_description="Categories data deleted from the database")
async def delete_category_data(id: PydanticObjectId):
    deleted_category = await delete_category(id)
    if deleted_category:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Categories with ID: {} removed".format(id),
            "data": deleted_category,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Categories with id {0} doesn't exist".format(id),
        "data": False,
    }


@router.put("/{id}", response_model=Response)
async def update_category(id: PydanticObjectId, req: UpdateCategoryModel = Body(...)):
    updated_category = await update_category_data(id, req.dict())
    if updated_category:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Categories with ID: {} updated".format(id),
            "data": updated_category,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Categories with ID: {} not found".format(id),
        "data": False,
    }
