from typing import List, Union
from models.company import Company
from beanie import PydanticObjectId



company_collection = Company

############################### Company Schema ####################################

async def retrieve_companys() -> List[Company]:
    companys = await company_collection.all().to_list()
    return companys


async def add_company(new_company: Company) -> Company:
    company = await new_company.create()
    return company

async def retrieve_admin_company(id_admin: Company): 
    companys = await company_collection.find(Company.id_admin == id_admin).to_list()
    # company = await company_collection.get(id_admin).to_list()
    if companys:
        return companys

async def retrieve_company(id: PydanticObjectId) -> Company:
    company = await company_collection.get(id)
    if company:
        return company


async def delete_company(id: PydanticObjectId) -> bool:
    company = await company_collection.get(id)
    if company:
        await company.delete()
        return True


async def update_company_data(id: PydanticObjectId, data: dict) -> Union[bool, Company]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    company = await company_collection.get(id)
    if company:
        await company.update(update_query)
        return company
    return False

############################### Fin Company Schema ##############################
