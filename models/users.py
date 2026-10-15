from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event

class User(BaseModel):
    email: EmailStr
    password: str
    username: str
    events: Optional[List[Event]] = []

    class Config:
        json_schema_extra = {
            "example": {
                "email": "vlad.ignatchenko@example.com",
                "password": "Vlad123!",
                "username": "Игнатченко Владислав",
                "events": []
            }
        }

class NewUser(User):
    pass

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "vlad.ignatchenko@example.com",
                "password": "VladStrong123!"
            }
        }