"""
Various margin properties:

* margin top, right, bottom and left
* margin (shorthand for all margins)
* margin horizontal and vertical (x & y)
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, SPACING, NEGATIVE_SPACING
from ...core import CssModule

vals = SPACING + NEGATIVE_SPACING + [('a', 'auto')]

mdl = CssModule(
    'Margin',
    [UP],
    dynamic={
        '.m': ['margin'],
        '.mt': ['margin-top'],
        '.mr': ['margin-right'],
        '.mb': ['margin-bottom'],
        '.ml': ['margin-left'],
        '.mx': ['margin-left', 'margin-right'],
        '.my': ['margin-top', 'margin-bottom']},
    values=vals,
    docstring=__doc__
)
