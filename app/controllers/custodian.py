import logging
from flask_login import login_user, logout_user

from app import db, login_manager, cache
from ..models.user import User
from ..blockchain.custodian import Custodian

@login_manager.user_loader
def load_user(username):
    return User.query.filter(User.username == username).first()

class CustodianController:
    def __init__(self):
        self.blockchain = Custodian()

    def approve_reimbursement(self):
        pass

    