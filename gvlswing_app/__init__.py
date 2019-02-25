# application initialization file


from flask import Flask
from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

from gvlswing_app import routes  # this line avoids a circular dependency
