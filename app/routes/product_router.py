from flask import Blueprint, request
from app.controllers.product_controller import (
    get_products,
    get_product,
    add_product,
    update_product,
    delete_product,
)

# Create a Blueprint instance for the product routes
product_blueprint = Blueprint("product", __name__)

# Route to get all products
product_blueprint.route("/products", methods=["GET"])(get_products)

# Route to get a specific product by ID
product_blueprint.route("/product/<int:id>", methods=["GET"])(get_product)

# Route to create a new product
product_blueprint.route("/product/create", methods=["GET", "POST"])(add_product)

# Route to update an existing product
product_blueprint.route("/product/edit/<int:id>", methods=["GET", "POST"])(
    update_product
)

# Route to delete a product
product_blueprint.route("/product/delete/<int:id>", methods=["POST"])(delete_product)
