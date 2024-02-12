"""Testing Registration Routes"""
from flask import url_for

from application import db
from application.database import User


def test_user_registration_success(client):
    with client:
        response = client.post("/registration", data={
            "email": "steve@steve.com",
            "password": "testtest",
            "confirm": "testtest",
        }, follow_redirects=True)

        assert response.request.path == url_for('authentication.login')
        assert response.status_code == 200


