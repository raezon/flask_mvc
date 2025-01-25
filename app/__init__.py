from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman


# Initialize the database (but don't initialize it here)
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # Initialize the Talisman security extension
    # Initialize Flask-Talisman
    talisman = Talisman(
        app,
        content_security_policy={
            "default-src": ["'self'"],
            "style-src": ["'self'", "https://stackpath.bootstrapcdn.com"],
        },
    )

    # Load configurations
    app.config.from_object("app.config.Config")

    # Initialize plugins
    db.init_app(app)

    # Register blueprints/routes
    from app.routes.product_router import product_blueprint

    app.register_blueprint(product_blueprint)

    return app
