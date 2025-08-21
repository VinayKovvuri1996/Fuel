from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    role: str   #owner, accountant, staff

class UserLogin(BaseModel):
    username: str
    password: str
    role: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"