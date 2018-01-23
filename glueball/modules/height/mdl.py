"""
Percentages and values for height
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, SIZING, PERCENTAGES
from ...core import CssModule


mdl = CssModule(
    'Height',
    BREAKPOINTS,
    [UP],
    dynamic={'.h': ['height']},
    values={'Modifiers': SIZING, 'Percentages': PERCENTAGES},
    docstring=__doc__
)
