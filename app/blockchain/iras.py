import logging
import requests

from ..blockchain import URL

REGISTRATION_ENDPOINT = "/org.acme.insurance.Regulator"


class IRAS:

    def register_regulator(self, username):
        logging.info("Registering {} into the blockchain".format(username))
        data = {
            "$class": "org.acme.insurance.Regulator",
            "regID": username,
            "name": "Admin",
            "organization": "IRAS"
        }
        r = requests.post(URL + REGISTRATION_ENDPOINT, json=data)
        logging.info("Status code: {}".format(r.status_code))
        if r.status_code != 200:
            logging.error("Unable to create regulator")
            logging.info(r.text)
            raise ValueError("Unable to create regulator in blockchain")
        return r.json()

    def approve_registration(self):
        pass

    def reject_registration(self):
        pass


iras = IRAS()
