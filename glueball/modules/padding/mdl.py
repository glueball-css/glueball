"""
Various padding properties:

* padding top, right, bottom and left
* padding (shorthand for all margins)
* padding horizontal and vertical (x & y)
"""
from defaults import *
from utils import CssModule, Style


mdl = CssModule(
    'Padding',
    BREAKPOINTS,
    [UP],
    dynamic={
        '.p': ['padding'],
        '.pt': ['padding-top'],
        '.pr': ['padding-right'],
        '.pb': ['padding-bottom'],
        '.pl': ['padding-left'],
        '.px': ['padding-left', 'padding-right'],
        '.py': ['padding-top', 'padding-bottom']},
    values={'Spacing': SPACING,},
    docstring=__doc__
)
