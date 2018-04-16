import logging
import requests
from ..blockchain import URL


REGISTRATION_ENDPOINT = "/org.acme.insurance.CustodianBank"
CUSTODIAN_ENDPOINT="/org.acme.insurance.CustodianBank"
REIMBURSEMENT_ENDPOINT = "/org.acme.insurance.Reimbursement"
CASHOUT_ENDPOINT = "/org.acme.insurance.CashOut"
APPROVE_REIMBURSEMENT_ENDPOINT = "/org.acme.insurance.ApproveReimbursement"
REJECT_REIMBURSEMENT_ENDPOINT = "/org.acme.insurance.RejectReimbursement"
APPROVE_CASHOUT_ENDPOINT = "/org.acme.insurance.ApproveCashOut"
REJECT_CASHOUT_ENDPOINT = "/org.acme.insurance.RejectCashOut"
VERIFY_PREMIUM_ENDPOINT = "/org.acme.insurance.VerifyPremiumPayment"
PREMIUM_ENDPOINT = "/org.acme.insurance.Premium"

class Custodian:

    def register_custodian(self, username):
        logging.info("Registering {} into the blockchain".format(username))
        data = {
            "$class": "org.acme.insurance.CustodianBank",
            "custodianID": username,
            "name": "Admin",
            "description": "admin from custodian bank"
        }
        r = requests.post(URL + REGISTRATION_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to create custodian")
            logging.info(r.text)
            raise ValueError("Unable to create custodian in blockchain")
        return r.json()


    def get_pending_reimbursement(self):
        logging.info("Getting pending reimbursement")
        r = requests.get(URL + REIMBURSEMENT_ENDPOINT)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to get pending customer reimbursement")
            logging.info(r.text)
            raise ValueError("Unable to get pending customer reimbursement")
        result = r.json()
        result = list(filter(lambda x: 'status' in x, result))
        result = list(filter(lambda x: x['status'] == "PENDING", result))
        return result


    def get_reimbursement(self):
        logging.info("Getting all reimbursement")
        r = requests.get(URL + REIMBURSEMENT_ENDPOINT)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to get customer reimbursements")
            logging.info(r.text)
            raise ValueError("Unable to get customer reimbursements")
        result = r.json()
        return result

    def approve_reimbursement(self, reimbID):
        logging.info("Approving registration of {} into the blockchain".format(reimbID))
        data = {
            "$class": "org.acme.insurance.ApproveReimbursement",
            "reimbursement": "resource:org.acme.insurance.Reimbursement#" + str(reimbID)
        }
        r = requests.post(URL + APPROVE_REIMBURSEMENT_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to approve reimbursement")
            logging.info(r.text)
            raise ValueError("Unable to approve reimbursement in blockchain")
        return r.json()

    def reject_reimbursement(self, reimbID):
        logging.info("Rejecting registration of {} into the blockchain".format(reimbID))
        data = {
            "$class": "org.acme.insurance.RejectReimbursement",
            "reimbursement": "resource:org.acme.insurance.Reimbursement#" + str(reimbID)
        }
        r = requests.post(URL + REJECT_REIMBURSEMENT_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to reject reimbursement")
            logging.info(r.text)
            raise ValueError("Unable to reject reimbursement in blockchain")
        return r.json()

    def get_cashout(self):
        logging.info("Getting all cashout")
        r = requests.get(URL + CASHOUT_ENDPOINT)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to get cashout")
            logging.info(r.text)
            raise ValueError("Unable to get cashout")
        result = r.json()
        return result

    def get_pending_cashout(self):
        logging.info("Getting pending cashout")
        r = requests.get(URL + CASHOUT_ENDPOINT)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to get pending cashout")
            logging.info(r.text)
            raise ValueError("Unable to get pending cashout")
        result = r.json()
        result = list(filter(lambda x: 'status' in x, result))
        result = list(filter(lambda x: x['status'] == "PENDING", result))
        return result

    def approve_cashout(self, cashoutID):
        logging.info("Approving registration of {} into the blockchain".format(cashoutID))
        data = {
            "$class": "org.acme.insurance.ApproveCashOut",
            "cashout": "resource:org.acme.insurance.CashOut#" + str(cashoutID)
        }
        r = requests.post(URL + APPROVE_CASHOUT_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to approve cashout")
            logging.info(r.text)
            raise ValueError("Unable to approve cashout in blockchain")
        return r.json()

    def reject_cashout(self, cashoutID):
        logging.info("Rejecting registration of {} into the blockchain".format(cashoutID))
        data = {
            "$class": "org.acme.insurance.RejectCashOut",
            "cashout": "resource:org.acme.insurance.CashOut#" + str(cashoutID)
        }
        r = requests.post(URL + REJECT_CASHOUT_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to reject cashout")
            logging.info(r.text)
            raise ValueError("Unable to reject cashout in blockchain")
        return r.json()

    def get_pending_premium(self):
        logging.info("Getting pending premium")
        r = requests.get(URL + PREMIUM_ENDPOINT)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to get pending premium")
            logging.info(r.text)
            raise ValueError("Unable to get pending premium")
        result = r.json()
        result = list(filter(lambda x: 'status' in x, result))
        result = list(filter(lambda x: x['status'] == "PENDING", result))
        return result

    def verify_premium(self, premID):
        logging.info("Approving registration of {} into the blockchain".format(premID))
        data = {
            "$class": "org.acme.insurance.VerifyPremiumPayment",
            "premium": "resource:org.acme.insurance.Premium#" + str(premID),
            "paymentState": "APPROVED"
        }
        r = requests.post(URL + VERIFY_PREMIUM_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to verify premium payment")
            logging.info(r.text)
            raise ValueError("Unable to verify premium payment in blockchain")
        return r.json()

    def reject_premium(self, premID):
        logging.info("Approving registration of {} into the blockchain".format(premID))
        data = {
            "$class": "org.acme.insurance.VerifyPremiumPayment",
            "premium": "resource:org.acme.insurance.Premium#" + str(premID),
            "paymentState": "REJECTED"
        }
        r = requests.post(URL + VERIFY_PREMIUM_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to reject premium payment")
            logging.info(r.text)
            raise ValueError("Unable to reject premium payment in blockchain")
        return r.json()
custodian = Custodian()