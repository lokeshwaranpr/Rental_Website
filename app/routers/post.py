from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import oauth2
from .. import models, schemas
from ..database import get_db



router = APIRouter(
    prefix="/posts",
    tags=["Posts"]

)




@router.post("/create",status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_item(post: schemas.PostCreate, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    new_post=models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    posts=db.query(models.Post).all()
    return posts


@router.get("/{id}",response_model=schemas.Post)
def get_post(id:int, db: Session = Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id==id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, db: Session = Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id==id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    post.delete(synchronize_session=False)
    db.commit()
    return {"message":"Post deleted successfully"}

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.Post)
def update_post(id:int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    post_query=db.query(models.Post).filter(models.Post.id==id)
    if not post_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    return {"message":"Post updated successfully"}