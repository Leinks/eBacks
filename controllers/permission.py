from typing import List, Union
from beanie import PydanticObjectId
from models.permission import Permission

permission_collection = Permission

############################### Permission Schema ###########################

async def retrieve_permissions() -> List[Permission]:
    permissions = await permission_collection.all().to_list()
    return permissions


async def add_permission(new_permission: Permission) -> Permission:
    permission = await new_permission.create()
    return permission


async def retrieve_permission(id: PydanticObjectId) -> Permission:
    permission = await permission_collection.get(id)
    if permission:
        return permission


async def delete_permission(id: PydanticObjectId) -> bool:
    permission = await permission_collection.get(id)
    if permission:
        await permission.delete()
        return True


async def update_permission_data(id: PydanticObjectId, data: dict) -> Union[bool, Permission]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    permission = await permission_collection.get(id)
    if permission:
        await permission.update(update_query)
        return permission
    return False

############################### Fin Permission Schema #############################
