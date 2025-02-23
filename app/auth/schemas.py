from typing import Optional
from sqlmodel import SQLModel, Field

class UserCreate(SQLModel):
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    first_name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)
    password: str
    class Config:
        extra = "forbid"

class User(SQLModel):
    id: int
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    first_name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)
    is_verified: bool = Field(default=False)
    password_hash: str
    class Config:
        extra = "forbid"

class UserResponse(SQLModel):
    id: int
    username: str
    email: str
    first_name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)
    is_verified: bool = Field(default=False)
    class Config:
        extra = "forbid"
        
class Token(SQLModel):
    access_token: str
    token_type: str
    refresh_token: str
    
class TokenData(SQLModel):
    username: Optional[str] = None