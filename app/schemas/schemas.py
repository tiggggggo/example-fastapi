from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


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


# POST
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    published: bool


class Post(PostBase):
    id: int
    created_at: datetime
    user: UserRead

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


# Vote
class Vote(BaseModel):
    post_id: int
    dir: int = Field(ge=0, le=1)


# POST WITH VOTE

class PostWithVotes(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True