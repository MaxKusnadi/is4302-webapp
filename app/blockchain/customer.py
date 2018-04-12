import logging
import requests

from ..blockchain import URL

CUSTOMER_ENDPOINT="/org.acme.insurance.Customer"
FILE_CLAIM="/org.acme.insurance.FileClaim"


class Customer:

    def file_claim(self, claimDesc):
        data = {
          "$class": "org.acme.insurance.Claim",
          "description": claimDesc,
          "customer": "resource:org.acme.insurance.Customer#elvin",
          "policy": "resource:org.acme.insurance.Policy#elvintest"
        }
        r = requests.post(URL+FILE_CLAIM, json=data)
        return r.json()

    def submit_premium_payment(self):
        pass

    def view_money_pool(self):
        pass

    def view_pool_reimbursement(self):
        pass

    def register_customer(self, username):
        logging.info("Registering {} into the blockchain".format(username))
        data = {
            "$class": "org.acme.insurance.Customer",
            "idNo": username,
            "salary": 0
        }
        r = requests.post(URL+CUSTOMER_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to create")
            logging.info(r.text)
            raise ValueError("Unable to create user in blockchain")
        return r.json()

    def add_salary(self, username, salary):
        pass
