"""
Progressively larger font sizes.
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, TYPE_SCALE
from ...core import CssModule


mdl = CssModule(
    'Font size',
    BREAKPOINTS,
    [UP],
    dynamic={'.fs': ['font-size']},
    values={'Type scales': TYPE_SCALE},
    pseudos={'hover': [UP], 'focus': [UP]},
    docstring=__doc__
)
