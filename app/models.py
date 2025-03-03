from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    isActive = Column(Boolean, default=True)
