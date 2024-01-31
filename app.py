from fastapi import FastAPI, Depends


from auth.jwt_bearer import JWTBearer
from config.config import initiate_database
from routes.admin import router as AdminRouter
from routes.user import router as UserRouter
from routes.role import router as RoleRouter
from routes.permission import router as PermissionRouter
from routes.company import router as CompanyRouter
from routes.store import router as StoreRouter
from routes.category import router as CategoryRouter
from routes.product import router as ProductRouter
from routes.sidebar import router as SidebarRouter
from routes.path import router as PathRouter
# from routes.custom import router as CustomRouter
# from routes.topbar import router as TopBarRouter
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

app = FastAPI()

token_listener = JWTBearer()

print(config('FRONTEND_URL'))

origins = [
    config('FRONTEND_URL')
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    # allow_methods=['POST', 'GET'],
    allow_methods=['*'],
    # allow_headers=['Set-Cookie', 'Content-Type', Authorization]
    allow_headers=['*']
)

@app.on_event("startup")
async def start_database():
    await initiate_database()


app.include_router(AdminRouter, tags=["Administrator"], prefix="/auth")
app.include_router(UserRouter, tags=["Users"], prefix="/user", dependencies=[Depends(token_listener)],)
app.include_router(RoleRouter, tags=["Roles"], prefix="/role", dependencies=[Depends(token_listener)],)
app.include_router(PermissionRouter, tags=["Permissions"], prefix="/permission", dependencies=[Depends(token_listener)],)
app.include_router(CompanyRouter, tags=["Companys"], prefix="/company", dependencies=[Depends(token_listener)],)
app.include_router(StoreRouter, tags=["Stores"], prefix="/store", dependencies=[Depends(token_listener)],)
app.include_router(CategoryRouter, tags=["Categories"], prefix="/category", dependencies=[Depends(token_listener)],)
app.include_router(ProductRouter, tags=["Products"], prefix="/product", dependencies=[Depends(token_listener)],)
app.include_router(SidebarRouter, tags=["Sidebar"], prefix="/sidebar", dependencies=[Depends(token_listener)],)
# app.include_router(CustomRouter, tags=["Custom"], prefix="/custom", dependencies=[Depends(token_listener)],)
app.include_router(PathRouter, tags=["Paths"], prefix="/path", dependencies=[Depends(token_listener)],)
# app.include_router(TopBarRouter, tags=["topbar"], prefix="/topbar", dependencies=[Depends(token_listener)],)
