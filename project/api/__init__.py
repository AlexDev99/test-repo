from fastapi import APIRouter

from .main_router import router as oper_router

router = APIRouter()
router.include_router(oper_router)
