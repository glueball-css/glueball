"""
Sets the background position of images.
A static declaration of "no-repeat" is implicitly included.
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

values = (
    ('lt',  'left top'),
    ('lc',  'left center'),
    ('lb',  'left bottom'),
    ('rt',  'right top'),
    ('rc',  'right center'),
    ('rb',  'right bottom'),
    ('ct',  'center top'),
    ('cc',  'center center'),
    ('cb',  'center bottom'),
)

mdl = CssModule(
    'Background position',
    [UP],
    static={'background-repeat': 'no-repeat'},
    dynamic={'.bgp': ['background-position']},
    values={'Positions': values},
    docstring=__doc__
)
