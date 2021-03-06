"""
Percentages and values for max width
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, SIZING, PERCENTAGES
from ...core import CssModule


mdl = CssModule(
    'Max width',
    [UP],
    dynamic={'.maxw': ['max-width']},
    values=SIZING+PERCENTAGES,
    docstring=__doc__
)
