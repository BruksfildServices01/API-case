from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import datetime
from uuid import UUID

class CustomerCreate(BaseModel):
    nome: str = Field(..., min_length=1, max_length=255)
    email: EmailStr = Field(..., max_length=255)
    telefone: Optional[str] = Field(None, max_length=30)

class CustomerRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    nome: str
    email: EmailStr
    telefone: Optional[str] = None
    created_at: datetime
