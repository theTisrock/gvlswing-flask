# calling render_template here should not cause any circular imports since all rendering is done here.
# ???
# One consideration: should render_template be implemented in a subsequent call stack.
# AKA: should underlying methods use render_template as their return type or should that return type
# be kept at top level
# ???

from gvlswing_app import app  # use the flask app object created in __init__.py
from flask import render_template
from gvlswing_app.forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/login")
@app.route("/admin")
def login():
    form = LoginForm()
    return render_template("login.html", title="Log In", form=form)
