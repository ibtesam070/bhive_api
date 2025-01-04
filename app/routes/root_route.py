from fastapi import APIRouter
from ..controllers.root_controller import RootController

router = APIRouter()

@router.get("/")
def health_check():
    return RootController.health_check()