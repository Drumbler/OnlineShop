import datetime

from flask import Flask, request, session

from views.products import render_products, render_main, render_product_page, render_categories

app = Flask(__name__)
app.config['SECRET_KEY'] = '6226f559396c27af3ef85e1c112d08ebed5d8429'
app.permanent_session_lifetime = datetime.timedelta(days=30)


@app.route('/products/<int:product_id>/setsession')
def setsession(product_id):
    res = str(session.items())
    if 'cart_item' not in session:
        session['cart_item'] = {}
        session.modified = True
    if product_id in session['cart_item']:
        session['cart_item'][product_id] += 1
        session.modified = True
    print(session)
    return res
 

# @app.route('/getproduct')
# def get_product(product_id: int):


@app.route('/')
def main_page():
    return render_main()


@app.route('/products')
def products():
    return render_products(
        category=request.args.get('category', type=int),
        sort=request.args.get('sort', default='ASC', type=str)
    )


@app.route('/products/<int:product_id>')
def product(product_id: int):
    return render_product_page(product_id)


@app.route('/categories')
def categories():
    return render_categories()


# @app.route('/cart')
# def cart():
#     items = str(session.items())
#     if 'cart_item' in session:


if __name__ == '__main__':
    app.run(debug=True)

