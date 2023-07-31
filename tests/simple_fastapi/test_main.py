from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from src.simple_fastapi.main import app


@pytest.fixture()
def test_client():
    return TestClient(app)


def test_hello(test_client: TestClient):
    response = test_client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json().startswith("Hello, World!")
