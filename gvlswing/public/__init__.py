# public app subsection

from flask import Blueprint

bp = Blueprint("public", __name__)  # object now available for import

from gvlswing.public import routes  # routes module pulls in 'bp' instance and adds a route to it. importing routes here
# "pulls" the bp instance back up to this 'location' here

# end
