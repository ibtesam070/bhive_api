from fastapi import APIRouter, Depends, Query
from ..controllers.fund_controller import FundController
from ..utils.jwt_check import get_current_user

router = APIRouter(prefix="/fund")


@router.get("/schemes")
def get_schemes(
    fund_family: str = Query("fund_family"), _: dict = Depends(get_current_user)
):
    return FundController.get_schemes(fund_family)
