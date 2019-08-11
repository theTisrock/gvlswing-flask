#  web forms collection
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from gvlswing_app.models import Administrator
from gvlswing_app.cms_no_db import Content

# contents


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
    prepopulate = Content.get_json_content("welcome_box.json")
    quantity_dance_duration = StringField("Dance Duration",
                                          validators=[DataRequired()],
                                          default=prepopulate['data']['quantity_time']['dance'])
    quantity_lesson_duration = StringField("Lesson(s) Duration",
                                           validators=[DataRequired()],
                                           default=prepopulate['data']['quantity_time']['lessons'])
    description_price = StringField("Price and/or description",
                                    validators=[DataRequired()],
                                    default=prepopulate['data']['description_price'])
    event_frequency = StringField("Frequency. Ex: Every, every other",
                                  validators=[DataRequired()],
                                  default=prepopulate['data']['frequency'])
    days_of_week = StringField("Day(s) of the week",
                               validators=[DataRequired()],
                               default=prepopulate['data']['days_of_week'])
    timespan_start = StringField("Start Time",
                                 validators=[DataRequired()],
                                 default=prepopulate['data']['timespan']['start_time'])
    timespan_stop = StringField("Stop Time",
                                validators=[DataRequired()],
                                default=prepopulate['data']['timespan']['end_time'])
    submit = SubmitField("Save Changes")

# end forms
