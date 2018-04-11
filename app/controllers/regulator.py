import logging

from ..blockchain.iras import iras


class RegulatorController:

    def get_pending_customer_registration(self):
        logging.info("Getting pending customer registration from controller")
        try:
            result = iras.get_pending_customer_registration()
        except ValueError:
            raise ValueError("Unable to get pending customer registration")
        return result

    def approve_registration(self, username):
        logging.info("Approving customer registration from controller")
        try:
            result = iras.approve_registration(username)
        except ValueError:
            raise ValueError("Unable to approve customer registration")
        return result

    def reject_registration(self, username):
        logging.info("Rejecting customer registration from controller")
        try:
            result = iras.reject_registration(username)
        except ValueError:
            raise ValueError("Unable to reject customer registration")
        return result


regulator_controller = RegulatorController()
