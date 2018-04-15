import logging
import requests
from ..blockchain import URL
CUSTODIAN_ENDPOINT="/org.acme.insurance.Custodian"
REIMBURSEMENT_ENDPOINT = "/org.acme.insurance.Reimbursement"
CASHOUT_ENDPOINT = "/org.acme.insurance.CashOut"
APPROVE_REIMBURSEMENT_ENDPOINT = "/org.acme.insurance.ApproveReimbursement"
REJECT_REIMBURSEMENT_ENDPOINT = "/org.acme.insurance.RejectReimbursement"
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

    def approve_reimbursement(self):
        pass

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

    def reject_reimbursement(self):
        pass

    def approve_cashout(self):
        pass

    def reject_cashout(self):
        pass

custodian = Custodian()