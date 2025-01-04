from fastapi import APIRouter, Depends, Query, HTTPException
from ..controllers.fund_controller import FundController
from ..utils.jwt_check import get_current_user

router = APIRouter(prefix="/fund")


@router.get("/schemes")
def get_schemes(
    fund_family: str = Query("fund_family"), _: dict = Depends(get_current_user)
):
    result = FundController.get_schemes(fund_family)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["data"])
    return result
