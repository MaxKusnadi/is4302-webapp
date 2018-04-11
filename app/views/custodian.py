from flask import redirect, url_for, flash, render_template
from flask_login import current_user

from app import app
from ..controllers.login import LoginController
from ..controllers.custodian import CustodianController

login_controller = LoginController()
custodian_controller = CustodianController()


@app.route('/custodianViewReimbursement')
def custodianViewReimbursement():
    return render_template('custodianViewReimbursement.html', title='View Reimbursement', name=current_user.username)

@app.route('/custodianViewCashout')
def custodianViewCashout():
    return render_template('custodianViewCashout.html', title='View Cashout', name=current_user.username)

@app.route('/custodianVerifyPremium')
def custodianVerifyPremium():
    return render_template('custodianVerifyPremium.html', title='Verify Premium', name=current_user.username)