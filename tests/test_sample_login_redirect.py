"""Testing Sample Calculation """
from flask import url_for
from flask_login import current_user

from application.database import User, SampleCalc


def test_sample_size_login_redirect_route(client):
    response = client.post("/registration", data={
        "email": "steve@steve.com",
        "password": "testtest",
        "confirm": "testtest",
    }, follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == url_for('authentication.login')
    response = client.get("/sample_size", follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == url_for('authentication.login')
    response = client.get(
        "/login?next=%2Fsample_size",
        follow_redirects=True
    )
    response = client.post(
        "/login?next=%2Fsample_size",
        data=dict(email='steve@steve.com', password='testtest'),
        follow_redirects=True
    )
    assert response.status_code == 200
    assert response.request.path == url_for('sample_size.sample_size_page')
