import logging
import requests

from ..blockchain import URL

REGISTRATION_ENDPOINT = "/org.acme.insurance.InsuranceCompany"
CUST_ENDPOINT ="/org.acme.insurance.Customer"
POLICY_ENDPOINT ="/org.acme.insurance.Policy"
POLICYAPPL_ENDPOINT="/org.acme.insurance.PolicyApplication"
CUSTPOL_ENDPOINT="/org.acme.insurance.CustomerPolicy"
REJECTPOLAPPL_ENDPOINT="/org.acme.insurance.RejectPolicyApplication"
CLAIM_ENDPOINT="/org.acme.insurance.Claim"
APPROVECLAIM_ENDPOINT="/org.acme.insurance.ApproveClaim"
REJECTCLAIM_ENDPOINT="/org.acme.insurance.RejectClaim"
SUBMITREIMB_ENDPOINT="/org.acme.insurance.SubmitReimbursement"


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

    def get_all_policy_appl(self):
        logging.info("Getting All Policy Applications")
        data = {
            "$class": "org.acme.insurance.PolicyApplication"
        }
        r = requests.get(URL + POLICYAPPL_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to retrieve all policy applications")
            logging.info(r.text)
            raise ValueError("Unable to retrieve all policy applications from blockchain")
        return r.json()

    def register_customer_policy(self, applyID):
        logging.info("Registering Policy To Customer")
        data = {
            "$class": "org.acme.insurance.CustomerPolicy",
            "status": "ACTIVE",
            "cashOutStatus": "INVALID",
            "apply": "resource:org.acme.insurance.PolicyApplication#"+applyID
        }
        r = requests.post(URL + CUSTPOL_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to create customer policy")
            logging.info(r.text)
            raise ValueError("Unable create customer policy in the blockchain")
        return r.json()

    def reject_policy_appl(self, applyID):
        logging.info("Rejecting Policy Application")
        data = {
            "$class": "org.acme.insurance.RejectPolicyApplication",
            "apply": "resource:org.acme.insurance.PolicyApplication#"+applyID
        }
        r = requests.post(URL + REJECTPOLAPPL_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to reject policy application")
            logging.info(r.text)
            raise ValueError("Unable reject policy application in the blockchain")
        return r.json()

    def submit_reimbursement(self, claimID, reimbType):
        logging.info("Submit Reimbursement")
        data = {
            "$class": "org.acme.insurance.SubmitReimbursement",
            "newCode": reimbType,
            "claim": "org.acme.insurance.Claim#"+claimID
        }
        r = requests.post(URL + SUBMITREIMB_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to submit reimbursement")
            logging.info(r.text)
            raise ValueError("Unable submit reimbursement in the blockchain")
        return r.json()

    def get_all_cust(self):
        logging.info("Getting All Customers")
        data = {
            "$class": "org.acme.insurance.Customer"
        }
        r = requests.get(URL + CUST_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to retrieve all customers")
            logging.info(r.text)
            raise ValueError("Unable to retrieve all customers from blockchain")
        return r.json()

    def submit_cashout(self):
        pass

    def get_all_claim(self):
        logging.info("Getting All Claim Requests")
        data = {
            "$class": "org.acme.insurance.Claim"
        }
        r = requests.get(URL + CLAIM_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to create")
            logging.info(r.text)
            raise ValueError("Unable to retrieve all claims from blockchain")
        return r.json()

    def approve_claim(self, claimID):
        logging.info("Approving Claim Request")
        data = {
            "$class": "org.acme.insurance.ApproveClaim",
            "claim": "resource:org.acme.insurance.Claim#"+claimID
        }
        r = requests.post(URL + APPROVECLAIM_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to create")
            logging.info(r.text)
            raise ValueError("Unable to approve claim in blockchain")
        return r.json()

    def reject_claim(self, claimID):
        logging.info("Rejecting Claim Request")
        data = {
            "$class": "org.acme.insurance.RejectClaim",
            "claim": "resource:org.acme.insurance.Claim#"+claimID
        }
        r = requests.post(URL + REJECTCLAIM_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to create")
            logging.info(r.text)
            raise ValueError("Unable to reject claim in blockchain")
        return r.json()

    def terminate_customer_policy(self):
        pass


company = Company()
