from flask import redirect, url_for, flash, render_template
from flask_login import current_user

from app import app
from ..controllers.login import LoginController
from ..controllers.custodian import CustodianController

login_controller = LoginController()
custodian_controller = CustodianController()


@app.route('/custodian_home', methods=["GET"])
def custodian_home():
    return render_template('custodian/custodianHome.html', title='Custodian Portal Home', name=current_user.username)

@app.route('/custodianViewPendingReimbursement', methods=["GET"])
def custodianViewPendingReimbursement():
    result = []
    try:
        result = custodian_controller.get_pending_reimbursement()
    except ValueError:
        flash("Unable to get reimbursement information. Please try again later")
    return render_template('custodian/custodianViewPendingReimbursement.html', reimbursements=result,title='View Pending Reimbursement', name=current_user.username)


@app.route('/approve-reimbursement/<reimbID>', methods=["GET"])
def approve_reimbursement(reimbID):
    if current_user.role != "custodian":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    try:
        custodian_controller.approve_reimbursement(reimbID)
    except ValueError:
        flash("Unable to approve reimbursement. Please try again later")
    return redirect(url_for('custodianViewAllReimbursement'))


@app.route('/reject-reimbursement/<reimbID>', methods=["GET"])
def reject_reimbursement(reimbID):
    if current_user.role != "custodian":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    try:
        custodian_controller.reject_reimbursement(reimbID)
    except ValueError:
        flash("Unable to reject reimbursement. Please try again later")
    return redirect(url_for('custodianViewAllReimbursement'))


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

@app.route('/approve-cashout/<cashoutID>', methods=["GET"])
def approve_cashout(cashoutID):
    if current_user.role != "custodian":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    try:
        custodian_controller.approve_cashout(cashoutID)
    except ValueError:
        flash("Unable to approve cashout. Please try again later")
    return redirect(url_for('custodianViewAllCashout'))


@app.route('/reject-cashout/<cashoutID>', methods=["GET"])
def reject_cashout(cashoutID):
    if current_user.role != "custodian":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    try:
        custodian_controller.reject_cashout(cashoutID)
    except ValueError:
        flash("Unable to reject cashout. Please try again later")
    return redirect(url_for('custodianViewAllCashout'))


@app.route('/custodianViewAllCashout')
def custodianViewAllCashout():
    result = []
    try:
        result = custodian_controller.get_cashout()
    except ValueError:
        flash("Unable to get cashout information. Please try again later")
    return render_template('custodian/custodianViewAllCashout.html', cashouts=result, title='View Pending Cashout', name=current_user.username)

@app.route('/verify-premium/<premID>', methods=["GET"])
def verify_premium(premID):
    if current_user.role != "custodian":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    try:
        custodian_controller.verify_premium(premID)
    except ValueError:
        flash("Unable to verify premium. Please try again later")
    return redirect(url_for('custodianVerifyPremium'))

@app.route('/reject-premium/<premID>', methods=["GET"])
def reject_premium(premID):
    if current_user.role != "custodian":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    try:
        custodian_controller.reject_premium(premID)
    except ValueError:
        flash("Unable to reject premium. Please try again later")
    return redirect(url_for('custodianVerifyPremium'))

@app.route('/custodianVerifyPremium')
def custodianVerifyPremium():
    result = []
    try:
        result = custodian_controller.get_pending_premium()
    except ValueError:
        flash("Unable to get pending premium information. Please try again later")
    return render_template('custodian/custodianVerifyPremium.html', premiumpayments=result, title='Verify Premium', name=current_user.username)

@app.route('/custodianViewAllPremium')
def custodianViewAllPremium():
    result = []
    try:
        result = custodian_controller.get_all_premium()
    except ValueError:
        flash("Unable to get premium information. Please try again later")
    return render_template('custodian/custodianViewAllPremium.html', premiumpayments=result, title='View Premium', name=current_user.username)
