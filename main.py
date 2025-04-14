from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time




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
    return {"message":"HelloWorld"}

@app.post("/createpost")
def create_item():
    return {"Message":"Post created successfully"}

@app.get("/getposts")
def get_item():
    cursor.execute("SELECT * FROM item")
    items = cursor.fetchall()
    return {"posts":items}