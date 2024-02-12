from faker import Faker

from application.database import User, db


def test_index_route(client):
    response = client.get("/about")
    assert response.status_code == 200
    assert b"about me" in response.data


