# tests/conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient

from app.db import Base, get_db
from app.main import create_app

# ✅ garante que a tabela 'clientes' está registrada no metadata
from app.models import customer as _customer_model  # noqa: F401  (import só para side-effect)

@pytest.fixture(scope="session")
def test_engine():
    # ✅ usa StaticPool para manter um ÚNICO banco em memória para toda a sessão de testes
    engine = create_engine(
        "sqlite://",  # (sem :memory: aqui)
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    yield engine
    engine.dispose()

@pytest.fixture
def db_session(test_engine):
    TestingSessionLocal = sessionmaker(bind=test_engine, autocommit=False, autoflush=False)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

@pytest.fixture
def client(db_session):
    app = create_app()

    def override_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_db
    return TestClient(app)
