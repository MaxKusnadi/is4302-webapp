from flask import redirect, url_for, flash, render_template
from flask_login import current_user

from app import app
from ..controllers.login import LoginController
from ..controllers.custodian import CustodianController

login_controller = LoginController()
custodian_controller = CustodianController()


@app.route('/custodianViewPendingReimbursement', methods=["GET"])
def custodianViewPendingReimbursement():
    result = []
    try:
        result = custodian_controller.get_pending_reimbursement()
    except ValueError:
        flash("Unable to get reimbursement information. Please try again later")
    return render_template('custodian/custodianViewPendingReimbursement.html', reimbursements=result,title='View Pending Reimbursement', name=current_user.username)

@app.route('/custodianViewAllReimbursement')
def custodianViewAllReimbursement():
    result = []
    try:
        result = custodian_controller.get_reimbursement()
    except ValueError:
        flash("Unable to get reimbursement information. Please try again later")
    return render_template('custodian/custodianViewAllReimbursement.html', reimbursements=result, title='View All Reimbursement', name=current_user.username)

@app.route('/custodianViewPendingCashout')
def custodianViewPendingCashout():
    result = []
    try:
        result = custodian_controller.get_pending_cashout()
    except ValueError:
        flash("Unable to get pending cashout information. Please try again later")
    return render_template('custodian/custodianViewPendingCashout.html', cashouts=result, title='View Pending Cashout', name=current_user.username)

@app.route('/custodianViewAllCashout')
def custodianViewAllCashout():
    result = []
    try:
        result = custodian_controller.get_cashout()
    except ValueError:
        flash("Unable to get cashout information. Please try again later")
    return render_template('custodian/custodianViewAllCashout.html', cashouts=result, title='View Pending Cashout', name=current_user.username)


@app.route('/custodianVerifyPremium')
def custodianVerifyPremium():
    return render_template('custodian/custodianVerifyPremium.html', title='Verify Premium', name=current_user.username)