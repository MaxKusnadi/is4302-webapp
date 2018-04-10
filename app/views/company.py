from flask import redirect, url_for, flash, render_template
from flask_login import current_user

from app import app
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
