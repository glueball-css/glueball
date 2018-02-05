"""
Percentages and values for minimum width
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, SIZING, PERCENTAGES
from ...core import CssModule


mdl = CssModule(
    'Min width',
    [UP],
    dynamic={'.minw': ['min-width']},
    values=SIZING+PERCENTAGES,
    docstring=__doc__
)
