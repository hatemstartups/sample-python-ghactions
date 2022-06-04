from fastapi.testclient import TestClient

import app.main

client = TestClient(app.main.service)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
