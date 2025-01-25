# app/routes.py
from flask import Blueprint, request, jsonify
from app.services.product_service import (
    create_new_product,
    fetch_product_by_id,
    fetch_all_products,
    modify_product,
    remove_product,
)

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return jsonify(message="Welcome to Flask with MySQL Boilerplate")


# Create a new product
@main.route("/product", methods=["POST"])
def add_product():
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")

    product = create_new_product(name, description, price)
    return (
        jsonify(
            {
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
            }
        ),
        201,
    )


# Get product by ID
@main.route("/product/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = fetch_product_by_id(product_id)
    if product:
        return jsonify(
            {
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
            }
        )
    return jsonify({"message": "Product not found"}), 404


# Get all products
@main.route("/products", methods=["GET"])
def get_all_products():
    products = fetch_all_products()
    return jsonify(
        [
            {
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
            }
            for product in products
        ]
    )


# Update product
@main.route("/product/<int:product_id>", methods=["PUT"])
def update_product_route(product_id):
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")

    product = modify_product(product_id, name, description, price)
    if product:
        return jsonify(
            {
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
            }
        )
    return jsonify({"message": "Product not found"}), 404


# Delete product
@main.route("/product/<int:product_id>", methods=["DELETE"])
def delete_product_route(product_id):
    product = remove_product(product_id)
    if product:
        return jsonify({"message": "Product deleted successfully"})
    return jsonify({"message": "Product not found"}), 404
