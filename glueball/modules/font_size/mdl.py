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
    pseudos={
        'hover': ([UP], TYPE_SCALE),
        'focus': ([UP], TYPE_SCALE),
    },
    docstring=__doc__
)
