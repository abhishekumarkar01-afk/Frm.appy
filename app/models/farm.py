from sqlalchemy import Column, Integer, Float, ForeignKey
from app.database import Base

class Farm(Base):
    __tablename__ = "farms"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    area_acres = Column(Float)
    irrigation = Column(Integer)
