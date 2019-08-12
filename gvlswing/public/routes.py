# public routes

from gvlswing.public import bp
from flask import render_template, flash
from cms import CMS


@bp.route("/", methods=['GET'])
def index():
    content = None
    try:
        content = CMS.read("index.json")['data']
    except FileNotFoundError:
        flash("No json data found for welcome box.")
        return render_template("index.html")
    return render_template("index.html", title="GVL Swing Dance", welcome_data=content)

# end
