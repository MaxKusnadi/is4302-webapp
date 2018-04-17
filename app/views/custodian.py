from flask import redirect, url_for, flash, render_template
from flask_login import current_user, login_required

from app import app
from ..controllers.custodian import custodian_controller


@app.route('/custodian_home', methods=["GET"])
@login_required
def custodian_home():
    if current_user.role != "custodian":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    return render_template('custodian/home.html', title='Custodian Portal Home', name=current_user.username)


@app.route('/custodianViewPendingReimbursement', methods=["GET"])
@login_required
def custodianViewPendingReimbursement():
    if current_user.role != "custodian":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    result = []
    try:
        result = custodian_controller.get_pending_reimbursement()
    except ValueError:
        flash("Unable to get reimbursement information. Please try again later")
    return render_template('custodian/viewPendingReimbursement.html', reimbursements=result,
                           title='View Pending Reimbursement', name=current_user.username)


@app.route('/approve-reimbursement/<reimbID>', methods=["GET"])
@login_required
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
@login_required
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
@login_required
def custodianViewAllReimbursement():
    if current_user.role != "custodian":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    result = []
    try:
        result = custodian_controller.get_reimbursement()
    except ValueError:
        flash("Unable to get reimbursement information. Please try again later")
    return render_template('custodian/viewAllReimbursement.html', reimbursements=result,
                           title='View All Reimbursement', name=current_user.username)


@app.route('/custodianViewPendingCashout')
@login_required
def custodianViewPendingCashout():
    if current_user.role != "custodian":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    result = []
    try:
        result = custodian_controller.get_pending_cashout()
    except ValueError:
        flash("Unable to get pending cashout information. Please try again later")
    return render_template('custodian/viewPendingCashout.html', cashouts=result,
                           title='View Pending Cashout', name=current_user.username)


@app.route('/approve-cashout/<cashoutID>', methods=["GET"])
@login_required
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
@login_required
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
@login_required
def custodianViewAllCashout():
    result = []
    try:
        result = custodian_controller.get_cashout()
    except ValueError:
        flash("Unable to get cashout information. Please try again later")
    return render_template('custodian/viewAllCashout.html', cashouts=result,
                           title='View Pending Cashout', name=current_user.username)


@app.route('/verify-premium/<premID>', methods=["GET"])
@login_required
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
@login_required
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
@login_required
def custodianVerifyPremium():
    if current_user.role != "custodian":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    result = []
    try:
        result = custodian_controller.get_pending_premium()
    except ValueError:
        flash("Unable to get pending premium information. Please try again later")
    return render_template('custodian/verifyPremium.html', premiumpayments=result,
                           title='Verify Premium', name=current_user.username)


@app.route('/custodianViewAllPremium')
@login_required
def custodianViewAllPremium():
    if current_user.role != "custodian":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    result = []
    try:
        result = custodian_controller.get_all_premium()
    except ValueError:
        flash("Unable to get premium information. Please try again later")
    return render_template('custodian/viewAllPremium.html', premiumpayments=result,
                           title='View Premium', name=current_user.username)
