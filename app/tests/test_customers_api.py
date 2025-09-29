from uuid import UUID

def test_create_customer_ok(client):
    resp = client.post("/clientes", json={
        "nome": "Maria Silva",
        "email": "maria@exemplo.com",
        "telefone": "11999990000"
    })
    assert resp.status_code == 201
    data = resp.json()
    assert "id" in data and UUID(data["id"])
    assert data["email"] == "maria@exemplo.com"

def test_create_customer_conflict_email(client):
    payload = {"nome":"A","email":"dup@exemplo.com","telefone":None}
    r1 = client.post("/clientes", json=payload)
    assert r1.status_code == 201
    r2 = client.post("/clientes", json=payload)
    assert r2.status_code == 409

def test_list_customers_and_filter(client):
    client.post("/clientes", json={"nome":"Maria Silva","email":"m1@ex.com"})
    client.post("/clientes", json={"nome":"Mariana","email":"m2@ex.com"})
    client.post("/clientes", json={"nome":"João","email":"j@ex.com"})
    all_resp = client.get("/clientes")
    assert all_resp.status_code == 200
    assert len(all_resp.json()) >= 3

    filt = client.get("/clientes?nome=mar")
    assert filt.status_code == 200
    names = [c["nome"].lower() for c in filt.json()]
    assert any("maria" in n or "mariana" in n for n in names)

def test_get_by_id_404(client):
    from uuid import uuid4
    resp = client.get(f"/clientes/{uuid4()}")
    assert resp.status_code == 404
