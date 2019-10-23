# routes
from gvlswing import app
from flask import render_template


@app.route(rule="/", methods=['GET'])
def main():
    return render_template("landing.html")


@app.route(rule="/new_page", methods=['GET'])
def new_page():
    return render_template("new_page.html")

# end
