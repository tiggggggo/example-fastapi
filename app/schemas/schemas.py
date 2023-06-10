from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


# USER
class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# USER LOGIN
class UserLogin(BaseModel):
    email: str
    password: str


# TOKEN
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
