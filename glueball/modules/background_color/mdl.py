"""
Full spectrum of hsla colors for background
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, SPECTRUM
from ...core import CssModule


mdl = CssModule(
    'Background color',
    [FULL],
    dynamic={'.bgc': ['background-color']},
    values={'Colors': [(c.get_selector(), str(c)) for c in SPECTRUM]},
    docstring=__doc__
)
