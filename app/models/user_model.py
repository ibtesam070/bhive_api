from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# DTO for authentication of user
class UserAuth(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)


# User Table
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
