# app/controllers/product_controller.py
from flask import Blueprint, request, render_template, redirect, url_for, flash
from app import db
from app.models import Product
product_blueprint = Blueprint("product", __name__)

# Render products list using Jinja
@product_blueprint.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()  # Récupère tous les produits
    return render_template("product/index.html", products=products)


# Render a single product view using Jinja
@product_blueprint.route("/product/<int:id>", methods=["GET"])
def get_product(id):
    product = Product.query.get(id)  # Recherche un produit par son ID
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

        # Création et ajout du produit à la base de données
        try:
            new_product = Product(name=name, description=description, price=float(price))
            db.session.add(new_product)
            db.session.commit()
            flash("Product created successfully", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error creating product: {e}", "error")
        return redirect(url_for("product.get_products"))

    return render_template("/product/create.html")


# Render form to update an existing product
@product_blueprint.route("/product/edit/<int:id>", methods=["GET", "POST"])
def update_product(id):
    product = Product.query.get(id)  # Recherche le produit par ID
    if not product:
        flash("Product not found", "error")
        return redirect(url_for("product.get_products"))

    if request.method == "POST":
        # Mise à jour des champs du produit
        try:
            product.name = request.form.get("name")
            product.description = request.form.get("description")
            product.price = float(request.form.get("price"))

            db.session.commit()
            flash("Product updated successfully", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error updating product: {e}", "error")
        return redirect(url_for("product.get_products"))

    return render_template("/product/edit.html", product=product)


# Delete product and return to products list
@product_blueprint.route("/product/delete/<int:id>", methods=["POST"])
def delete_product(id):
    product = Product.query.get(id)  # Recherche le produit par ID
    if product:
        try:
            db.session.delete(product)
            db.session.commit()
            flash("Product deleted successfully", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error deleting product: {e}", "error")
    else:
        flash("Product not found", "error")
    return redirect(url_for("product.get_products"))
