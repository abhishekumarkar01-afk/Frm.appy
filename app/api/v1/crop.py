from fastapi import APIRouter
from app.api.v1 import crop, soil, farm

api_router = APIRouter()
api_router.include_router(crop.router, prefix="/crop", tags=["Crop"])
api_router.include_router(soil.router, prefix="/soil", tags=["Soil"])
api_router.include_router(farm.router, prefix="/farm", tags=["Farm"])
