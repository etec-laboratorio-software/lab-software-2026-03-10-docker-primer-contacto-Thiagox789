# backend/app/database/db.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Configuración de la URL de la base de datos.
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# `connect_args` es necesario únicamente para SQLite.
if SQLALCHEMY_DATABASE_URL and SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

# `sessionmaker` es una clase que nos permite crear sesiones de base de datos.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# `declarative_base` nos permite crear modelos ORM.
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
