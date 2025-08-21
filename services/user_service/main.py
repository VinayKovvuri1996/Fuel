
from fastapi import FastAPI
from app.routes import router as user_router
from app.database import Base, engine
from app.models import User

app = FastAPI(title="FuelForce - User Service")

# Include user routes
app.include_router(user_router, prefix="/users", tags=["users"])

@app.get("/")
def root():
    return{"message": "User service is running"}

#This creates tables only if they don't exit
Base.metadata.create_all(bind=engine)