"""
Percentages and values for minimum height
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, SIZING, PERCENTAGES
from ...core import CssModule


mdl = CssModule(
    'Min height',
    [UP],
    dynamic={'.minh': ['min-height']},
    values=SIZING+PERCENTAGES,
    docstring=__doc__
)
