from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models import models
from app.security import oauth2
from app.utils import utils

router = APIRouter(tags=['Authentication'])


@router.post("/login")
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Invalid credentials")
    if not utils.verify_password(user_credentials.password, user.password):
        raise HTTPException( status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Invalid credentials")

    # create a token
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
