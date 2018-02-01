"""
Full spectrum of hsla colors for border
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, SPECTRUM
from ...core import CssModule


mdl = CssModule(
    'Border color',
    [FULL],
    dynamic={'.bc': ['border-color']},
    values=[(c.get_selector(), str(c)) for c in SPECTRUM],
    docstring=__doc__
)
