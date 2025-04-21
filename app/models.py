from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from .database import Base, engine
from sqlalchemy.sql.sqltypes import TIMESTAMP

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
    available = Column(Boolean, index=True, server_default='True', default=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    email = Column(String, primary_key=True, index=True, nullable=False, unique=True)
    password = Column(String, index=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))