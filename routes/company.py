from fastapi import APIRouter, Body

from controllers.company import *
from models.company import *

router = APIRouter()

@router.get("/", response_description="Companys retrieved", response_model=Response)
async def get_companys():
    companys = await retrieve_companys()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Companys data retrieved successfully",
        "data": companys,
    }


@router.get("/{id}", response_description="Companys data retrieved", response_model=Response)
async def get_company_data(id: PydanticObjectId):
    company = await retrieve_company(id)
    if company:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Companys data retrieved successfully",
            "data": company,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Companys doesn't exist",
    }


@router.post("/", response_description="Companys data added into the database", response_model=Response,)
async def add_company_data(company: Company = Body(...)):
    new_company = await add_company(company)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Companys created successfully",
        "data": new_company,
    }

@router.put("/{id}", response_model=Response)
async def update_company(id: PydanticObjectId, req: UpdateCompanyModel = Body(...)):
    updated_company = await update_company_data(id, req.model_dump())
    if updated_company:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Companys with ID: {} updated".format(id),
            "data": updated_company,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Companys with ID: {} not found".format(id),
        "data": False,
    }
    
@router.delete("/{id}", response_description="Companys data deleted from the database")
async def delete_company_data(id: PydanticObjectId):
    deleted_company = await delete_company(id)
    if deleted_company:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Companys with ID: {} removed".format(id),
            "data": deleted_company,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Companys with id {0} doesn't exist".format(id),
        "data": False,
    }


