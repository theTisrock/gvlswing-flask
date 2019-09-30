# routes
from gvlswing import app


@app.route(rule="/", methods=['GET'])
def main():
    return "hello"

# end
