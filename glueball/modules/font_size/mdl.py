"""
Progressively larger font sizes.
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, TYPE_SCALE
from ...core import CssModule


mdl = CssModule(
    'Font size',
    [UP],
    dynamic={'.size': ['font-size']},
    values=TYPE_SCALE,
    pseudos={'hover': [UP], 'focus': [UP]},
    docstring=__doc__
)
