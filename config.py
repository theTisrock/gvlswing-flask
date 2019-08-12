#  any flask app instance may use this configuration. It is external to the application.
#  All configuration details go here and an application instance loads them.
import os

base_directory = os.path.abspath(os.path.dirname(__file__))


class Configuration(object):
    # secret key configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or "fall_back_secret_key"

