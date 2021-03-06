from ..blockchain.customer import customer


class CustomerController:

    def get_own_data(self, username):
        try:
            return customer.get_own_data(username)
        except ValueError:
            raise AttributeError("Can't retrieve own data from blockchain")

    def get_policies(self):
        try:
            return customer.get_policies()
        except ValueError:
            raise AttributeError("Can't retrieve policies from blockchain")

    def submit_policy_appl(self, username, policyid):
        try:
            return customer.submit_policy_appl(username, policyid)
        except ValueError:
            raise AttributeError("Can't submit policy application in blockchain")

    def get_policy_appl(self, applyid):
        try:
            return customer.get_policy_appl(applyid)
        except ValueError:
            raise AttributeError("Can't retrieve policy application from blockchain")

    def view_money_pool(self, username):
        try:
            return customer.view_money_pool(username)
        except ValueError:
            raise AttributeError("Can't retrieve money pool from blockchain")

    def view_money_pool_reimbursed(self, policyid):
        try:
            return customer.view_money_pool_reimbursed(policyid)
        except ValueError:
            raise AttributeError("Can't retrieve money pool reimbursed from blockchain")

    def file_claim(self, policyid, username, claimdesc):
        try:
            return customer.file_claim(policyid, username, claimdesc)
        except ValueError:
            raise AttributeError("Can't file claim in blockchain")

    def submit_premium_payment(self, policyid, username):
        try:
            return customer.submit_premium_payment(policyid, username)
        except ValueError:
            raise AttributeError("Can't submit premium payment in blockchain")


customer_controller = CustomerController()
