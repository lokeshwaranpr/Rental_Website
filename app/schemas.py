from typing import Optional, List, Union
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


class UserCreate(BaseModel):
    email: EmailStr
    password: str 


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    

class TokenData(BaseModel):
    id: Optional[Union[str,int]] = None