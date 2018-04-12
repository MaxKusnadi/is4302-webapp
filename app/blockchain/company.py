import logging
import requests
import datetime

from ..blockchain import URL

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
            logging.error("Unable to create")
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
            logging.error("Unable to create")
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
            logging.error("Unable to create")
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
            logging.error("Unable to create")
            logging.info(r.text)
            raise ValueError("Unable submit reimbursement in the blockchain")
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
