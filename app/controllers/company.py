import logging
from flask_login import login_user, logout_user

from app import db, login_manager, cache
from ..models.user import User
from ..blockchain.company import Company

@login_manager.user_loader
def load_user(username):
    return User.query.filter(User.username == username).first()

class CompanyController:
    def __init__(self):
        self.blockchain = Company()

    def get_all_policy_appl(self):
        logging.info("Retrieving All Policy Applications")
        try:
            return self.blockchain.get_all_policy_appl()
        except ValueError:
            raise AttributeError("Can't retrieve from the blockchain")

    def register_cust_policy(self, applyID):
        logging.info("Registering Customer's Policy")
        try:
            return self.blockchain.register_customer_policy(applyID)
        except ValueError:
            raise AttributeError("Can't register policy application in blockchain")

    def reject_policy_appl(self, applyID):
        logging.info("Rejecting Customer's Policy Application")
        try:
            return self.blockchain.reject_policy_appl(applyID)
        except ValueError:
            raise AttributeError("Can't reject policy application in blockchain")

    def get_all_claim(self):
        logging.info("Retrieving All Claims")
        try:
            return self.blockchain.get_all_claim()
        except ValueError:
            raise AttributeError("Can't retrieve from the blockchain")

    def approve_claim(self, claimID):
        logging.info("Approve Claim")
        try:
            return self.blockchain.approve_claim(claimID)
        except ValueError:
            raise AttributeError("Can't approve claim in blockchain")

    def reject_claim(self, claimID):
        logging.info("Reject Claim")
        try:
            return self.blockchain.reject_claim(claimID)
        except ValueError:
            raise AttributeError("Can't reject claim in blockchain")

    def submit_reimb(self, claimID, reimbType):
        logging.info("Submit Reimbursement")
        try:
            return self.blockchain.submit_reimbursement(claimID, reimbType)
        except ValueError:
            raise AttributeError("Can't submit reimbursement in blockchain")