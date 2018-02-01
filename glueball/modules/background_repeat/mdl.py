"""
Options for repeating background images
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = (
    ('n',   'no-repeat'),
    ('x',   'repeat-x'),
    ('y',   'repeat-y'),
)

mdl = CssModule(
    'Background repeat',
    [FULL],
    dynamic={'.bgr': ['background-repeat']},
    values=vals,
    docstring=__doc__
)
