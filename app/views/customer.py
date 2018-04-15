from flask import request, redirect, url_for, flash, render_template
from flask_login import current_user, login_required

from app import app
from ..controllers.forms import FileClaimForm
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
            flash("test")
            return redirect(url_for('login'))
        return redirect(url_for('index'))
    return render_template('customer/fileClaim.html', form=form, title='File Claim', name=current_user.username)

@app.route('/view-policy', methods=["GET","POST"])
@login_required
def view_policy():
    if current_user.role.lower() != "customer":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    poldata = customer_controller.get_policies()
    custdata = customer_controller.get_own_data(current_user.username)

    return render_template('customer/viewPolicy.html', title='View My Policies', poldata=poldata, custdata=custdata)

@app.route('/submit-policy-appl', methods=["GET","POST"])
@login_required
def submit_policy_appl():
    if current_user.role.lower() != "customer":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    policyid = request.args.get("policy")
    customer_controller.submit_policy_appl(current_user.username, policyid)

    return redirect(url_for('view_policy'))

@app.route('/submit-premium', methods=["GET", "POST"])
@login_required
def submit_premium_payment():
    return render_template('customer/submitPremiumPayment.html', title='Submit Premium Payment', name=current_user.username)
