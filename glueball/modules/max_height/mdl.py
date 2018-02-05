"""
Percentages and values for maximum height
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, SIZING, PERCENTAGES
from ...core import CssModule


mdl = CssModule(
    'Max height',
    [UP],
    dynamic={'.maxh': ['max-height']},
    values=SIZING+PERCENTAGES,
    docstring=__doc__
)
