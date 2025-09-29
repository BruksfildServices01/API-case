from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List, Optional

from app.db import get_db
from app.schemas.customer import CustomerCreate, CustomerRead
from app.services.customer import (         # << AQUI!
    create_customer,
    list_customers,
    get_customer,
)
from app.exceptions import ConflictError, NotFoundError  # << AQUI!

router = APIRouter(prefix="/clientes", tags=["clientes"])


@router.post("", response_model=CustomerRead, status_code=status.HTTP_201_CREATED)
def create_endpoint(payload: CustomerCreate, db: Session = Depends(get_db)):
    try:
        return create_customer(db, payload)
    except ConflictError as e:
        from fastapi import HTTPException
        raise HTTPException(status_code=409, detail=str(e))

@router.get("", response_model=List[CustomerRead])
def list_endpoint(nome: Optional[str] = None, db: Session = Depends(get_db)):
    return list_customers(db, nome)

@router.get("/{id_}", response_model=CustomerRead)
def get_endpoint(id_: UUID, db: Session = Depends(get_db)):
    try:
        return get_customer(db, id_)
    except NotFoundError as e:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail=str(e))
