"""
Percentages and values for maximum width
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, SIZING, PERCENTAGES
from ...core import CssModule


mdl = CssModule(
    'Max width',
    BREAKPOINTS,
    [FULL],
    dynamic={'.mw': ['max-width']},
    values={'Modifiers': SIZING, 'Percentages': PERCENTAGES},
    docstring=__doc__
)
