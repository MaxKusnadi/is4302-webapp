import logging
from flask_login import login_user, logout_user

from app import db, login_manager, cache
from ..models.user import User
from ..blockchain.customer import customer

@login_manager.user_loader
def load_user(username):
    return User.query.filter(User.username == username).first()

class CustomerController:

    def get_own_data(self, username):
        try:
            return customer.get_own_data(username)
        except ValueError:
            raise AttributeError("Can't retrieve own data from blockchain")

    def get_policy_appl(self, applyid):
        try:
            return customer.get_policy_appl(applyid)
        except ValueError:
            raise AttributeError("Can't retrieve policy application from blockchain")

    def file_claim(self, policyid, username, claimdesc):
        try:
            return customer.file_claim(policyid, username, claimdesc)
        except ValueError:
            raise AttributeError("Can't file claim in blockchain")

    def submit_premium_payment(self, policyid, username):
        try:
            return customer.submit_premium_payment(policyid, username)
        except ValueError:
            raise AttributeError("Can't submit premium payment in blockchain")

customer_controller = CustomerController()
