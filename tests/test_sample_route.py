"""Testing Sample Calculation """
from flask import url_for
from flask_login import current_user

from application.database import User, SampleCalc


def test_sample_calc_route(app, client, login):
    with app.app_context():
        assert SampleCalc.record_count() == 0

    with client:
        response = client.post("/sample_size", data={
            "z_score": "2.58",
            "margin_error": ".05",
            "std": ".5",
            "population_size": "425"
        }, follow_redirects=True)
        with app.app_context():
            assert SampleCalc.record_count() == 1

        assert response.status_code == 200
        assert response.request.path == url_for('sample_size.my_sample_calcs')
        assert b"259.39" in response.data
