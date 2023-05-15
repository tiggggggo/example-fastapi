from typing import Optional

from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models import models
from app.schemas import schemas
from app.schemas.schemas import PostWithVotes
from app.security import oauth2

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@router.get("/", response_model=list[schemas.Post])
def get_posts(db: Session = Depends(get_db),
              current_user: schemas.UserRead = Depends(oauth2.get_current_user),
              skip: int = 0,
              limit: int = 10,
              search: Optional[str] = None):
    # # if want to fetch just current user posts
    # posts = db.query(models.Post).filter(models.Post.user_id == current_user.id).all()
    posts_query = db.query(models.Post)
    if search:
        posts_query = posts_query.filter(models.Post.title.contains(search))
    posts = posts_query.offset(skip).limit(limit).all()
    return posts


@router.get("/votes", response_model=list[PostWithVotes])
def get_posts(db: Session = Depends(get_db),
              current_user: schemas.UserRead = Depends(oauth2.get_current_user),
              skip: int = 0,
              limit: int = 10,
              search: Optional[str] = None):
    posts_query = db.query(models.Post, func.count(models.Vote.post_id).label("votes")) \
        .join(models.Vote, isouter=True) \
        .group_by(models.Post.id)
    if search:
        posts_query = posts_query.filter(models.Post.title.contains(search))
    posts = posts_query.offset(skip).limit(limit).all()
    return posts


@router.get("/{id}", response_model=schemas.Post)
def get_post(id: int,
             db: Session = Depends(get_db),
             current_user: schemas.UserRead = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id={id} not found")
    # # get just current user post
    # if post.user_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
    #                         detail="Not authorized to perform requested action")
    return post


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db),
                 current_user: schemas.UserRead = Depends(oauth2.get_current_user)):
    new_post = models.Post(user_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db),
                current_user: schemas.UserRead = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id={id} not found")
    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    db.delete(post)
    db.commit()


@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, post: schemas.PostUpdate, db: Session = Depends(get_db),
                current_user: schemas.UserRead = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    updated_post = post_query.first()
    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id={id} not found")
    if updated_post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    post_query.update(post.dict())
    db.commit()
    db.refresh(updated_post)
    return updated_post
