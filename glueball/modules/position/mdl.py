"""
Options
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = (
    'static',
    'relative',
    'absolute',
    'fixed'
)

mdl = CssModule(
    'Position',
    [UP],
    dynamic={'.': ['position']},
    values=list(zip(vals, vals)),
    docstring=__doc__
)
