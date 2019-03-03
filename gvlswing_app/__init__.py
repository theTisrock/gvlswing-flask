# application initialization file - read in configuration, setup database with migrations


from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from gvlswing_app import routes, models  # this line avoids a circular dependency
