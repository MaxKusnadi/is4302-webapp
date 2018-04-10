from flask import redirect, url_for, flash, render_template
from flask_login import current_user

from app import app
from ..controllers.forms import LoginForm, RegistrationForm
from ..controllers.login import LoginController

login_controller = LoginController()


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        try:
            login_controller.login(username, password)
        except ValueError:
            flash("Username not found. Please Register")
            return redirect(url_for('login'))
        except AttributeError:
            flash("Wrong password")
            return redirect(url_for('login'))
        return redirect(url_for('index'))
    return render_template('login.html', form=form, title='Login')


@app.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        role = form.role.data
        try:
            login_controller.sign_up(username, password, role)
        except ValueError:
            flash("Username exists. Please Login")
            return redirect(url_for('register'))
        except AttributeError:
            flash("Can't register in the blockchain")
            return redirect(url_for('register'))
        return redirect(url_for('index'))
    return render_template('register.html', form=form, title='Sign Up')


@app.route('/')
@app.route('/index')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    if current_user.role.lower() == 'customer':
        return render_template('home.html', title='Customer Portal Home', name=current_user.username)
    elif current_user.role.lower() == 'company':
        return render_template('companyHome.html', title='Company Portal Home', name=current_user.username)
    elif current_user.role.lower() == 'custodian':
        return render_template('home.html', title='Custodian Portal Home', name=current_user.username)
    elif current_user.role.lower() == 'regulator':
        return render_template('home.html', title='Regulator Portal Home', name=current_user.username)


@app.route('/logout')
def logout():
    login_controller.logout()
    return redirect(url_for('login'))
