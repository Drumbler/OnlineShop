from models.database import db


def get_products():
    return db.query('SELECT * FROM products')
