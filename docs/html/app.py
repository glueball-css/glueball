from flask import Flask, render_template, abort
from jinja2 import TemplateNotFound
import string

from glueball.glueball import sheet
from glueball.modules.defaults import TYPE_SCALE, WEIGHT, SPECTRUM

app = Flask(__name__)


MODULE_DIR = 'modules/'
FONT_MODULE = sheet['font-family']


def style_from_url(url, font_mdl=FONT_MODULE):
    for style in font_mdl.styles:
        for sel in style.selectors:
            if sel.base == url:
                return style
    return None


def hsla_from_url(url, spectrum=SPECTRUM):
    for hsla in spectrum:
        if hsla.get_selector() == url:
            return hsla


@app.route('/')
def home():
    return render_template('home.html', sheet=sheet)


@app.route('/docs/')
def docs():
    return render_template('modules.html', sheet=sheet)


@app.route('/docs/fonts/')
def fonts():
    return render_template('fonts.html', styles=FONT_MODULE.styles)


@app.route('/docs/fonts/<font_url>/')
def font(font_url):
    style = style_from_url(font_url)
    return render_template('font.html', style=style, sizes=TYPE_SCALE, weights=WEIGHT, string=string)


@app.route('/docs/colors/')
def colors():
    return render_template('colors.html', spectrum=SPECTRUM)


@app.route('/docs/color/<color_url>/')
def color(color_url):
    hsla = hsla_from_url(color_url)
    return render_template('color.html', hsla=hsla)


@app.route('/docs/modules/<mdlurl>/')
def mdl(mdlurl):
    try:
        return render_template(MODULE_DIR+mdlurl+'.html', mdl=sheet[mdlurl])
    except TemplateNotFound:
        abort(404)

if __name__ == "__main__":
    app.run()
