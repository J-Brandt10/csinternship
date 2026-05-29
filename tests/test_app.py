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


def test_calculator_status(client):
    response = client.get("/calculator")
    assert response.status_code == 200


def test_calculator_content(client):
    response = client.get("/calculator")
    assert b"Calculator" in response.data
    assert b"clearAll" in response.data
    assert b"calculate" in response.data


def test_hello_mother_status(client):
    response = client.get("/hello-mother")
    assert response.status_code == 200


def test_hello_mother_content(client):
    response = client.get("/hello-mother")
    assert b"Hello Mother" in response.data
    assert b"Pacifico" in response.data
    assert b"rainbow" in response.data
