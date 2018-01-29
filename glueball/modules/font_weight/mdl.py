"""
Only numbers, not bold or normal
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, WEIGHT
from ...core import CssModule

mdl = CssModule(
    'Font weight',
    [UP],
    dynamic={'.weight': ['font-weight']},
    values={'Weights': WEIGHT},
    docstring=__doc__
)
