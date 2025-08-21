from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, auth
from app.database import SessionLocal

router = APIRouter()

# Dependency to get DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_username(db, user.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    return crud.create_user(db, user.username, user.password, user.role)

@router.post("/login", response_model=schemas.TokenResponse)
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if not db_user or not auth.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    if user.role != db_user.role:
        raise HTTPException(status_code=403, detail="Role Mismatch")
    
    token = auth.create_access_token({"sub": db_user.username, "role": db_user.role})
    return {"access_token": token}



@router.get("/health")
def health_check():
    return{"status":"User service healthy"}