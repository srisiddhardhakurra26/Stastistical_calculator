"""Testing Sample Calculation """
from flask import url_for
from flask_login import current_user

from application.database import User, SampleCalc


def test_menu_calculate_sample_unauthenticated(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Calculate Sample" in response.data


