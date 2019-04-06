#  web forms collection
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from gvlswing_app.models import Administrator


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

    def validate_username(self, username):  # flask-wtf validator
        found_match = Administrator.query.filter_by(username=username.data).first()
        if found_match is not None:
            raise ValidationError("Pick a different username.")

    def validate_email(self, email):  # flask-wtf validator
        found_match = Administrator.query.filter_by(email=email.data).first()
        if found_match is not None:
            raise ValidationError("Pick a different email.")


class CMSWelcomeForm(FlaskForm):
    quantity_dance_duration = StringField("Dance Duration")
    quantity_lesson_duration = StringField("Lesson(s) Duration")
    description_price = StringField("Price and/or description")
    event_frequency = StringField("Frequency. Ex: Every, every other")
    days_of_week = StringField("Day(s) of the week")
    timespan_start = StringField("Start Time")
    timespan_stop = StringField("Stop Time")
    submit = SubmitField("Save Changes")

# end forms
