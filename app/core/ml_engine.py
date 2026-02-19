import numpy as np

class CropModel:
    def __init__(self):
        # Placeholder for real ML model
        self.model = None

    def preprocess(self, image_bytes):
        # Convert image bytes to array
        return np.random.rand(1, 224, 224, 3)

    def predict(self, image_bytes):
        data = self.preprocess(image_bytes)
        # Dummy prediction
        return "Healthy"
