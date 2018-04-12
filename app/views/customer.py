from flask import redirect, url_for, flash, render_template
from flask_login import current_user

from app import app
from ..controllers.forms import FileClaimForm
from ..controllers.login import LoginController
from ..controllers.customer import CustomerController

login_controller = LoginController()
customer_controller = CustomerController()


@app.route('/fileClaim', methods=["GET", "POST"])
def fileClaim():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    #form = FileClaimForm()
    #if form.validate_on_submit():
        #claimDesc = form.ClaimDesc.data
        #try:
            #customer_controller.file_claim(claimDesc)
        #except AttributeError:
            #flash("test")
            #return redirect(url_for('login'))
        #return redirect(url_for('index'))
    return render_template('fileClaim.html', title='File Claim', name=current_user.username)
    #return render_template('fileClaim.html', form=form, title='File CLaim')
