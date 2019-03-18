#  web forms collection
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from gvlswing_app.models import Administrator, ActivityLog


class LoginForm(FlaskForm):
    # static components
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember me")
    submit = SubmitField()


class RegistrationForm(FlaskForm):
    # static components
    username = StringField("username", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])
    password_confirm = PasswordField("confirm password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField()

    def validate_username(self, username):
        found_match = Administrator.query.filter_by(username=username.data).first()
        if found_match is not None:
            raise ValidationError("Pick a different username.")

    def validate_email(self, email):
        found_match = Administrator.query.filter_by(email=email.data).first()
        if found_match is not None:
            raise ValidationError("Pick a different email.")


# end forms
