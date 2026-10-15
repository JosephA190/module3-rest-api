import pytest
from fastapi.testclient import TestClient
from app.main import create_app

@pytest.fixture
def client():
    with TestClient(create_app()) as test_client:
        yield test_client

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
