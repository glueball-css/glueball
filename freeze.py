from flask_frozen import Freezer
from docs.html.app import app

app.config['FREEZER_DESTINATION'] = '../../gh-pages'
app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*', 'CNAME', '.gitignore', 'readme.md']
app.config['FREEZER_RELATIVE_URLS'] = False

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
