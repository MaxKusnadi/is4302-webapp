import logging
from flask_login import login_user, logout_user

from app import db, login_manager, cache
from ..models.user import User
from ..blockchain.custodian import custodian

@login_manager.user_loader
def load_user(username):
    return User.query.filter(User.username == username).first()

class CustodianController:
    
    def get_pending_reimbursement(self):
        logging.info("Getting pending reimbursement from controller")
        try:
            result = custodian.get_pending_reimbursement()
        except ValueError:
            raise ValueError("Unable to get pending customer reimbursement")
        return result

    def get_reimbursement(self):
        logging.info("Getting all reimbursement from controller")
        try:
            result = custodian.get_reimbursement()
        except ValueError:
            raise ValueError("Unable to get customer reimbursements")
        return result

    def get_pending_cashout(self):
        logging.info("Getting pending cashout from controller")
        try:
            result = custodian.get_pending_cashout()
        except ValueError:
            raise ValueError("Unable to get pending customer cashout")
        return result

    def get_cashout(self):
        logging.info("Getting all cashout from controller")
        try:
            result = custodian.get_cashout()
        except ValueError:
            raise ValueError("Unable to get customer cashout")
        return result

    def approve_reimbursement(self, reimbID):
        logging.info("Approving reimbursement from controller")
        try:
            result = custodian.approve_reimbursement(reimbID)
        except ValueError:
            raise ValueError("Unable to approve reimbursement")
        return result

    def reject_reimbursement(self, reimbID):
        logging.info("Rejecting reimbursement from controller")
        try:
            result = custodian.reject_reimbursement(reimbID)
        except ValueError:
            raise ValueError("Unable to reject reimbursement")
        return result

    def approve_cashout(self, cashoutID):
        logging.info("Approving cashout from controller")
        try:
            result = custodian.approve_cashout(cashoutID)
        except ValueError:
            raise ValueError("Unable to approve cashout")
        return result

    def reject_cashout(self, cashoutID):
        logging.info("Rejecting cashout from controller")
        try:
            result = custodian.reject_cashout(cashoutID)
        except ValueError:
            raise ValueError("Unable to reject cashout")
        return result

    def get_pending_premium(self):
        logging.info("Getting pending premium from controller")
        try:
            result = custodian.get_pending_premium()
        except ValueError:
            raise ValueError("Unable to get pending premium data")
        return result

    def verify_premium(self, premID):
        logging.info("Verifying premium from controller")
        try:
            result = custodian.verify_premium(premID)
        except ValueError:
            raise ValueError("Unable to approve premium")
        return result

    def reject_premium(self, premID):
        logging.info("Rejecting premium from controller")
        try:
            result = custodian.reject_premium(premID)
        except ValueError:
            raise ValueError("Unable to reject premium")
        return result