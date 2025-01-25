# app/controllers/product_controller.py
from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.services.product_service import (
    create_new_product,
    fetch_product_by_id,
    fetch_all_products,
    modify_product,
    remove_product,
)

product_blueprint = Blueprint("product", __name__)


# Render products list using Jinja
@product_blueprint.route("/products", methods=["GET"])
def get_products():
    products = fetch_all_products()
    return render_template("product/index.html", products=products)


# Render a single product view using Jinja
@product_blueprint.route("/product/<int:id>", methods=["GET"])
def get_product(id):
    product = fetch_product_by_id(id)
    if product:
        return render_template("view.html", product=product)
    flash("Product not found", "error")
    return redirect(url_for("product.get_products"))


# Render form to create a new product
@product_blueprint.route("/product/create", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        price = request.form.get("price")

        product = create_new_product(name, description, price)
        flash("Product created successfully", "success")
        return redirect(url_for("product.get_products"))

    return render_template("/product/create.html")


# Render form to update an existing product
@product_blueprint.route("/product/edit/<int:id>", methods=["GET", "POST"])
def update_product(id):
    product = fetch_product_by_id(id)
    if not product:
        flash("Product not found", "error")
        return redirect(url_for("product.get_products"))

    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        price = request.form.get("price")

        product = modify_product(id, name, description, price)
        flash("Product updated successfully", "success")
        return redirect(url_for("product.get_products"))

    return render_template("/product/edit.html", product=product)


# Delete product and return to products list
@product_blueprint.route("/product/delete/<int:id>", methods=["POST"])
def delete_product(id):
    product = remove_product(id)
    if product:
        flash("Product deleted successfully", "success")
    else:
        flash("Product not found", "error")
    return redirect(url_for("product.get_products"))
