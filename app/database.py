from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# โหลดค่าจาก .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# สร้าง Engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class สำหรับ ORM
Base = declarative_base()

# Dependency สำหรับการเชื่อมต่อ DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
