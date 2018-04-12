from flask import redirect, url_for, flash, render_template
from flask_login import current_user
from flask import request

from app import app
from ..controllers.forms import ReimbursementForm
from ..controllers.company import CompanyController
from ..controllers.login import LoginController

login_controller = LoginController()
company_controller = CompanyController()


@app.route('/companyRegisterCust')
def companyRegisterCust():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return render_template('companyRegisterCust.html', title='Register Customer', name=current_user.username)


@app.route('/companyRegisterPolicy')
def companyRegisterPolicy():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return render_template('companyRegisterPolicy.html', title='Register Policy', name=current_user.username)

@app.route('/companyViewPolicyAppl', methods=["GET", "POST"])
def companyViewPolicyAppl():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    data = company_controller.get_all_policy_appl()

    return render_template('companyViewPolicyAppl.html', title='View All Policy Applications', appl=data)

@app.route('/companyApprovePolicyAppl', methods=["GET","POST"])
def companyApprovePolicyAppl():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    applyID = request.args.get("id")
    company_controller.register_cust_policy(applyID)

    return redirect(url_for('companyViewPolicyAppl'))

@app.route('/companyRejectPolicyAppl', methods=["GET","POST"])
def companyRejectPolicyAppl():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    applyID = request.args.get("id")
    company_controller.reject_policy_appl(applyID)

    return redirect(url_for('companyViewPolicyAppl'))

@app.route('/companyViewClaim', methods=["GET","POST"])
def companyViewClaim():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    data = company_controller.get_all_claim()

    return render_template('companyViewClaim.html', title='View All Claim Requests', claim=data)

@app.route('/companyApproveClaim', methods=["GET","POST"])
def companyApproveClaim():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    claimID = request.args.get("id")
    company_controller.approve_claim(claimID)

    return redirect(url_for('companyViewClaim'))

@app.route('/companyRejectClaim', methods=["GET","POST"])
def companyRejectClaim():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    claimID = request.args.get("id")
    company_controller.reject_claim(claimID)

    return redirect(url_for('companyViewClaim'))

@app.route('/companySubmitReimb', methods=["GET","POST"])
def companySubmitReimb():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    claimID = request.args.get("id")

    form = ReimbursementForm()
    if form.validate_on_submit():
        claim = form.claim.data
        reimbtype = form.reimbtype.data
        try:
            company_controller.submit_reimb(claim, reimbtype)
        except AttributeError:
            flash("Can't submit reimbursement in the blockchain")
            return redirect(url_for('companyViewClaim'))
        return redirect(url_for('companyViewClaim'))
    return render_template('companySubmitReimb.html', form=form, claim=claimID, title='Submit Reimbursement')
