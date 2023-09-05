from flask import Flask, request

from views.products import render_products, render_main, render_product_page, render_categories

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_main()


@app.route('/products')
def products_page():
    return render_products(category=request.args.get('category'))


@app.route('/products/<int:product_id>')
def product(product_id: int):
    return render_product_page(product_id)


@app.route('/categories')
def categories():
    return render_categories()


if __name__ == '__main__':
    app.run(debug=True)
