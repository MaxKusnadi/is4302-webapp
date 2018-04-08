from flask import redirect, url_for, flash, render_template
from flask_login import current_user

from app import app
from ..controllers.company import CompanyController
from ..controllers.login import LoginController

login_controller = LoginController()
company_controller = CompanyController();

@app.route('/companyHome')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return render_template('companyHome.html', title='Company Portal Home', name=current_user.username)

@app.route('/companyRegisterCust')
def companyRegisterCust():
    return render_template('companyRegisterCust.html', title='Register Customer', name=current_user.username)

@app.route('/companyRegisterPolicy')
def companyRegisterPolicy():
    return render_template('companyRegisterPolicy.html', title='Register Policy', name=current_user.username)

@app.route('/logout')
def logout():
    login_controller.logout()
    return redirect(url_for('login'))
