# app/crud/product_crud.py
from app import db
from app.models import Product


def create_product(name, description, price):
    new_product = Product(name=name, description=description, price=price)
    db.session.add(new_product)
    db.session.commit()
    return new_product


def get_product_by_id(product_id):
    return Product.query.get(product_id)


def get_all_products():
    return Product.query.all()


def update_product(product_id, name, description, price):
    product = Product.query.get(product_id)
    if product:
        product.name = name
        product.description = description
        product.price = price
        db.session.commit()
    return product


def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
    return product
