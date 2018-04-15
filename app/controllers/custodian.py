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
    def approve_reimbursement(self):
        pass


custodian_controller = CustodianController()
