from fastapi import APIRouter
from app.services.soil_analysis import analyze_soil

router = APIRouter()

@router.post("/analyze")
def soil_analysis(payload: dict):
    return analyze_soil(payload)
