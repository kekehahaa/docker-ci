import pytest

from app import app
from fastapi.testclient import TestClient

@pytest.fixture
def test_home_func():
    return TestClient(app)

class TestHomeEndpoint:
    def test_home(self, client):
        response = client.get("/")
        data = response.json()

        assert response.status_code == 200
        assert data == {"message": "Hello, Docker!"}
        assert response.headers["content-type"] == "application/json"
    