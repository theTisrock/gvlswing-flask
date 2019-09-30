# routes
from gvlswing import app
from flask import render_template


@app.route(rule="/", methods=['GET'])
def main():
    return render_template("landing.html")

# end
