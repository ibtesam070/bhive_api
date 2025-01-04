from fastapi import FastAPI
from dotenv import load_dotenv
import os
import uvicorn
from .routes.root_route import router as root_router
from .routes.auth_route import router as auth_router
from .routes.fund_route import router as fund_router

load_dotenv()

print(f"PORT: {os.getenv('PORT')}")

app = FastAPI()

app.include_router(root_router)
app.include_router(auth_router)
app.include_router(fund_router)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)