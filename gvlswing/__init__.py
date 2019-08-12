# __init__ : public application blueprinting
from flask import Flask
from config import Configuration

from flask_login import LoginManager

login = LoginManager()


def create_app(config=Configuration):
    app = Flask(__name__)  # instantiate

    app.config['SECRET_KEY'] = Configuration.SECRET_KEY

    login.init_app(app)  # register extensions

    from gvlswing.public import bp as pub_bp
    app.register_blueprint(pub_bp)

    return app

# end public application blueprinting
