"""
Full spectrum of hsla colors for font
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, SPECTRUM
from ...core import CssModule


mdl = CssModule(
    'Color',
    [FULL],
    dynamic={'.': ['color']},
    values=[(c.get_selector(), str(c)) for c in SPECTRUM],
    docstring=__doc__
)
