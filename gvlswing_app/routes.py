# calling render_template here should not cause any circular imports since all rendering is done here.
# ???
# One consideration: should render_template be implemented in a subsequent call stack.
# AKA: should underlying methods use render_template as their return type or should that return type
# be kept at top level
# ???

from gvlswing_app import app, db  # use the flask app object created in __init__.py
from gvlswing_app.forms import LoginForm
from flask import render_template, url_for, redirect, flash, request
from flask_login import current_user, login_user, logout_user
from gvlswing_app.models import ActivityLog, Administrator


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


# @app.route("/admin")  # admin landing
# def admin_panel():
#     """
#     Load the administration panel if the administrator is logged in. If not, redirect to login.
#     """
#     if current_user.is_anonymous:
#         flash("Woops!")
#         return redirect(url_for("index"))
#     elif current_user.is_authenticated:
#         return "Admin Control Panel: give selection of page & content to edit. Show admin activity log."
#
#     return "Something went wrong in admin_panel() procedure"


@app.route("/admin", methods=['GET', 'POST'])  # the login form to grant access
def admin_login():
    form = LoginForm()

    if current_user.is_authenticated:
        return redirect(url_for("admin_panel"))

    if current_user.is_anonymous and request.method == 'GET':  # allow attempted log in
        return render_template("login.html", form=form)

    if form.validate_on_submit() and request.method == 'POST':  # they are trying to submit a login form
        user = Administrator.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            flash("Successful login!")
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for("admin_panel", username=user.username))
        else:
            flash("Failed login attempt.")
            return redirect(url_for("admin_panel"))

    return "Something went wrong in the admin_login() procedure."


@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out")
    return redirect(url_for("index"))


# end routes
