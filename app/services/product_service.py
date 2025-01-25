# app/services/product_service.py
from app.models import Product
from app.repositories.product_repository import (
    create_product,
    get_product_by_id,
    get_all_products,
    update_product,
    delete_product,
)


def create_new_product(name, description, price):
    return create_product(name, description, price)


def fetch_product_by_id(product_id):
    return get_product_by_id(product_id)


def fetch_all_products():
    return get_all_products()


def modify_product(product_id, name, description, price):
    return update_product(product_id, name, description, price)


def remove_product(product_id):
    return delete_product(product_id)
