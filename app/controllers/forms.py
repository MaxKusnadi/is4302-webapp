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


class FileClaimForm(FlaskForm):
    #assume claim description to be legitimate
    claimDesc = StringField('Claim Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class SubmitPremiumPaymentForm(FlaskForm):
    policyid = StringField('Policy Id', validators=[DataRequired()])
    submit = SubmitField('Confirm Payment')


class ViewMoneyPoolReimbursedForm(FlaskForm):
    policyid = StringField('Policy Id', validators=[DataRequired()])
    submit = SubmitField('View')


class RegisterPolicyForm(FlaskForm):
    policy_id = StringField('Policy ID', validators=[DataRequired()])
    duration = IntegerField('Duration in month', validators=[DataRequired()])
    submit = SubmitField('Register')


class TerminateCustomerPolicyForm(FlaskForm):
    policy_id = StringField('Policy ID', validators=[DataRequired()])
    cust_id = StringField('Customer ID', validators=[DataRequired()])
    submit = SubmitField("Terminate")
