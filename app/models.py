from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base, engine

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=False)
    price = Column(Integer, index=True, nullable=False)
    category = Column(String, index=True, nullable=False)
    rental_rate = Column(Integer, index=True, nullable=False)
    condition = Column(String, index=True, nullable=False)
    image_url = Column(String, index=True, nullable=False)
    location = Column(String, index=True, nullable=False)
    available = Column(String, index=True, default= True)
