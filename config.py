#  any flask app instance may use this configuration. It is external to the application.
#  All configuration details go here and an application instance grabs and loads them.
import os

base_directory = os.path.abspath(os.path.dirname(__file__))


class Configuration(object):
    # secret key configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or "fall_back_secret_key"

    # database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "sqlite:///" + \
                              os.path.join(base_directory, 'gvlswing.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
