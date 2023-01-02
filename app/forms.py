from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, EmailField, PasswordField, FloatField, TextAreaField
from wtforms.validators import DataRequired, Email, NumberRange, Length, ValidationError


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


class ProductForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=400)])
    price = FloatField("Price", validators=[
                       DataRequired(), NumberRange(min=0)])
    description = TextAreaField("Description")
    submit = SubmitField()


class AddressForm(FlaskForm):
    fullname = StringField("Fullname", validators=[
                           DataRequired(), Length(max=1000)])
    address = StringField("Address", validators=[
                          DataRequired(), Length(max=1000)])
    building = StringField(
        "Building", validators=[Length(max=100)])
    city = StringField("City", validators=[DataRequired(), Length(max=1000)])
    state = StringField("State", validators=[Length(max=1000)])
    zipcode = StringField("Zipcode", validators=[
                          DataRequired(), Length(min=6, max=10)])
    region = StringField("Region", validators=[
                         DataRequired(), Length(max=1000)])
    phone = StringField("Phone", validators=[
        DataRequired(), Length(min=10, max=10)])
    submit = SubmitField()
