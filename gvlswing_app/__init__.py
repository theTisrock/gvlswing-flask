from flask import Flask

app = Flask(__name__)

from gvlswing_app import routes  # this line avoids a circular dependency
