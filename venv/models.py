# app/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
# from database import Base
from pydantic import BaseModel
from datetime import datetime  # test done 
from app.database import Base
# from app.database import Base 
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    tasks = relationship("Task", back_populates="owner")
    tenants = relationship("Tenant", back_populates="owner")

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="tasks")

class Tenant(Base):
    __tablename__ = "tenants"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    business_legal_name = Column(String)
    business_website = Column(String)
    business_phone_no = Column(String)
    business_email = Column(String)
    created_at = Column(Date, default=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="tenants")

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class TaskCreate(BaseModel):
    title: str
    description: str

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    owner_id: int


    class Config:
        orm_mode = True

class TenantCreate(BaseModel):
    name: str
    business_legal_name: str
    business_website: str
    business_phone_no: str
    business_email: str

class TenantResponse(BaseModel):
    id: int
    name: str
    business_legal_name: str
    business_website: str
    business_phone_no: str
    business_email: str
    created_at: datetime
    owner_id: int

    class Config:
        orm_mode = True