from app.controllers.product_controller import product_blueprint

# List of all blueprints
blueprints = [
    product_blueprint
]

def register_blueprints(app):
    """
    Registers all blueprints to the given app instance.
    """
    for blueprint in blueprints:
        app.register_blueprint(blueprint)