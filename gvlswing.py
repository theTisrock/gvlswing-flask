# entry point

from gvlswing_app import app, db  # flask obtains the application instance here
from gvlswing_app.models import Administrator


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'admin': Administrator}

# end entry point
