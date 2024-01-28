from typing import List, Union
from beanie import PydanticObjectId
from models.category import Category


category_collection = Category

############################### Category Schema #################################

async def retrieve_categories() -> List[Category]:
    categories = await category_collection.all().to_list()
    return categories


async def add_category(new_category: Category) -> Category:
    category = await new_category.create()
    return category


async def retrieve_category(id: PydanticObjectId) -> Category:
    category = await category_collection.get(id)
    if category:
        return category


async def delete_category(id: PydanticObjectId) -> bool:
    category = await category_collection.get(id)
    if category:
        await category.delete()
        return True


async def update_category_data(id: PydanticObjectId, data: dict) -> Union[bool, Category]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    category = await category_collection.get(id)
    if category:
        await category.update(update_query)
        return category
    return False

############################### Fin Category Schema #############################