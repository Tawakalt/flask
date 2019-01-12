
def load_routes(app):
    @app.route("/")
    def hello():
        return "Hello World!"