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
from .routers import post, user


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
   

app.include_router(post.router)
app.include_router(user.router)


@app.get("/")
def root():
    return {"message":"hello world"}






