import logging
import requests

from ..blockchain import URL

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
        r = requests.get(URL + CUSTOMER_ENDPOINT + "/" + username, json=data)
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
        r = requests.get(URL + POLICY_ENDPOINT, json=data)
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
        r = requests.post(URL + SUBMITPOLICYAPPL_ENDPOINT, json=data)
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

    def view_money_pool(self, username):
        logging.info("Retrieving all customer policy money pool Data")
        data = {
            "$class": "org.acme.insurance.Customer#"+username
        }

        logging.info("Getting customer info")
        #customer info request
        cr = requests.get(URL + CUSTOMER_ENDPOINT+ "/" + username, json=data)

        logging.info("Status code: {}".format(cr.status_code))

        if cr.status_code != 200:
            logging.error("Unable to retrieve")
            logging.info(cr.text)
            raise ValueError("Unable to get all customers")
        cust = cr.json()
        result = []
        for policyid in cust['policies']:
            # money pool request
            mr = requests.get(URL + VIEW_MONEY_POOL_ENDPOINT+ "/" + policyid, json=data)
            logging.info("Status code: {}".format(mr.status_code))
            if mr.status_code != 200:
                logging.error("Unable to retrieve")
                logging.info(mr.text)
                raise ValueError("Unable retrieve from the blockchain")
            result.push(mr.json())
        return result

    def view_money_pool_reimbursed(self, policyid, fromDate, toDate):
        logging.info("Retrieving money pool reimbursed Data")
        data = {
            "$class": "org.acme.insurance.Customer",
            "policyId": policyid,
            "fromDate": fromDate,
            "toDate": toDate,
        }
        r = requests.get(URL + VIEW_MONEY_POOL_REIMBURSED_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to retrieve")
            logging.info(r.text)
            raise ValueError("Unable retrieve from the blockchain")
        return r.json()

    def register_customer(self, username, salary=0):
        logging.info("Registering {} into the blockchain".format(username))
        data = {
            "$class": "org.acme.insurance.Customer",
            "idNo": username,
            "salary": salary
        }
        r = requests.post(URL + REGISTER_CUSTOMER, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to create customer")
            logging.info(r.text)
            raise ValueError("Unable to create user in blockchain")
        return r.json()

    def add_salary(self, username, salary):
        pass

customer = Customer()
