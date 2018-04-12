from flask import redirect, url_for, flash, render_template
from flask_login import current_user, login_required

from app import app
from ..controllers.forms import FileClaimForm
from ..controllers.login import LoginController
from ..controllers.customer import CustomerController

login_controller = LoginController()
customer_controller = CustomerController()


@app.route('/fileClaim', methods=["GET", "POST"])
@login_required
def file_claim():
    form = FileClaimForm()
    if form.validate_on_submit():
        claimDesc = form.claimDesc.data
        username = current_user.username
        try:
            customer_controller.file_claim(username, claimDesc)
        except ValueError:
            flash("test")
            return redirect(url_for('login'))
        return redirect(url_for('index'))
    return render_template('fileClaim.html', form=form, title='File Claim', name=current_user.username)
