from models.local import Local
from typing import List, Union
from beanie import PydanticObjectId

local_collection = Local

############################### Local Schema ####################################

async def retrieve_locals() -> List[Local]:
    locals = await local_collection.all().to_list()
    return locals


async def add_local(new_local: Local) -> Local:
    local = await new_local.create()
    return local


async def retrieve_local(id: PydanticObjectId) -> Local:
    local = await local_collection.get(id)
    if local:
        return local


async def delete_local(id: PydanticObjectId) -> bool:
    local = await local_collection.get(id)
    if local:
        await local.delete()
        return True


async def update_local_data(id: PydanticObjectId, data: dict) -> Union[bool, Local]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    local = await local_collection.get(id)
    if local:
        await local.update(update_query)
        return local
    return False

############################### Fin Local Schema ################################