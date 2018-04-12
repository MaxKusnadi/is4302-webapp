import logging
from flask_login import login_user, logout_user

from app import db, login_manager, cache
from ..models.user import User
from ..blockchain.customer import customer
from ..blockchain.company import company
from ..blockchain.custodian import custodian
from ..blockchain.iras import iras


@login_manager.user_loader
def load_user(username):
    return User.query.filter(User.username == username).first()


class LoginController:

    def sign_up(self, username, password, role):
        logging.info("Signup by {}".format(username))
        # Check username exists
        user = self._get_user(username)
        if user:
            logging.error("Username {} exits".format(username))
            raise ValueError("Username exits")

        try:
            logging.info("User role: {}".format(role))
            if role == "customer":
                customer.register_customer(username)
            elif role == "company":
                company.register_company(username)
            elif role == "custodian":
                custodian.register_custodian(username)
            elif role == "regulator":
                iras.register_regulator(username)
        except ValueError:
            raise AttributeError("Can't register in blockchain")

        user = User(username, password, role)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        logging.info("{} signup successful".format(username))
        return user

    def login(self, username, password):
        logging.info("Login by {}".format(username))
        user = User.query.filter(User.username == username).first()
        if not user:
            logging.info(user)
            logging.error("User {} not found".format(username))
            raise ValueError("Username not found")
        if not user.is_password_correct(password):
            logging.error("Wrong password")
            raise AttributeError("Wrong password")
        login_user(user)
        logging.info("{} Login successful".format(username))
        return user

    def logout(self):
        logout_user()

    @cache.memoize()
    def _get_user(self, username):
        return User.query.filter(User.username == username).first()


login_controller = LoginController()
