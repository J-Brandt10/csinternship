import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_homepage_status(client):
    response = client.get("/")
    assert response.status_code == 200


def test_homepage_content(client):
    response = client.get("/")
    assert b"CS Internship Tools - Welcome Jack!" in response.data
