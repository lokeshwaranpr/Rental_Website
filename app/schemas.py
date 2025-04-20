from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field


class Post(BaseModel):
    title: str
    description: str
    price: float
    category: str
    rental_rate: Optional[float] = None
    condition: str
    image_url: Optional[str] = None
    location: str