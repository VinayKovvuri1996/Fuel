from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv() #Load from .env if running locally

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://fueladmin:Kodad@2021@@localhost:5432/fuelforce")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

