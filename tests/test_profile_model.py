"""Testing User Profile """
from flask_login import current_user

from application.database import User, db, Profile


def test_user_profile_model(app, create_5_users):
    with app.app_context():
        assert Profile.record_count() == 0
        user = User.find_by_id(1)
        profile = Profile("Steve", "Steve", "5555555")
        user.profile = profile
        user.save()
        assert Profile.record_count() == 1
        assert user.profile.first_name == "Steve"
        assert user.profile.last_name == "Steve"
        assert user.profile.phone == "5555555"