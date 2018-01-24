from flask import Flask, render_template, abort
from jinja2 import TemplateNotFound

from glueball.glueball import sheet

app = Flask(__name__)

MODULE_DIR = 'modules/'


@app.route('/')
def home():
    return render_template('home.html', sheet=sheet)


@app.route('/module/<slug>')
def mdl(slug):
    try:
        return render_template(MODULE_DIR+slug+'.html', mdl=sheet[slug])
    except TemplateNotFound:
        abort(404)

if __name__ == "__main__":
    app.run()
