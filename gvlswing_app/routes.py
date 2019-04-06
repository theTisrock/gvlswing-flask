# calling render_template here should not cause any circular imports since all rendering is done here.
# ???
# One consideration: should render_template be implemented in a subsequent call stack.
# AKA: should underlying methods use render_template as their return type or should that return type
# be kept at top level
# ???

from gvlswing_app import app, db  # use the flask app object created in __init__.py
from gvlswing_app.urls import Action, URL
from gvlswing_app.forms import LoginForm, RegistrationForm
from gvlswing_app.models import Administrator
from gvlswing_app.cms_no_db import CMSSimple
from flask import render_template, url_for, redirect, flash, request
from flask_login import current_user, login_user, logout_user, login_required


@app.route(URL.root)
@app.route(URL.index)
def index():
    content = None
    try:
        content = CMSSimple.get_json_content("welcome_box.json")['data']
    except FileNotFoundError:
        flash("No json data found for welcome box.")
        return render_template("index.html")
    return render_template("index.html", title="GVL Swing Dance", welcome_data=content)


@app.route(URL.admin_control_panel)  # admin landing
@login_required
def admin_panel():
    """
    Load the administration panel if the administrator is logged in. If not, redirect to login.
    """
    return "Admin Control Panel: give selection of page & content to edit. Show admin activity log."

    # return "Something went wrong in admin_panel() procedure"


@app.route(URL.admin_login, methods=['GET', 'POST'])  # the login form to grant access
def admin_login():
    form = LoginForm()

    if current_user.is_authenticated:
        return redirect(url_for(Action.admin_panel))

    if current_user.is_anonymous and request.method == 'GET':  # allow attempted log in
        return render_template("login.html", form=form)

    if form.validate_on_submit() and request.method == 'POST':  # they are trying to submit a login form
        user = Administrator.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            flash("Successful login!")
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for(Action.admin_panel, username=user.username))
        else:
            flash("Failed login attempt.")
            return redirect(url_for(Action.admin_panel))

    return "Something went wrong in the admin_login() procedure."


@app.route(URL.logout)
def logout():
    logout_user()
    flash("Logged out")
    return redirect(url_for(Action.index))


@app.route(URL.admin_register, methods=['GET', 'POST'])
def admin_register():
    form = RegistrationForm()
    if current_user.is_authenticated:
        flash("You're already logged in")
        return redirect(url_for(Action.admin_panel))
    elif request.method == 'GET' and current_user.is_anonymous:
        return render_template("register.html", form=form)
    elif form.validate_on_submit() and request.method == 'POST':
        user = Administrator(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        # user.set_role("dancer")
        db.session.add(user)
        db.session.commit()  # commit at end of successful request
        flash("Registration successful!")
        return redirect(url_for(Action.index))
    elif not form.validate_on_submit() and request.method == 'POST':
        flash("Registration failed")
        return render_template("register.html", form=form)

    return "Something went wrong with admin_register() procedure"


# end routes
