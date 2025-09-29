from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from ..models.customer import Customer
from uuid import UUID

def create(db: Session, c: Customer) -> Customer:
    db.add(c)
    db.commit()
    db.refresh(c)
    return c

def exists_email(db: Session, email: str) -> bool:
    stmt = select(func.count()).select_from(Customer).where(func.lower(Customer.email) == email.lower())
    return db.execute(stmt).scalar_one() > 0

def get_by_id(db: Session, id_: UUID) -> Optional[Customer]:
    return db.get(Customer, id_)

def list_all(db: Session) -> List[Customer]:
    stmt = select(Customer).order_by(Customer.created_at.desc())
    return db.execute(stmt).scalars().all()

def search_by_name(db: Session, name_substring: str) -> List[Customer]:
    stmt = (
        select(Customer)
        .where(func.lower(Customer.nome).like(f"%{name_substring.lower()}%"))
        .order_by(Customer.created_at.desc())
    )
    return db.execute(stmt).scalars().all()
