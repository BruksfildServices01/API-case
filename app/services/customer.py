from typing import List
from uuid import UUID
from sqlalchemy.orm import Session

from app.schemas.customer import CustomerCreate, CustomerRead
from app.models.customer import Customer
from app.repositories import customer_repo
from app.exceptions import ConflictError, NotFoundError


def create_customer(db: Session, payload: CustomerCreate) -> CustomerRead:
    if customer_repo.exists_email(db, payload.email):
        raise ConflictError("E-mail já cadastrado")
    entity = Customer(nome=payload.nome.strip(), email=payload.email, telefone=payload.telefone)
    entity.normalize()
    saved = customer_repo.create(db, entity)
    return CustomerRead.model_validate(saved)

def list_customers(db: Session, nome: str | None) -> List[CustomerRead]:
    rows = customer_repo.search_by_name(db, nome) if nome else customer_repo.list_all(db)
    return [CustomerRead.model_validate(r) for r in rows]

def get_customer(db: Session, id_: UUID) -> CustomerRead:
    found = customer_repo.get_by_id(db, id_)
    if not found:
        raise NotFoundError("Cliente não encontrado")
    return CustomerRead.model_validate(found)
