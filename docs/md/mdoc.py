from jinja2 import Environment, FileSystemLoader

from glueball.glueball import sheet

mdl = sheet.modules[1]

env = Environment(loader=FileSystemLoader(''))

template = env.get_template('docs/md/templ.md')

rendered = template.render(mdl=mdl)

if __name__ == "__main__":
    print(rendered)
