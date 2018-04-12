import logging
import requests

from ..blockchain import URL

CUSTOMER_ENDPOINT = "/org.acme.insurance.Customer"


class Customer:

    def file_claim(self):
        pass

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
            "salary": 0,
            "verifiedByIRAS": "PENDING"
        }
        r = requests.post(URL+CUSTOMER_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to create customer")
            logging.info(r.text)
            raise ValueError("Unable to create user in blockchain")
        return r.json()

    def add_salary(self, username, salary):
        pass


customer = Customer()
