
from flask import Flask
from app.routes import load_routes

def create_app():
    app = Flask(__name__)
    load_routes(app)
    return app
