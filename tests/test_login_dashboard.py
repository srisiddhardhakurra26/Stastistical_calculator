"""Testing Login Routes"""
from flask import url_for


def test_user_login_dashboard(client, login):
    with client:
        response = client.get("/dashboard", follow_redirects=True)
        assert response.request.path == url_for('authentication.dashboard')
        assert response.status_code == 200
        assert b"steve@steve.com" in response.data
