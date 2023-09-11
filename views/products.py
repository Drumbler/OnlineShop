from flask import render_template

from models.exceptions import RecordNotFound
from models.products import get_product, get_categories, get_products_category


def render_products(category, sort):
    sort = {
        'ASC': 'ASC',
        'DESC': 'DESC'
    }.get(sort.upper(), 'ASC')
    products = get_products_category(category, sort)
    return render_template('products.html',
                           products=products, category=category, sort=sort)


def render_main():
    return render_template('main.html')


def render_product_page(product_id):
    try:
        product = get_product(product_id)
    except RecordNotFound:
        return "Product not found", 404
    return render_template('product_page.html',
                           product=product)


def render_categories():
    categories = get_categories()
    return render_template('categories.html',
                           categories=categories)




