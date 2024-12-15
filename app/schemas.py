from pydantic import BaseModel

# Base Schema
class ProductBase(BaseModel):
    name: str
    price: int
    isActive: bool = True

# Schema สำหรับการสร้าง
class ProductCreate(ProductBase):
    pass

# Schema สำหรับการตอบกลับ
class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True
