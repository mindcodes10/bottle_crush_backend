# schemas.py
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Annotated
from fastapi import FastAPI, File, UploadFile

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserCreate(BaseModel):
    email: str
    password: str
    role: str  # Role is required in registration
    is_active: bool = True
    is_deleted: bool = False
    created_by: int
    updated_by: int
    created_at: datetime = datetime.utcnow()  # Default to current timestamp
    updated_at: datetime = datetime.utcnow()  # Default to current timestamp

    class Config:
        orm_mode = True


class BusinessCreate(BaseModel):
    name: str
    mobile: str
    logo_image: Annotated[UploadFile, File()]
    business_owner: int
    created_by: int
    updated_by: int
    created_at: datetime = datetime.utcnow()  # Default to current timestamp
    updated_at: datetime = datetime.utcnow()  # Default to current timestamp
    is_active: bool = True
    is_deleted: bool = False

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True  # Allow arbitrary types like bytearray

class MachineCreate(BaseModel):
    name: str
    number: str
    street: str
    city: str
    state: str
    pin_code: str
    business_id: int

    class Config:
        orm_mode = True

# Pydantic schema for creating a new bottle entry
class BottleCreate(BaseModel):
    machine_id: int
    bottle_count: int
    bottle_weight: float
    is_deleted: bool = False

    class Config:
        orm_mode = True


class ForgotPasswordRequest(BaseModel):
    email: str

class VerifyOtpRequest(BaseModel):
    email: str
    otp: str

class ResetPasswordRequest(BaseModel):
    reset_token: str
    new_password: str

class BusinessUpdate(BaseModel):
    name: str = Field(..., max_length=100, example="Updated Business Name")
    mobile: str = Field(..., pattern="^[0-9]{10}$", example="9876543210")
      
class MachinesPerBusiness(BaseModel):
    id: int
    name: str
    number: str
    street: str
    city: str
    state: str
    pin_code: str
    