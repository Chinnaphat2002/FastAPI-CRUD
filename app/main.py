from fastapi import FastAPI
from .database import engine, Base
from .routers import products

# สร้างตารางในฐานข้อมูล
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product CRUD API")

# รวม Router
app.include_router(products.router, prefix="/products", tags=["Products"])
