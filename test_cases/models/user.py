import os
import unittest
import tempfile
import app

from app.models.user import User


class TestGratitudeDatabaseController(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        self.app = app.app.test_client()
        app.db.create_all()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])

    def test_user_model(self):
        username = "test"
        password = "password"
        role = "customer"

        user = User(username, password, role)

        # Checking customer data
        assert user.username == username
        assert user.role == role
        # Checking if password is encrypted
        assert user._password != password
        assert user.is_password_correct(password)

        # Adding to database
        app.db.session.add(user)
        app.db.session.commit()

        u = User.query.filter(User.username == username).first()
        assert u is user
