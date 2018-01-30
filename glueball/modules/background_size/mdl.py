"""
Contain or cover
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = (
    'contain',
    'cover',
)

mdl = CssModule(
    'Background size',
    [UP],
    dynamic={'.': ['background-size']},
    values={'Sizings': list(zip(vals, vals))},
    docstring=__doc__
)
