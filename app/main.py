from fastapi import FastAPI
from app.utils.logging import setup_logging
from app.db import Base, engine
from app.routers.customers import router as customers_router  # << AQUI!

def create_app() -> FastAPI:
    setup_logging()
    app = FastAPI(title="Customers API", version="1.0.0")
    app.include_router(customers_router)  # << AQUI!
    return app

app = create_app()
Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"ok": True}
