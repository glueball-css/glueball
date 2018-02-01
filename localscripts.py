from docs.html.app import app
from docs.md.mdoc import rendered
from glueball.glueball import write_css
from glueball.glueball import sheet


def print_mods(s=sheet):
    for m in s.modules:
        vals = []
        for q, w in m.values.items():
            for zz in w:
                vals.append(zz[0])
        for k, v in m.dynamic.items():
            print(k, v, vals)


def write_css_files():
    for mdl in sheet.modules:
        mdl.write_css()

if __name__ == "__main__":
    # write_css()
    # app.run()
    # print_mods()
    # print(rendered)
    write_css_files()


