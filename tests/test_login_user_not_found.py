"""Testing Login Routes"""
from flask import url_for


def test_user_login_user_not_found(client):
    with client:
        response = client.post("/registration", data={
            "email": "steve@steve.com",
            "password": "testtest",
            "confirm": "testtest",
        }, follow_redirects=True)

        assert response.request.path == url_for('authentication.login')
        assert response.status_code == 200
        response = client.post("/login", data={
            "email": "steve@steve.bad",
            "password": "testtes",
        }, follow_redirects=True)
        assert response.request.path == url_for('authentication.login')
        assert response.status_code == 200
        assert b"User Not Found" in response.data
