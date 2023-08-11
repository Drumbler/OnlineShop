from jinja2 import Template, Environment, FileSystemLoader
from DataBase import db


def render_goods():
    products = db.get_goods()
    templateLoader = FileSystemLoader(searchpath="./")
    templateEnv = Environment(loader=templateLoader)
    template = templateEnv.get_template("template_table.j2")
    outputText = template.render(products=products)  # this is where to put args to the template renderer

    return outputText
