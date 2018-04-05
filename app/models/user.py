from flask_login import UserMixin

from app import db, bcrypt
from sqlalchemy import Column, String, Integer, Boolean


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True)
    _password = Column(String(128))
    is_verified = Column(Boolean)
    role = Column(String)

    def __init__(self, username, password, role):
        self.role = role
        self.username = username
        self._password = bcrypt.generate_password_hash(password)
        self.is_verified = False

    def is_active(self):
        return True

    def get_id(self):
        return self.username

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def is_password_correct(self, password):
        return bcrypt.check_password_hash(self._password, password)

    def __repr__(self):  # pragma: no cover
        return "<{id}> Username: {user}".format(
            id=self.id,
            user=self.username
        )
