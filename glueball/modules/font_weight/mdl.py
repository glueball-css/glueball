"""
Only numbers, not bold or normal
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

mdl = CssModule(
    'Font weight',
    [UP],
    dynamic={'.fw': ['font-weight']},
    values={'Weights': zip(range(1, 10), range(100, 901, 100))},
    docstring=__doc__
)
