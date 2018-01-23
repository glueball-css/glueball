"""
Sets the background position of images.
A static declaration of "no-repeat" is implicitly included.
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

values = {
    'Positions': [
        ('lt', 'lc', 'lb', 'rt', 'rc', 'rb', 'ct', 'cc', 'cb'),
        ('left top', 'left center', 'left bottom', 'right top', 'right center', 'right bottom', 'center top',
         'center center', 'center bottom')
    ]
}

mdl = CssModule(
    'Background position',
    BREAKPOINTS,
    [UP],
    styles=[
        ('.test', {'width': '2rem', 'margin': '0'}),
        ('div.test', {'color': 'red'}),
    ],
    static={'background-repeat': 'no-repeat'},
    dynamic={'.bgp': ['background-position']},
    values=values,
    docstring=__doc__
)
