from jinja2 import Environment, FileSystemLoader

from glueball.glueball import sheet


env = Environment(loader=FileSystemLoader(''))

template = env.get_template('templ.md')

if __name__ == "__main__":
    print(template.render(the='variables', go='here'))

