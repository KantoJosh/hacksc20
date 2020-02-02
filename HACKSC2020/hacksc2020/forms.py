from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField("Username",
                            validators = [DataRequired(),Length(min=2,max=20)])
    email = StringField("Email",
                            validators = [DataRequired(),Email()])

    password = PasswordField("Password",
                            validators = [DataRequired()])
    confirm = PasswordField("Confirm password",
                            validators = [DataRequired(),EqualTo('password')])

    submit = SubmitField("Sign up")


class LoginForm(FlaskForm):
    email = StringField("Email",
                            validators = [DataRequired(),Email()])

    password = PasswordField("Password",
                            validators = [DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")


class DropdownForm(FlaskForm):
    quantity = SelectField('Quantity',choices=[(str(i),str(i)) for i in range(5)])