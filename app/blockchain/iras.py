import logging
import requests

from ..blockchain import URL
from ..blockchain import REGURL

REGISTRATION_ENDPOINT = "/org.acme.insurance.Regulator"
CUSTOMER_ENDPOINT = "/org.acme.insurance.Customer"
APPROVE_REG_ENDPOINT = "/org.acme.insurance.ApproveRegistration"
REJECT_REG_ENDPOINT = "/org.acme.insurance.RejectRegistration"


class IRAS:

    def register_regulator(self, username):
        logging.info("Registering {} into the blockchain".format(username))
        data = {
            "$class": "org.acme.insurance.Regulator",
            "regID": username,
            "name": "Admin",
            "organization": "IRAS"
        }
        r = requests.post(URL + REGISTRATION_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to create regulator")
            logging.info(r.text)
            raise ValueError("Unable to create regulator in blockchain")
        return r.json()

    def get_pending_customer_registration(self):
        logging.info("Getting pending customer registration")
        r = requests.get(REGURL + CUSTOMER_ENDPOINT)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to get pending customer registration")
            logging.info(r.text)
            raise ValueError("Unable to get pending customer registration")
        result = r.json()
        result = list(filter(lambda x: 'verifiedByIRAS' in x, result))
        result = list(filter(lambda x: x['verifiedByIRAS'] == "PENDING", result))
        return result

    def approve_registration(self, username):
        logging.info("Approving registration of {} into the blockchain".format(username))
        data = {
            "$class": "org.acme.insurance.ApproveRegistration",
            "customer": username
        }
        r = requests.post(REGURL + APPROVE_REG_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to approve registration")
            logging.info(r.text)
            raise ValueError("Unable to approve registration in blockchain")
        return r.json()

    def reject_registration(self, username):
        logging.info("Rejecting registration of {} into the blockchain".format(username))
        data = {
            "$class": "org.acme.insurance.RejectRegistration",
            "customer": username
        }
        r = requests.post(REGURL + REJECT_REG_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to reject registration")
            logging.info(r.text)
            raise ValueError("Unable to reject registration in blockchain")
        return r.json()


iras = IRAS()
