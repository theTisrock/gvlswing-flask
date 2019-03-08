# models for the gvlswing.db
from gvlswing_app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Administrator(UserMixin, db.Model):
    """
        Administrator accounts for changing content throughout the website.
        The "role" attribute will have two types: owners, staff
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), nullable=False)
    activities = db.relationship('ActivityLog', backref='admin', lazy='dynamic')
    # places virtual admin column in ActivityLog table

    def __repr__(self):
        return f"<Admin: {self.username} Role: {self.role}>"

    def set_password(self, password_entered):  # upon registration
        self.password_hash = generate_password_hash(password_entered)

    def check_password(self, password_entered):  # upon login
        # go set up Administrator model with UserMixin
        pass


@login.user_loader  # upon request. Attempts to load either anonymous user or logged in user, probably into current_user
def attempt_load_user(id):
    return Administrator.query.get(int(id))
# end Administrator


class ActivityLog(db.Model):
    """
        The ActivityLog should record...
        who modified content, when they modified it, and which content was modified.
    """
    log_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    admin_id = db.Column(db.Integer, db.ForeignKey('administrator.id'))
    # how do I track which content they modified??

    def __repr__(self):
        return f"<Mod Id: {self.log_id} timestamp: {self.timestamp}"
