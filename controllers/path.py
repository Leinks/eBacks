from typing import List, Union
from models.path import Path
from beanie import PydanticObjectId

path_collection = Path

############################### Path Schema ####################################

async def retrieve_paths() -> List[Path]:
    paths = await path_collection.all().to_list()
    return paths


async def add_path(new_path: Path) -> Path:
    path = await new_path.create()
    return path


async def retrieve_path(id: PydanticObjectId) -> Path:
    path = await path_collection.get(id)
    if path:
        return path


async def delete_path(id: PydanticObjectId) -> bool:
    path = await path_collection.get(id)
    if path:
        await path.delete()
        return True


async def update_path_data(id: PydanticObjectId, data: dict) -> Union[bool, Path]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    path = await path_collection.get(id)
    if path:
        await path.update(update_query)
        return path
    return False

############################### Fin Path Schema ##############################
