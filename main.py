from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


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

@app.get("/")
def root():
    return {"message":"HelloWorld"}

@app.post("/createpost")
def create_item():
    return {"Message":"Post created successfully"}