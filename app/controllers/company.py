import logging

from app import db
from ..blockchain.company import company
from ..blockchain.customer import customer
from ..models.user import User


class CompanyController:

    def register_policy(self, policy_id, duration):
        logging.info("Registering policy from controller")
        try:
            company.register_policy(policy_id, duration)
        except ValueError:
            raise ValueError("Unable to register policy in blockchain")

        try:
            return company.assign_pool_to_policy(policy_id)
        except ValueError:
            raise AttributeError("Unable to assign money pool to policy")

    def terminate_customer_policy(self, cust_id, policy_id):
        logging.info("Terminating customer policy from controller")
        try:
            return company.terminate_customer_policy(policy_id, cust_id)
        except ValueError:
            raise AttributeError("Can't terminate customer policy from the blockchain")

    def register_customer(self, username, password, salary):
        logging.info("Registering customer {} by company".format(username))
        # Check username exists
        user = User.query.filter(User.username == username).first()
        if user:
            logging.error("Username {} exits".format(username))
            raise ValueError("Username exits")
        try:
            customer.register_customer(username, salary)
        except ValueError:
            raise AttributeError("Can't register in blockchain")

        user = User(username, password, "customer")
        db.session.add(user)
        db.session.commit()
        logging.info("{} customer registration successful".format(username))
        return user

    def get_all_policy_appl(self):
        logging.info("Retrieving All Policy Applications")
        try:
            return company.get_all_policy_appl()
        except ValueError:
            raise AttributeError("Can't retrieve from the blockchain")

    def register_cust_policy(self, applyID):
        logging.info("Registering Customer's Policy")
        try:
            return company.register_customer_policy(applyID)
        except ValueError:
            raise AttributeError("Can't register policy application in blockchain")

    def reject_policy_appl(self, applyID):
        logging.info("Rejecting Customer's Policy Application")
        try:
            return company.reject_policy_appl(applyID)
        except ValueError:
            raise AttributeError("Can't reject policy application in blockchain")

    def get_all_claim(self):
        logging.info("Retrieving All Claims")
        try:
            return company.get_all_claim()
        except ValueError:
            raise AttributeError("Can't retrieve from the blockchain")

    def reject_claim(self, claimID):
        logging.info("Reject Claim")
        try:
            return company.reject_claim(claimID)
        except ValueError:
            raise AttributeError("Can't reject claim in blockchain")

    def submit_reimb(self, claimID, reimbType):
        logging.info("Submit Reimbursement")
        try:
            return company.submit_reimbursement(claimID, reimbType)
        except ValueError:
            raise AttributeError("Can't submit reimbursement in blockchain")

    def get_all_cust(self):
        logging.info("Retrieving All Customers")
        try:
            return company.get_all_cust()
        except ValueError:
            raise AttributeError("Can't retrieve from the blockchain")

    def submit_cashout(self, custpolicyid, custid):
        logging.info("Submit CashOut")
        try:
            return company.submit_cashout(custpolicyid, custid)
        except ValueError:
            raise AttributeError("Can't create in the blockchain")


company_controller = CompanyController()
