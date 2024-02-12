"""Testing User Profile """
from flask_login import current_user

from application.database import User, db, Profile


def test_user_profile_post_controller(app, client, login):
    with app.app_context():
        assert Profile.record_count() == 0
    with client:
        response = client.post("/profile", data={
            "first_name": "Steve",
            "last_name": "Steve",
            "phone": "5555555",
        }, follow_redirects=True)
        assert response.status_code == 200

    with app.app_context():
        assert Profile.record_count() == 1
