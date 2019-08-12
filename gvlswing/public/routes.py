# public routes

from gvlswing.public import bp
from flask import render_template


@bp.route("/", methods=['GET'])
def index():
    return render_template("index.html")

# end
