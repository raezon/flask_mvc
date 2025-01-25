from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman


# Initialize the database
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # Initialize the Talisman security extension
    talisman = Talisman(app)

    # Load configurations
    app.config.from_object("app.config.Config")

    # Initialize plugins
    db.init_app(app)

    # Register blueprints/routes
    from app.routes import main

    app.register_blueprint(main)

    return app
