from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email


def validation_errors_formatter(form, validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = {
        form[field].label.text: error
        for field in validation_errors
        for error in validation_errors[field]
    }
    return errorMessages


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log in")


class SignupForm(FlaskForm):
    fullname = StringField("Full name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField()
