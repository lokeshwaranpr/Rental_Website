from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class PostBase(BaseModel):
    title: str
    description: str
    price: float
    category: str
    rental_rate: Optional[float] = None
    condition: str
    image_url: Optional[str] = None
    location: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    available: bool = True
    created_at: datetime

    class Config:
        from_attributes = True
