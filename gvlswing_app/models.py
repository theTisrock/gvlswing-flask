# models for the gvlswing.db
from gvlswing_app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Administrator(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    email = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"<[Admin]: {self.username} [Email]: {self.email}>"

    # setters
    def set_email(self, email_entered):
        self.email = email_entered

    def set_password(self, password_entered):  # upon registration
        self.password_hash = generate_password_hash(password_entered)

    # getters
    def get_email(self):
        return self.email

    def get_username(self):
        return self.username

    # def get_role(self):
    #     return self.role

    # checkers
    def check_password(self, password_entered):  # upon login
        # go set up Administrator model with UserMixin
        return check_password_hash(self.password_hash, password_entered)


@login.user_loader  # upon request. Attempts to load either anonymous user or logged in user, probably into current_user
def attempt_load_user(id):
    return Administrator.query.get(int(id))

# end models
