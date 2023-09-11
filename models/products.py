from models.database import db


def get_products():
    return db.query('SELECT * FROM products')


def get_products_category(category, sort):
    if sort not in ('ASC', 'DESC'):
        raise Exception('sort value is not allowed')
    return db.query(f'''
        SELECT * FROM products p 
        JOIN categories c ON p.fk_category_id = c.category_id
        WHERE (%(category)s is null or fk_category_id = %(category)s)
        ORDER BY price {sort}
    ''', category=category)


def get_product(product_id):
    return db.query_single('SELECT * FROM products WHERE product_id=%(product_id)s',
                           product_id=product_id)


def get_categories():
    return db.query('SELECT * FROM categories')


