import logging
import requests

from ..blockchain import CUSTURL
from ..blockchain import COMPURL

# List of endpoints
CUSTOMER_ENDPOINT = "/org.acme.insurance.Customer"
REGISTER_CUSTOMER = "/org.acme.insurance.RegisterCustomer"
POLICY_ENDPOINT = "/org.acme.insurance.Policy"
POLICYAPPL_ENDPOINT = "/org.acme.insurance.PolicyApplication"
SUBMITPOLICYAPPL_ENDPOINT = "/org.acme.insurance.SubmitPolicyApplication"
FILE_CLAIM_ENDPOINT = "/org.acme.insurance.FileClaim"
SUBMIT_PREMIUM_PAYMENT_ENDPOINT = "/org.acme.insurance.SubmitPremiumPayment"
VIEW_MONEY_POOL_ENDPOINT = "/org.acme.insurance.MoneyPool"
VIEW_MONEY_POOL_REIMBURSED_ENDPOINT = "/org.acme.insurance.ViewMoneyPoolAmountReimbursed"


class Customer:

    def get_own_data(self, username):
        logging.info("Retrieving Own Data")
        data = {
            "$class": "org.acme.insurance.Customer"
        }
        r = requests.get(CUSTURL + CUSTOMER_ENDPOINT + "/" + username, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to retrieve")
            logging.info(r.text)
            raise ValueError("Unable retrieve from the blockchain")
        return r.json()

    def get_policies(self):
        logging.info("Retrieving Policies")
        data = {
            "$class": "org.acme.insurance.Policy"
        }
        r = requests.get(CUSTURL + POLICY_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to retrieve")
            logging.info(r.text)
            raise ValueError("Unable retrieve policies in blockchain")
        return r.json()

    def submit_policy_appl(self, username, policyid):
        logging.info("Submit Policy Application")
        data = {
            "$class": "org.acme.insurance.SubmitPolicyApplication",
            "newCust": "resource:org.acme.insurance.Customer#"+username,
            "newPolicy": "resource:org.acme.insurance.Policy#"+policyid
        }
        r = requests.post(CUSTURL + SUBMITPOLICYAPPL_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to create")
            logging.info(r.text)
            raise ValueError("Unable create in the blockchain")
        return r.json()

    def get_policy_appl(self, applyid):
        logging.info("Retrieving Policy Application")
        data = {
            "$class": "org.acme.insurance.PolicyApplication"
        }
        r = requests.get(CUSTURL + POLICYAPPL_ENDPOINT + "/" + applyid, json=data)
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
        r = requests.post(CUSTURL + FILE_CLAIM_ENDPOINT, json=data)
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
        r = requests.post(CUSTURL + SUBMIT_PREMIUM_PAYMENT_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to create payment")
            logging.info(r.text)
            raise ValueError("Unable create premium payment in the blockchain")
        return r.json()

    def view_money_pool(self, username):
        logging.info("Retrieving all customer policy money pool Data")
        data = {
            "$class": "org.acme.insurance.Customer#"+username
        }

        logging.info("Getting customer info")
        cr = requests.get(CUSTURL + CUSTOMER_ENDPOINT + "/" + username, json=data)

        logging.info("Status code: {}".format(cr.status_code))

        if cr.status_code != 200:
            logging.error("Unable to retrieve")
            logging.info(cr.text)
            raise ValueError("Unable to get all customers")
        cust = cr.json()
        result = []
        for policy in cust['policies']:
            # money pool request
            policyID = policy['policy'].split('#')
            mr = requests.get(CUSTURL + VIEW_MONEY_POOL_ENDPOINT+ "/" + str(policyID[1]), json=data)
            logging.info("Status code: {}".format(mr.status_code))
            if mr.status_code != 200:
                logging.error("Unable to retrieve")
                logging.info(mr.text)
                raise ValueError("Unable retrieve from the blockchain")
            result.append(mr.json())
        return result

    def view_money_pool_reimbursed(self, policyid):
        logging.info("Retrieving money pool reimbursed Data")

        r = requests.get(CUSTURL + VIEW_MONEY_POOL_ENDPOINT+ "/" + policyid)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to retrieve")
            logging.info(r.text)
            raise ValueError("Unable retrieve from the blockchain")
        return r.json()

    def register_customer(self, username, salary=0):
        logging.info("Registering {} into the blockchain".format(username))
        data = {
            "$class": "org.acme.insurance.RegisterCustomer",
            "idNo": username,
            "salary": salary
        }
        r = requests.post(COMPURL + REGISTER_CUSTOMER, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to create customer")
            logging.info(r.text)
            raise ValueError("Unable to create user in blockchain")
        return r.json()

    def add_salary(self, username, salary):
        pass


customer = Customer()
