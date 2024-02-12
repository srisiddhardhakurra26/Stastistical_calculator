from faker import Faker

from application.database import User, db


def test_index_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"IS 601" in response.data

