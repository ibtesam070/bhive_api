from fastapi import FastAPI
from .routes.root_route import router as root_router
from .routes.auth_route import router as auth_router
from .routes.fund_route import router as fund_router

app = FastAPI()

app.include_router(root_router)
app.include_router(auth_router)
app.include_router(fund_router)
