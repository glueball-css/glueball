"""
Percentages and values for height
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, SIZING, PERCENTAGES
from ...core import CssModule


mdl = CssModule(
    'Height',
    [UP],
    dynamic={'.h': ['height']},
    values=SIZING+PERCENTAGES,
    docstring=__doc__
)
