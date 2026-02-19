from fastapi import APIRouter, UploadFile, File
from app.services.crop_analysis import analyze_crop_image

router = APIRouter()

@router.post("/analyze")
async def analyze_crop(file: UploadFile = File(...)):
    result = await analyze_crop_image(file)
    return result
