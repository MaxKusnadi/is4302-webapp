import logging
import requests

from ..blockchain import URL

CUSTOMER_ENDPOINT = "/org.acme.insurance.Customer"
POLICYAPPL_ENDPOINT = "/org.acme.insurance.PolicyApplication"
FILE_CLAIM_ENDPOINT = "/org.acme.insurance.FileClaim"
SUBMIT_PREMIUM_PAYMENT_ENDPOINT = "/org.acme.insurance.SubmitPremiumPayment"


class Customer:

    def get_own_data(self, username):
        logging.info("Retrieving Own Data")
        data = {
            "$class": "org.acme.insurance.Customer",
        }
        r = requests.get(URL + CUSTOMER_ENDPOINT + "/" + username, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to retrieve")
            logging.info(r.text)
            raise ValueError("Unable retrieve from the blockchain")
        return r.json()

    def get_policy_appl(self, applyid):
        logging.info("Retrieving Policy Application")
        data = {
            "$class": "org.acme.insurance.PolicyApplication",
        }
        r = requests.get(URL + POLICYAPPL_ENDPOINT + "/" + applyid, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to retrieve")
            logging.info(r.text)
            raise ValueError("Unable retrieve from the blockchain")
        return r.json()

    def file_claim(self, policyid, username, claimdesc):
        logging.info("File Claim")
        data = {
          "$class": "org.acme.insurance.FileClaim",
          "policyId": policyid,
          "claimDesc": claimdesc,
          "customer": "resource:org.acme.insurance.Customer#"+username
        }
        #logging.info(username+" "+claimdesc+" "+policyid)
        r = requests.post(URL + FILE_CLAIM_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to create claim")
            logging.info(r.text)
            raise ValueError("Unable create claim in the blockchain")
        return r.json()

    def submit_premium_payment(self, policyid, username):
        logging.info("Submit Premium Payment")
        data = {
          "$class": "org.acme.insurance.SubmitPremiumPayment",
          "policyId": policyid,
          "customer": "resource:org.acme.insurance.Customer#"+username
        }
        r = requests.post(URL + SUBMIT_PREMIUM_PAYMENT_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to create payment")
            logging.info(r.text)
            raise ValueError("Unable create premium payment in the blockchain")
        return r.json()

    def view_money_pool(self):
        pass

    def view_pool_reimbursement(self):
        pass

    def register_customer(self, username, salary=0):
        logging.info("Registering {} into the blockchain".format(username))
        data = {
            "$class": "org.acme.insurance.Customer",
            "idNo": username,
            "salary": salary,
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
