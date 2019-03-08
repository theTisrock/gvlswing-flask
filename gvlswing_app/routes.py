# calling render_template here should not cause any circular imports since all rendering is done here.
# ???
# One consideration: should render_template be implemented in a subsequent call stack.
# AKA: should underlying methods use render_template as their return type or should that return type
# be kept at top level
# ???

from gvlswing_app import app  # use the flask app object created in __init__.py
from gvlswing_app.forms import LoginForm
from flask import render_template, url_for, redirect
from flask_login import current_user, login_user
from gvlswing_app.models import ActivityLog, Administrator

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/admin")
def admin_panel():
    """
    Load the administration panel if the administrator is logged in. If not, redirect to login.
    :return:
    """
    # if current_user.is_authenticated():
    #     return render_template(url_for('admin-panel'))
    return redirect(url_for("index"))


@app.route("/admin/login")
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    else:
        form = LoginForm()
    return render_template("login.html", form=form)

# end routes
