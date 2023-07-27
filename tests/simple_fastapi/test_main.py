import pytest
from fastapi.testclient import TestClient

from src.simple_fastapi.main import app


@pytest.fixture
def test_client():
    client = TestClient(app)
    return client


def test_hello(test_client: TestClient):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json().startswith("Hello, World!")
