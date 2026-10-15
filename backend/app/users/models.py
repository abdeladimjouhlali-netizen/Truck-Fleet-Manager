from fastapi_users_db_beanie import BeanieBaseUser
from beanie import Document
from pydantic import BaseModel, Field
from typing import Optional
from fastapi_users import schemas

class User(BeanieBaseUser):
    pass

class UserRead(schemas.BaseUser[str]):
    pass

class UserCreate(schemas.BaseUserCreate):
    pass
