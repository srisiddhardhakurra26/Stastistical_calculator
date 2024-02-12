"""Testing Sample Calculation """
from flask import url_for
from flask_login import current_user

from application.database import User, SampleCalc


def test_sample_calc_model(app, create_5_users):
    with app.app_context():
        assert SampleCalc.record_count() == 0
        sample_calc = SampleCalc(z_score=2.58, margin_error=.05, std=.5, population_size=425)
        assert sample_calc.calc_sample_size == 259.39
        user = User.get_random_record()
        user.sample_calcs.append(sample_calc)
        user.save()
        assert SampleCalc.record_count() == 1