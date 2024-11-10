from fastapi import APIRouter
from scrap.router import router as scrap_router


api_router = APIRouter()

api_router.include_router(scrap_router,
                          prefix='/scrap_football_data')