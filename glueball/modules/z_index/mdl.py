"""
Place
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = list(range(10)) + [99, 999, 9999, 99999]

mdl = CssModule(
    'Z index',
    [UP],
    dynamic={'.z': ['z-index']},
    values=list(zip(vals, vals)),
    docstring=__doc__
)
