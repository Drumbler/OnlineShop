from flask import Flask, send_from_directory, send_file
from views.products import render_products

app = Flask(__name__)


@app.route('/products')
def products_page():
    return render_products()

if __name__ == '__main__':
    app.run(debug=True)
