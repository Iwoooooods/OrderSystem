from typing import Optional, Any
from fastapi import Form
from pydantic import BaseModel

class UserBase(BaseModel):
    user_name: str

class UserCreate(UserBase):
    password: str

class UserQuery(UserBase):
    id: int
    is_active: bool = False

class LoginForm(BaseModel):
    user_name: str = Form(...)
    password: str = Form(...)