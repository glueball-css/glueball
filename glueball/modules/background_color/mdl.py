"""
Full spectrum of hsla colors for background
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, SPECTRUM
from ...core import CssModule


mdl = CssModule(
    'Background color',
    [UP],
    dynamic={'.bgc': ['background-color']},
    values=[(c.get_selector(), str(c)) for c in SPECTRUM],
    pseudos={'hover': [UP]},
    docstring=__doc__,
)
