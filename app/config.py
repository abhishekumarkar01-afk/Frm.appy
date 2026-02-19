import os

class Settings:
    PROJECT_NAME = "Agro AI"
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:password@db:5432/agro_ai"
    )

settings = Settings()
