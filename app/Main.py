from fastapi import FastAPI
from app.api.v1.router import api_router

app = FastAPI(
    title="Agro AI Infrastructure",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def health_check():
    return {"status": "Agro AI running"}
