import logging
import requests

from ..blockchain import URL
from ..blockchain import COMPURL

REGISTRATION_ENDPOINT = "/org.acme.insurance.InsuranceCompany"
CUST_ENDPOINT = "/org.acme.insurance.Customer"
POLICY_ENDPOINT = "/org.acme.insurance.Policy"
POLICYAPPL_ENDPOINT = "/org.acme.insurance.PolicyApplication"
CUSTPOL_ENDPOINT = "/org.acme.insurance.CustomerPolicy"
REJECTPOLAPPL_ENDPOINT = "/org.acme.insurance.RejectPolicyApplication"
CLAIM_ENDPOINT = "/org.acme.insurance.Claim"
APPROVECLAIM_ENDPOINT = "/org.acme.insurance.ApproveClaim"
REJECTCLAIM_ENDPOINT = "/org.acme.insurance.RejectClaim"
SUBMITREIMB_ENDPOINT = "/org.acme.insurance.SubmitReimbursement"
SUBMITCASHOUT_ENDPOINT = "/org.acme.insurance.SubmitCashOut"
REGISTER_POLICY_ENDPOINT = "/org.acme.insurance.RegisterPolicy"
ASSIGN_MONEY_POOL_TO_POLICY_ENDPOINT = "/org.acme.insurance.AssignMoneyPoolToPolicy"
TERMINATE_POLICY_ENDPOINT = "/org.acme.insurance.TerminateCustomerPolicy"


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

    def register_policy(self, policyId, duration):
        logging.info("Registering a policy {}".format(policyId))
        data = {
            "$class": "org.acme.insurance.RegisterPolicy",
            "policyID": policyId,
            "description": "New policy",
            "duration": duration,
            "moneyPoolID": policyId
        }
        r = requests.post(COMPURL + REGISTER_POLICY_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to register policy")
            logging.info(r.text)
            raise ValueError("Unable to register in blockchain")
        return r.json()

    def assign_pool_to_policy(self, policyId):
        logging.info("Assigning pool to policy")
        data = {
            "$class": "org.acme.insurance.AssignMoneyPoolToPolicy",
            "policy": "resource:org.acme.insurance.Policy#"+policyId,
            "pool": "resource:org.acme.insurance.MoneyPool#"+policyId
        }
        r = requests.post(COMPURL + ASSIGN_MONEY_POOL_TO_POLICY_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to assign pool to policy")
            logging.info(r.text)
            raise ValueError("Unable to assign pool to policy in blockchain")
        return r.json()

    def get_all_policy_appl(self):
        logging.info("Getting All Policy Applications")
        data = {
            "$class": "org.acme.insurance.PolicyApplication"
        }
        r = requests.get(COMPURL + POLICYAPPL_ENDPOINT, json=data)
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
        r = requests.post(COMPURL + CUSTPOL_ENDPOINT, json=data)
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
        r = requests.post(COMPURL + REJECTPOLAPPL_ENDPOINT, json=data)
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
        r = requests.post(COMPURL + SUBMITREIMB_ENDPOINT, json=data)
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
        r = requests.get(COMPURL + CUST_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to retrieve all customers")
            logging.info(r.text)
            raise ValueError("Unable to retrieve all customers from blockchain")
        return r.json()

    def submit_cashout(self, custpolicyid, custid):
        logging.info("Submit CashOut")
        data = {
            "$class": "org.acme.insurance.SubmitCashOut",
            "custPolicyID": custpolicyid,
            "customer": "org.acme.insurance.Customer#"+custid
        }
        r = requests.post(COMPURL + SUBMITCASHOUT_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to submit cash out")
            logging.info(r.text)
            raise ValueError("Unable submit cash out in the blockchain")
        return r.json()

    def get_all_claim(self):
        logging.info("Getting All Claim Requests")
        data = {
            "$class": "org.acme.insurance.Claim"
        }
        r = requests.get(COMPURL + CLAIM_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to create")
            logging.info(r.text)
            raise ValueError("Unable to retrieve all claims from blockchain")
        return r.json()

    def reject_claim(self, claimID):
        logging.info("Rejecting Claim Request")
        data = {
            "$class": "org.acme.insurance.RejectClaim",
            "claim": "resource:org.acme.insurance.Claim#"+claimID
        }
        r = requests.post(COMPURL + REJECTCLAIM_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to create")
            logging.info(r.text)
            raise ValueError("Unable to reject claim in blockchain")
        return r.json()

    def terminate_customer_policy(self, policy_id, customer_id):
        logging.info("Terminating policy {} from  customer {}".format(policy_id, customer_id))
        data = {
            "$class": "org.acme.insurance.TerminateCustomerPolicy",
            "custPolicyID": policy_id,
            "customer": "resource:org.acme.insurance.Customer#"+customer_id
        }
        r = requests.post(COMPURL + TERMINATE_POLICY_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to terminate customer policy")
            logging.info(r.text)
            raise ValueError("Unable terminate customer policy in the blockchain")
        return r.json()


company = Company()
