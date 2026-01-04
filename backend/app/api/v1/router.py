from fastapi import APIRouter
from app.api.v1 import analysis

router = APIRouter()
router.include_router(analysis.router)
