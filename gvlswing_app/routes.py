# calling render_template here should not cause any circular imports since all rendering is done here.
# ???
# One consideration: should render_template be implemented in a subsequent call stack.
# AKA: should underlying methods use render_template as their return type or should that return type
# be kept at top level
# ???

from gvlswing_app import app  # use the flask app object created in __init__.py
from gvlswing_app.forms import LoginForm
from flask import render_template, url_for, redirect, flash, request
from flask_login import current_user, login_user
from gvlswing_app.models import ActivityLog, Administrator

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/admin")  # the login panel after access has been granted
def admin_panel():
    """
    Load the administration panel if the administrator is logged in. If not, redirect to login.
    """
    if not current_user.is_authenticated:
        flash("Woops!")
        return redirect(url_for("index"))
    flash("You are logged in as admin.")
    return render_template("index")


@app.route("/admin/login", methods=['GET', 'POST'])  # the login form to grant access
def admin_login():
    if current_user.is_authenticated:
        flash("Um ... you're already logged in")
        return redirect(url_for("admin_panel"))
    elif request == 'GET':  # log them in
        form = LoginForm()
        form.validate_on_submit()
    elif request == 'POST':  # they are trying to submit a login form

    return render_template("login.html", form=form)

# end routes
