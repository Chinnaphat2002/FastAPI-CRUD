from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

# Dependency
get_db = database.get_db

# Create Product
@router.post("/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

# Get Product by ID
@router.get("/{product_id}", response_model=schemas.ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db=db, product_id=product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

# Get All Products
@router.get("/", response_model=list[schemas.ProductResponse])
def get_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_products(db=db, skip=skip, limit=limit)

# Update Product
@router.put("/{product_id}", response_model=schemas.ProductResponse)
def update_product(product_id: int, product: schemas.ProductBase, db: Session = Depends(get_db)):
    updated_product = crud.update_product(db=db, product_id=product_id, product=product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

# Delete Product
@router.delete("/{product_id}", response_model=schemas.ProductResponse)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted_product = crud.delete_product(db=db, product_id=product_id)
    if not deleted_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return deleted_product
