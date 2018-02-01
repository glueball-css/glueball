"""
Various padding properties:

* padding top, right, bottom and left
* padding (shorthand for all margins)
* padding horizontal and vertical (x & y)
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, SPACING
from ...core import CssModule


mdl = CssModule(
    'Padding',
    [UP],
    dynamic={
        '.p': ['padding'],
        '.pt': ['padding-top'],
        '.pr': ['padding-right'],
        '.pb': ['padding-bottom'],
        '.pl': ['padding-left'],
        '.px': ['padding-left', 'padding-right'],
        '.py': ['padding-top', 'padding-bottom']},
    values=SPACING,
    docstring=__doc__
)
