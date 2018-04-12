import logging
import requests

from ..blockchain import URL

REGISTRATION_ENDPOINT = "/org.acme.insurance.InsuranceCompany"


class Company:

    def register_company(self, username):
        logging.info("Registering {} into the blockchain".format(username))
        data = {
            "$class": "org.acme.insurance.InsuranceCompany",
            "companyID": username,
            "name": "Admin"
        }
        r = requests.post(URL + REGISTRATION_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to create company")
            logging.info(r.text)
            raise ValueError("Unable to create company in blockchain")
        return r.json()

    def register_policy(self):
        pass

    def assign_pool_to_policy(self):
        pass

    def register_customer_policy(self):
        pass

    def submit_reimbursement(self):
        pass

    def submit_cashout(self):
        pass

    def approve_claim(self):
        pass

    def reject_claim(self):
        pass

    def terminate_customer_policy(self):
        pass


company = Company()
