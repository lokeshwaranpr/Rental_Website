from typing import Optional,List
from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models,schemas,utils
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext



models.Base.metadata.create_all(bind=engine)

app = FastAPI()




while True:
    try:
        conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="password", cursor_factory=RealDictCursor)
        print("Database connection successful")
        break
    except Exception as e:
        print("Database connection failed")
        print("Error:", e)
        time.sleep(2)
   


@app.get("/")
def root():
    return {"message":"hello world"}


@app.post("/createpost",status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_item(post: schemas.PostCreate, db: Session = Depends(get_db)):
    new_post=models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@app.get("/getposts", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    posts=db.query(models.Post).all()
    return posts


@app.get("/getpost/{id}",response_model=schemas.Post)
def get_post(id:int, db: Session = Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id==id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post


@app.delete("/deletepost/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, db: Session = Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id==id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    post.delete(synchronize_session=False)
    db.commit()
    return {"message":"Post deleted successfully"}

@app.put("/updatepost/{id}", status_code=status.HTTP_200_OK, response_model=schemas.Post)
def update_post(id:int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    post_query=db.query(models.Post).filter(models.Post.id==id)
    if not post_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    return {"message":"Post updated successfully"}


@app.post("/createuser", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Hash the password 
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user=models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user