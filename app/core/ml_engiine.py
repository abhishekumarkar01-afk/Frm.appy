import numpy as np

class CropModel:

    def __init__(self):
        self.model = None  # Replace with real model later

    def preprocess(self, image_bytes):
        return np.random.rand(1, 224, 224, 3)

    def predict(self, image_bytes):
        data = self.preprocess(image_bytes)
        return {
            "disease": "Healthy",
            "confidence": 0.91
        }
