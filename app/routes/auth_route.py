from fastapi import APIRouter,HTTPException
from ..controllers.auth_controller import AuthController
from ..models.user_model import UserAuth
from fastapi import Depends
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter(prefix="/auth")


@router.post("/signup")
def login(user: UserAuth, db: Session = Depends(get_db)):
    result = AuthController.signup(user.email, user.password, db)
    if not result["success"]:
        raise HTTPException(status_code=403,  detail=result['data'])
    return result


@router.post("/login")
def signup(user: UserAuth, db: Session = Depends(get_db)):
    result = AuthController.login(user.email, user.password, db)
    if not result["success"]:
        raise HTTPException(status_code=403, detail=result['data'])
    return result
