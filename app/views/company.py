from flask import request, redirect, url_for, flash, render_template
from flask_login import login_required, current_user

from app import app
from ..controllers.forms import ReimbursementForm, CustomerRegistrationForm
from ..controllers.company import company_controller


@app.route('/company-home')
@login_required
def company_home():
    if current_user.role != "company":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    return render_template('company/home.html', title='Company Portal Home', name=current_user.username)


@app.route('/register/customer', methods=["GET", "POST"])
@login_required
def register_customer():
    if current_user.role != "company":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    form = CustomerRegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        salary = form.salary.data
        try:
            company_controller.register_customer(username, password, salary)
        except ValueError:
            flash("Username exists.")
            return redirect(url_for('register_customer'))
        except AttributeError:
            flash("Can't register in the blockchain")
            return redirect(url_for('register_customer'))
        flash("Customer '{}' registration is successful".format(username))
        return redirect(url_for('index'))
    return render_template('company/registerCust.html', form=form, title='Register Customer', name=current_user.username)


# TODO
@app.route('/register/policy', methods=["GET", "POST"])
@login_required
def register_policy():
    if current_user.role != "company":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    return render_template('company/registerPolicy.html', title='Register Policy', name=current_user.username)


@app.route('/policy')
@login_required
def view_policy_application():
    if current_user.role != "company":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    data = company_controller.get_all_policy_appl()
    return render_template('company/viewPolicyAppl.html', title='View All Policy Applications', appl=data)


@app.route('/approve-policy')
@login_required
def approve_policy_application():
    if current_user.role != "company":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    applyID = request.args.get("id")
    company_controller.register_cust_policy(applyID)

    return redirect(url_for('view_policy_application'))


@app.route('/reject-policy')
@login_required
def reject_policy_application():
    if current_user.role != "company":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    applyID = request.args.get("id")
    company_controller.reject_policy_appl(applyID)

    return redirect(url_for('view_policy_application'))


@app.route('/claim')
@login_required
def view_claim():
    if current_user.role != "company":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    data = company_controller.get_all_claim()

    return render_template('company/viewClaim.html', title='View All Claim Requests', claim=data)


@app.route('/approve-claim')
@login_required
def approve_claim():
    if current_user.role != "company":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    claimID = request.args.get("id")
    company_controller.approve_claim(claimID)

    return redirect(url_for('view_claim'))


@app.route('/reject-claim')
@login_required
def reject_claim():
    if current_user.role != "company":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    claimID = request.args.get("id")
    company_controller.reject_claim(claimID)

    return redirect(url_for('view_claim'))


@app.route('/reimbursement', methods=["GET","POST"])
@login_required
def submit_reimbursement():
    if current_user.role != "company":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    claimID = request.args.get("id")

    form = ReimbursementForm()
    if form.validate_on_submit():
        claim = form.claim.data
        reimbtype = form.reimbtype.data
        try:
            company_controller.submit_reimb(claim, reimbtype)
        except AttributeError:
            flash("Can't submit reimbursement in the blockchain")
            return redirect(url_for('view_claim'))
        return redirect(url_for('view_claim'))
    return render_template('company/submitReimb.html', form=form, claim=claimID, title='Submit Reimbursement')

@app.route('/view-cashout')
@login_required
def view_cashout():
    if current_user.role != "company":
        flash("Not authorized to do such action")
        return redirect(url_for('index'))
    cust = company_controller.get_all_cust()

    return render_template('company/viewCashOut.html', title='View Available CashOuts', custpol=cust)
