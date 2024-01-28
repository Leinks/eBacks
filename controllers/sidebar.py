from typing import List, Union
from models.sidebar import Sidebar
from beanie import PydanticObjectId

sidebar_collection = Sidebar

############################### Sidebar Schema ####################################

async def retrieve_sidebars() -> List[Sidebar]:
    sidebars = await sidebar_collection.all().to_list()
    return sidebars


async def add_sidebar(new_sidebar: Sidebar) -> Sidebar:
    sidebar = await new_sidebar.create()
    return sidebar


async def retrieve_sidebar(id: PydanticObjectId) -> Sidebar:
    sidebar = await sidebar_collection.get(id)
    if sidebar:
        return sidebar


async def delete_sidebar(id: PydanticObjectId) -> bool:
    sidebar = await sidebar_collection.get(id)
    if sidebar:
        await sidebar.delete()
        return True


async def update_sidebar_data(id: PydanticObjectId, data: dict) -> Union[bool, Sidebar]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    sidebar = await sidebar_collection.get(id)
    if sidebar:
        await sidebar.update(update_query)
        return sidebar
    return False

############################### Fin Sidebar Schema ##############################
