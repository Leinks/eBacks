from typing import List, Union
from models.product import Product
from beanie import PydanticObjectId

product_collection = Product

############################### Product Schema #################################

async def retrieve_products() -> List[Product]:
    products = await product_collection.all().to_list()
    return products


async def add_product(new_product: Product) -> Product:
    product = await new_product.create()
    return product

async def retrieve_products_category(id_category: Product): 
    products = await product_collection.find(Product.id_category == id_category).to_list()
    if products:
        return products

async def retrieve_product(id: PydanticObjectId) -> Product:
    product = await product_collection.get(id)
    if product:
        return product


async def delete_product(id: PydanticObjectId) -> bool:
    product = await product_collection.get(id)
    if product:
        await product.delete()
        return True


async def update_product_data(id: PydanticObjectId, data: dict) -> Union[bool, Product]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    product = await product_collection.get(id)
    if product:
        await product.update(update_query)
        return product
    return False

############################### Fin Product Schema #############################