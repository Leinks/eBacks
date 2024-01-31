from fastapi import APIRouter, Body, HTTPException
from controllers.store import *
from models.store import *

router = APIRouter()


@router.get("/", response_description="Store retrieved", response_model=Response)
async def get_stores():
    stores = await retrieve_stores()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Stores data retrieved successfully",
        "data": stores,
    }


@router.get("/{id}", response_description="Store data retrieved", response_model=Response)
async def get_store_data(id: PydanticObjectId):
    store = await retrieve_store(id)
    if store:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Store data retrieved successfully",
            "data": store,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Store doesn't exist",
    }

@router.get("/admin/{id}", response_description="Stores Company data retrieved", response_model=Response)
async def get_admin_store_data(id_company: str):
    stores = await retrieve_stores_company(id_company)
    if stores:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Stores admin data retrieved successfully",
            "data": stores,
        }
    return {
    "status_code": 404,
    "response_type": "error",
    "description": "Stores doesn't exist",
    }


@router.post("/", response_description="Store data added into the database", response_model=Response,)
async def add_store_data(store: Store = Body(...)):
    store_exists = await Store.find_one(Store.email == store.email)
    if store_exists:
        raise HTTPException(
            status_code=409, detail="store with email supplied already exists"
        )
    new_store = await add_store(store)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Store created successfully",
        "data": new_store,
    }


@router.put("/{id}", response_model=Response)
async def update_store(id: PydanticObjectId, req: UpdateStoreModel = Body(...)):
    updated_store = await update_store_data(id, req.model_dump())
    if updated_store:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Store with ID: {} updated".format(id),
            "data": updated_store,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Store with ID: {} not found".format(id),
        "data": False,
    }
    
@router.delete("/{id}", response_description="Store data deleted from the database")
async def delete_store_data(id: PydanticObjectId):
    deleted_store = await delete_store(id)
    if deleted_store:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Store with ID: {} removed".format(id),
            "data": deleted_store,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Store with id {0} doesn't exist".format(id),
        "data": False,
    }


