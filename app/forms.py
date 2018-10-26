from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    passwd = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign In")

class NewPasswdForm(FlaskForm):
    oldpasswd = PasswordField("Old password", validators=[DataRequired()])
    newpasswd = PasswordField("New password", validators=[DataRequired()])
    retpasswd = PasswordField("Retype new password", validators=[DataRequired()])
    submit = SubmitField("Change")

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    passwd = PasswordField("Password", validators=[DataRequired()])
    retpasswd = PasswordField("Retype password", validators=[DataRequired()])
    submit = SubmitField("Register")

