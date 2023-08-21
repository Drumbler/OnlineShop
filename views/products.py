from flask import render_template
from models.products import get_products, get_product


def render_products():
    products = get_products()
    return render_template('products.html', products=products)


def render_main():
    return render_template('main.html')


def render_product_page(product_id):
    product = get_product(product_id)
    return render_template('product_page.html', product=product)
