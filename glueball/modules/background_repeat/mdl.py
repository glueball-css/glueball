"""
Options for repeating background images
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

values = (
    ('n',   'no-repeat'),
    ('x',   'repeat-x'),
    ('y',   'repeat-y'),
)

mdl = CssModule(
    'Background repeat',
    [FULL],
    dynamic={'.bgr': ['background-repeat']},
    values={'Values': values},
    docstring=__doc__
)
