from fastapi import APIRouter, UploadFile, File
from app.services.crop_service import analyze_crop

router = APIRouter()

@router.post("/analyze")
async def crop_analysis(file: UploadFile = File(...)):
    return await analyze_crop(file)
