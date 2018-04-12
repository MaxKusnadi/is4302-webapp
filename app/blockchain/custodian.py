import logging
import requests

from ..blockchain import URL

REGISTRATION_ENDPOINT = "/org.acme.insurance.CustodianBank"


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

    def reject_reimbursement(self):
        pass

    def approve_cashout(self):
        pass

    def reject_cashout(self):
        pass


custodian = Custodian()
