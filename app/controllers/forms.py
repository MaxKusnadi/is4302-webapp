from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField(label='Role', choices=[('customer', 'Customer'),
                                              ('company', 'Company'),
                                              ('regulator', 'Regulator'),
                                              ('custodian', 'Custodian')])
    submit = SubmitField('Signup')


class CustomerRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    salary = IntegerField('Salary', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Signup')


class ReimbursementForm(FlaskForm):
    claim = StringField('Claim ID', validators=[DataRequired()])
    reimbtype = SelectField(label='Reimbursement Code', choices=[('INC1', 'INC1'),
                                              ('INC2', 'INC2')])
    submit = SubmitField('Submit Reimbursement')
