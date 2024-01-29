from fastapi import APIRouter, Body

from controllers.product import *
from models.product import *

router = APIRouter()

@router.get("/", response_description="Products retrieved", response_model=Response)
async def get_products():
    products = await retrieve_products()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Products data retrieved successfully",
        "data": products,
    }


@router.get("/{id}", response_description="Products data retrieved", response_model=Response)
async def get_product_data(id: PydanticObjectId):
    product = await retrieve_product(id)
    if product:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Products data retrieved successfully",
            "data": product,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Products doesn't exist",
    }

@router.get("/admin/{id}", response_description="Locals Admin data retrieved", response_model=Response)
async def get_admin_products_data(id_category: str):
    locals = await retrieve_products_category(id_category)
    if locals:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Locals admin data retrieved successfully",
            "data": locals,
        }
    return {
    "status_code": 404,
    "response_type": "error",
    "description": "Locals doesn't exist",
    }


@router.post("/", response_description="Products data added into the database", response_model=Response,)
async def add_product_data(product: Product = Body(...)):
    new_product = await add_product(product)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Products created successfully",
        "data": new_product,
    }

@router.put("/{id}", response_model=Response)
async def update_product(id: PydanticObjectId, req: UpdateProductModel = Body(...)):
    updated_product = await update_product_data(id, req.dict())
    if updated_product:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Products with ID: {} updated".format(id),
            "data": updated_product,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Products with ID: {} not found".format(id),
        "data": False,
    }
    
@router.delete("/{id}", response_description="Products data deleted from the database")
async def delete_product_data(id: PydanticObjectId):
    deleted_product = await delete_product(id)
    if deleted_product:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Products with ID: {} removed".format(id),
            "data": deleted_product,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Products with id {0} doesn't exist".format(id),
        "data": False,
    }


