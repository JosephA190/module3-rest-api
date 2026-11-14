import pytest
import tempfile
import os
from fastapi.testclient import TestClient
from app.main import create_app

@pytest.fixture
def client():
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
        db_path = f.name
    try:
        with TestClient(create_app(db_path=db_path)) as test_client:
            yield test_client
    finally:
        try:
            os.unlink(db_path)
        except OSError:
            pass

def test_greeting_returns_json(client):
    response = client.get("/api/hello")
    assert response.status_code == 200
    assert isinstance(response.json()["message"], str)

def test_valid_post_returns_created_idea(client):
    response = client.post("/api/ideas", json={"title": "Start a coding club", "category": "clubs"})
    assert response.status_code == 201
    assert response.json()["id"] is not None
    assert response.json()["title"] == "Start a coding club"
    assert response.json()["category"] == "clubs"

def test_spaces_only_title_returns_400(client):
    count_before = len(client.get("/api/ideas").json())
    response = client.post("/api/ideas", json={"title": "   ", "category": "clubs"})
    assert response.status_code == 400
    count_after = len(client.get("/api/ideas").json())
    assert count_after == count_before
