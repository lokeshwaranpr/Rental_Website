from typing import Optional
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session



models.Base.metadata.create_all(bind=engine)

app = FastAPI()



class Item(BaseModel):
    title: str
    description: str
    price: float
    category: str
    rental_rate: Optional[float] = None
    condition: str
    image_url: Optional[str] = None
    location: str
    available: bool

while True:

    try:
        conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="password", cursor_factory= RealDictCursor)
        cursor = conn.cursor()
        print("Database connection successful")
        break
    except Exception as e:
        print("Database Connection failed")
        print("Error",e)
        time.sleep(2)


@app.get("/")
def root():
    return {"message":"hello world"}

@app.post("/createpost")
def create_item(item : Item):
    cursor.execute("INSERT INTO item (title, description, price) VALUES (%s, %s, %s )", (item.title, item.description, item.price))
    conn.commit()
    return {"Message":"Successfully Created "}

@app.get("/getposts")
def get_item():
    cursor.execute("SELECT * FROM item")
    items = cursor.fetchall()
    return {"posts":items}

@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    return {"data": "Success"}