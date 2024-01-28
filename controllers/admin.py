from models.admin import Admin
# from typing import List, Union
# from beanie import PydanticObjectId

admin_collection = Admin

############################### Admin Schema #################################
async def add_admin(new_admin: Admin) -> Admin:
    admin = await new_admin.create()
    return admin
############################### Admin Schema #################################