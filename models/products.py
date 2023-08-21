from models.database import db


def get_products():
    return db.query('SELECT * FROM products')


def get_product(product_id):
    return db.query(f'SELECT * FROM products WHERE product_id={product_id}')[0]
