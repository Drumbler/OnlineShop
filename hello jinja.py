from jinja2 import *
template = Template('hello {{ name }}')
print(template.render(name = u'World'))