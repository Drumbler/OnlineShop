from jinja2 import Environment, FileSystemLoader
from models.products import get_products


def render_products():
    products = get_products()
    templateLoader = FileSystemLoader(searchpath="./")
    templateEnv = Environment(loader=templateLoader)
    template = templateEnv.get_template("views/templates/products.j2")
    outputText = template.render(products=products)  # this is where to put args to the template renderer

    return outputText
# переименовать products
