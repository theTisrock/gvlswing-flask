# __init__

# code

# end init

app = Flask(__name__)

app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "admin_login"


from gvlswing_app import routes, models, errors  # this line avoids a circular dependency
