from app.core.ml_engine import CropModel

model = CropModel()

async def analyze_crop(file):
    image = await file.read()
    prediction = model.predict(image)
    return prediction
