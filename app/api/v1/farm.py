from fastapi import APIRouter
from app.services.farm_analysis import analyze_farm

router = APIRouter()

@router.post("/analyze")
def farm_analysis(payload: dict):
    return analyze_farm(payload)
