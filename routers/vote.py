from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models import models
from app.schemas import schemas
from app.security import oauth2

router = APIRouter(
    prefix="/votes",
    tags=["Votes"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote,
         db: Session = Depends(get_db),
         current_user: schemas.UserRead = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id={vote.post_id} not found")

    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id,
                                              models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()
    if vote.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"{current_user.id} user has already voted on post {vote.post_id}")
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "Successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"{current_user.id} user has not voted on post {vote.post_id}")
        vote_query.delete(synchronize_session="fetch")
        db.commit()
        return {"message": "Successfully deleted vote"}
