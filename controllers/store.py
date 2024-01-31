from models.store import Store
from typing import List, Union
from beanie import PydanticObjectId

store_collection = Store

############################### Store Schema ####################################

async def retrieve_stores() -> List[Store]:
    stores = await store_collection.all().to_list()
    return stores


async def add_store(new_store: Store) -> Store:
    store = await new_store.create()
    return store

async def retrieve_stores_company(id_company: Store): 
    stores = await store_collection.find(Store.id_company == id_company).to_list()
    if stores:
        return stores

async def retrieve_store(id: PydanticObjectId) -> Store:
    store = await store_collection.get(id)
    if store:
        return store

async def delete_store(id: PydanticObjectId) -> bool:
    store = await store_collection.get(id)
    if store:
        await store.delete()
        return True

async def update_store_data(id: PydanticObjectId, data: dict) -> Union[bool, Store]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    store = await store_collection.get(id)
    if store:
        await store.update(update_query)
        return store
    return False

############################### Fin Store Schema ################################