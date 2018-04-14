from flask import request, redirect, url_for, flash, render_template
from flask_login import current_user, login_required

from app import app
from ..controllers.forms import FileClaimForm, SubmitPremiumPaymentForm
from ..controllers.login import LoginController
from ..controllers.customer import customer_controller

login_controller = LoginController()

@app.route('/customer-home', methods=["GET"])
@login_required
def customer_home():
    if current_user.role.lower() != "customer":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    return render_template('customer/home.html', title='Customer Home', name=current_user.username)

@app.route('/view-my-policy', methods=["GET","POST"])
@login_required
def view_my_policies():
    if current_user.role.lower() != "customer":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    data = customer_controller.get_own_data(current_user.username)

    return render_template('customer/viewMyPolicies.html', title='View My Policies', cust_policy=data)

@app.route('/file-claim', methods=["GET","POST"])
@login_required
def file_claim():
    if current_user.role.lower() != "customer":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))

    policyid = request.args.get("id")

    form = FileClaimForm()
    if form.validate_on_submit():
        claimDesc = form.claimDesc.data
        username = current_user.username
        try:
            customer_controller.file_claim(policyid, username, claimDesc)
        except ValueError:
            flash("Couldnt file claim")
            return redirect(url_for('login'))
        flash("Claim Filed")
        return redirect(url_for('index'))
    return render_template('customer/fileClaim.html', form=form, title='File Claim', name=current_user.username)

@app.route('/submit-premium-payment', methods=["GET", "POST"])
@login_required
def submit_premium_payment():
    if current_user.role.lower() != "customer":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))

    form = SubmitPremiumPaymentForm()

    if form.validate_on_submit():
        policyid = form.policyid.data
        username = current_user.username
        try:
            customer_controller.submit_premium_payment(policyid, username)
        except ValueError:
            flash("Couldnt submit premium payment")
            return redirect(url_for('login'))
        flash("Payment is Confirmed")
        return redirect(url_for('index'))
    return render_template('customer/submitPremiumPayment.html', form=form, title='Submit Premium Payment', name=current_user.username)
