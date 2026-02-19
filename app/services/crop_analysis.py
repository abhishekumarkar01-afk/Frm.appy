from app.core.ml_engine import CropModel

model = CropModel()

async def analyze_crop_image(file):
    image_bytes = await file.read()
    prediction = model.predict(image_bytes)
    return {
        "disease_prediction": prediction,
        "confidence": 0.92
    }
