from sqlalchemy.orm import Session
from typing import List, Optional
from . import models, schemas

# Create Product
def create_product(db: Session, product: schemas.ProductCreate) -> models.Product:
    db_product = models.Product(name=product.name, price=product.price, isActive=product.isActive)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Get Product by ID
def get_product(db: Session, product_id: int) -> Optional[models.Product]:
    return db.query(models.Product).filter(models.Product.id == product_id).first()

# Get All Products
def get_products(db: Session, skip: int = 0, limit: int = 10) -> List[models.Product]:
    return db.query(models.Product).offset(skip).limit(limit).all()

# Update Product
def update_product(db: Session, product_id: int, product: schemas.ProductBase) -> Optional[models.Product]:
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product:
        db_product.name = product.name
        db_product.price = product.price
        db_product.isActive = product.isActive
        db.commit()
        db.refresh(db_product)
    return db_product

# Delete Product
def delete_product(db: Session, product_id: int) -> Optional[models.Product]:
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product
