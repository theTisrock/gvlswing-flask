# errors
from gvlswing_app import app


@app.errorhandler(404)
def http_not_found_error(error):
    return "What you requested doesn't exist.", 404


@app.errorhandler(500)
def http_application_error(error):
    return "It's not you ... it's me", 500

# end errors
