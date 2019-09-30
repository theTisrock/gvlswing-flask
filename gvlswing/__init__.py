# main application package init
from flask import Flask

app = Flask(__name__)

from gvlswing import routes

# end
