import logging
from flask_login import login_user, logout_user

from app import db, login_manager, cache
from ..models.user import User
from ..blockchain.customer import Customer

@login_manager.user_loader
def load_user(username):
    return User.query.filter(User.username == username).first()

class CustomerController:
    def __init__(self):
        self.blockchain = Customer()

    def file_claim(self, username, claimDesc):
        try:
            result = self.blockchain.file_claim(username, claimDesc)
        except ValueError:
            raise AttributeError("Can't file claim in blockchain")
        return result

    def submit_premium_payment(self):
        pass
