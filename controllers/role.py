from models.role import Role
from typing import List, Union
from beanie import PydanticObjectId

role_collection = Role

############################### Role Schema #################################

async def retrieve_roles() -> List[Role]:
    roles = await role_collection.all().to_list()
    return roles

async def add_role(new_role: Role) -> Role:
    role = await new_role.create()
    return role

async def retrieve_role(id: PydanticObjectId) -> Role:
    role = await role_collection.get(id)
    if role:
        return role

async def delete_role(id: PydanticObjectId) -> bool:
    role = await role_collection.get(id)
    if role:
        await role.delete()
        return True

async def update_role_data(id: PydanticObjectId, data: dict) -> Union[bool, Role]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    role = await role_collection.get(id)
    if role:
        await role.update(update_query)
        return role
    return False

############################### Fin Role Schema #############################