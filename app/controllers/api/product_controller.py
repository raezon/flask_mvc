# app/controllers/product_controller.py
from flask import Blueprint, request, jsonify
from app.services.product_service import (
    create_new_product,
    fetch_product_by_id,
    fetch_all_products,
    modify_product,
    remove_product,
)

product_blueprint = Blueprint("product", __name__)


@product_blueprint.route("/products", methods=["GET"])
def get_products():
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


@product_blueprint.route("/product/<int:id>", methods=["GET"])
def get_product(id):
    product = fetch_product_by_id(id)
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


@product_blueprint.route("/product", methods=["POST"])
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


@product_blueprint.route("/product/<int:id>", methods=["PUT"])
def update_product(id):
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")

    product = modify_product(id, name, description, price)
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


@product_blueprint.route("/product/<int:id>", methods=["DELETE"])
def delete_product(id):
    product = remove_product(id)
    if product:
        return jsonify({"message": "Product deleted"})
    return jsonify({"message": "Product not found"}), 404
