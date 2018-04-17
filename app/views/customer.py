from flask import request, redirect, url_for, flash, render_template
from flask_login import current_user, login_required

from app import app
from ..controllers.forms import FileClaimForm, SubmitPremiumPaymentForm, ViewMoneyPoolReimbursedForm
from ..controllers.customer import customer_controller


@app.route('/customer-home', methods=["GET"])
@login_required
def customer_home():
    if current_user.role.lower() != "customer":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    return render_template('customer/home.html', title='Customer Home', name=current_user.username)


@app.route('/view-my-policy', methods=["GET", "POST"])
@login_required
def view_my_policies():
    if current_user.role.lower() != "customer":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    data = customer_controller.get_own_data(current_user.username)
    return render_template('customer/viewMyPolicies.html', title='View My Policies',
                           cust_policy=data, name=current_user.username)


@app.route('/view-money-pool', methods=["GET", "POST"])
@login_required
def view_money_pool():
    if current_user.role.lower() != "customer":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    data = customer_controller.view_money_pool(current_user.username)
    return render_template('customer/viewMoneyPool.html', title='View Policies Money Pool',
                           policy_money_pool=data, name=current_user.username)


@app.route('/view-money-pool-reimbursed', methods=["GET", "POST"])
@login_required
def view_money_pool_reimbursed():
    if current_user.role.lower() != "customer":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))

    form = ViewMoneyPoolReimbursedForm()
    if form.validate_on_submit():
        result = []
        policyid = form.policyid.data
        try:
            result = customer_controller.view_money_pool_reimbursed(policyid)
        except ValueError:
            flash("Couldnt view money pool reimbused")
            return redirect(url_for('login'))
        return render_template('customer/viewMoneyPoolReimbursed.html', moneyPool=result,
                               title='View Money Pool Reimbursed', name=current_user.username)
    return render_template('customer/submitMoneyPoolReimbursed.html', form=form,
                           title='Submit Money Pool Reimbursed', name=current_user.username)


@app.route('/file-claim', methods=["GET", "POST"])
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
    return render_template('customer/fileClaim.html', form=form, title='File Claim',
                           policyid=policyid, name=current_user.username)


@app.route('/view-policy', methods=["GET", "POST"])
@login_required
def view_policy():
    if current_user.role.lower() != "customer":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    poldata = customer_controller.get_policies()
    custdata = customer_controller.get_own_data(current_user.username)
    return render_template('customer/viewPolicy.html', title='View My Policies', poldata=poldata,
                           custdata=custdata, name=current_user.username)


@app.route('/submit-policy-appl', methods=["GET", "POST"])
@login_required
def submit_policy_appl():
    if current_user.role.lower() != "customer":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    policyid = request.args.get("policy")
    customer_controller.submit_policy_appl(current_user.username, policyid)
    flash("Policy Application Submitted")
    return redirect(url_for('view_policy'))


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
