# entry point

# Created by Chris Torok using Miguel Grinbergs Flask Mega Tutorial on Udemy
# Tutorial: https://www.udemy.com/flask-mega-tutorial/

from gvlswing_app import app, db  # flask obtains the application instance here
from gvlswing_app.models import Administrator, ActivityLog


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'admin': Administrator, 'activity_log': ActivityLog}

# end entry point
