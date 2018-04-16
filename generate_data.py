import logging

from app.controllers.login import login_controller
from app.controllers.company import company_controller

from app import db


# Reset Database
meta = db.metadata
for table in reversed(meta.sorted_tables):
    db.session.execute(table.delete())
db.session.commit()

# Generate customer
logging.info("Generating customer data")
company_controller.register_customer("customer1", "customer1", 3000)
logging.info("customer1 created")

# Generate company
logging.info("Generating company data")
login_controller.sign_up("company", "company", "company")
logging.info("company created")

# Generate regulator
logging.info("Generating regulator data")
login_controller.sign_up("regulator", "regulator", "regulator")
logging.info("regulator created")

# Generate custodian
logging.info("Generating custodian data")
login_controller.sign_up("custodian", "custodian", "custodian")
logging.info("custodian created")