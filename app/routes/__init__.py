from app.routes.product_router import product_blueprint
from app.routes.user_router import user_blueprint

# List of all blueprints
blueprints = [
    product_blueprint,
    user_blueprint,
]

def register_blueprints(app):
    """
    Registers all blueprints to the given app instance.
    """
    for blueprint in blueprints:
        app.register_blueprint(blueprint)