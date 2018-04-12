from flask import redirect, url_for, flash, render_template
from flask_login import current_user, login_required

from app import app
from ..controllers.regulator import regulator_controller


@app.route('/regulator-home', methods=["GET"])
@login_required
def regulator_home():
    if current_user.role != "regulator":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    result = []
    try:
        result = regulator_controller.get_pending_customer_registration()
    except ValueError:
        flash("Unable to get user information. Please try again later")
    return render_template('regulator/home.html', customers=result, title='Regulator Portal Home', name=current_user.username)


@app.route('/approve-registration/<username>', methods=["GET"])
@login_required
def approve_registration(username):
    if current_user.role != "regulator":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    try:
        regulator_controller.approve_registration(username)
    except ValueError:
        flash("Unable to approve registration. Please try again later")
    return redirect(url_for('regulator_home'))


@app.route('/reject-registration/<username>', methods=["GET"])
@login_required
def reject_registration(username):
    if current_user.role != "regulator":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    try:
        regulator_controller.reject_registration(username)
    except ValueError:
        flash("Unable to reject registration. Please try again later")
    return redirect(url_for('regulator_home'))
