from docs.html.app import app
# from docs.md.mdoc import rendered
from glueball.glueball import write_css
from glueball.glueball import sheet


def print_mods(s=sheet):
    """Print module info for use in other applications (spreadsheet)"""
    for m in s.modules:
        vals = []
        for q, w in m.values.items():
            for zz in w:
                vals.append(zz[0])
        for k, v in m.dynamic.items():
            print(k, v, vals)


def write_css_files():
    """Make a CSS file for every module in its folder"""
    for mdl in sheet.modules:
        mdl.write_css()


def write_md_files():
    """Make a readme.md file for every module in its folder"""
    for mdl in sheet.modules:
        mdl.write_md()


if __name__ == "__main__":
    write_css()  # General css file
    # app.run()
    # print_mods()
    # print(rendered)
    write_css_files()
    # write_md_files()

