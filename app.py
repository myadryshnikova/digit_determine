from flask import Flask, Blueprint

from digit_routes import digits_blueprint


def create_app():
    """Application factory, used to create application"""
    app = Flask(__name__)

    # without this /feeds will work but /feeds/ with the slash at the end won't
    app.url_map.strict_slashes = False
    register_blueprints(app)
    return app


def register_blueprints(app):
    """Register all blueprints for application"""
    api_blueprint = Blueprint('api', __name__, url_prefix='/api')
    api_blueprint.register_blueprint(digits_blueprint)
    app.register_blueprint(api_blueprint)
