from models.products import get_products
from views.template_loader import jinja_env


def render_products():
    products = get_products()
    template = jinja_env.get_template("/products.j2")
    output_text = template.render(products=products)

    return output_text
# переименовать products
