"""
Various margin properties:

* margin top, right, bottom and left
* margin (shorthand for all margins)
* margin horizontal and vertical (x & y)
"""
from defaults import *
from utils import CssModule, Style


mdl = CssModule(
    'Margin',
    BREAKPOINTS,
    [UP],
    dynamic={
        '.m': ['margin'],
        '.mt': ['margin-top'],
        '.mr': ['margin-right'],
        '.mb': ['margin-bottom'],
        '.ml': ['margin-left'],
        '.mx': ['margin-left', 'margin-right'],
        '.my': ['margin-top', 'margin-bottom']},
    values={
        'Spacing': SPACING,
        'Negative': NEGATIVE_SPACING},
    docstring=__doc__
)
