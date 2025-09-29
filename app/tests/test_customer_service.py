from app.schemas.customer import CustomerCreate
from app.services.customer import create_customer, get_customer, list_customers
from app.repositories.customer_repo import exists_email

def test_service_create_and_list(db_session, monkeypatch):
    def fake_exists(db, email): return False
    monkeypatch.setattr("app.repositories.customer_repo.exists_email", fake_exists)
    payload = CustomerCreate(nome="Ana", email="ana@ex.com", telefone=None)
    created = create_customer(db_session, payload)
    assert created.email == "ana@ex.com"
    items = list_customers(db_session, None)
    assert any(i.email == "ana@ex.com" for i in items)
