from flask import Flask
from jinja2 import Template
from productTemplate import render_goods

app = Flask(__name__)

@app.route('/')
def hello():
    return render_goods()


if __name__ == '__main__':
    app.run()
