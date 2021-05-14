"""Initialize app."""
import sys
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
# from .import_data import import_boats, import_users


db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    """Construct the core app object."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import root
        from . import api
        from . import pages
        from . import auth
        from .assets import compile_static_assets
        from .import_data import import_boats, import_users, import_locations, import_races, import_boats, import_boat_types

        # Register Blueprints
        app.register_blueprint(root.root_bp)
        app.register_blueprint(api.api_bp)
        app.register_blueprint(pages.pages_bp)
        app.register_blueprint(auth.auth_bp)

        # Create Database Models
        db.create_all()

        # Import some test data

        try:
            import_boat_types()
        except:
            print("Unexpected error:", sys.exc_info())
            print("There was an error importing boat types. Data probably already exists")
        try:
            import_users()
        except:
            print("Unexpected error:", sys.exc_info())
            print("There was an error importing users. Data probably already exists")
        try:
            import_locations()
        except:
            print("Unexpected error:", sys.exc_info())
            print("There was an error importing locations. Data probably already exists")
        try:
            import_races()
        except:
            print("Unexpected error:", sys.exc_info())
            print("There was an error importing races. Data probably already exists")
        try:
            import_boats()
        except:
            print("Unexpected error:", sys.exc_info())
            print("There was an error importing races. Data probably already exists")

        # Compile static assets
        if app.config['FLASK_ENV'] == 'development':
            compile_static_assets(app)

        return app
