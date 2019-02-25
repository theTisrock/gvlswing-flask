#  any flask app instance may use this configuration. It is external to the application.
#  All configuration details go here and an application instance grabs and loads them.
import os


class Configuration(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "fall_back_secret_key"
