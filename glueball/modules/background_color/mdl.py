"""
Full spectrum of hsla colors for background
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, SPECTRUM
from ...core import CssModule

vals = [(c.get_selector(), str(c)) for c in SPECTRUM]

mdl = CssModule(
    'Background color',
    [UP],
    dynamic={'.bgc': ['background-color']},
    values=vals,
    pseudos={'hover': ([UP], vals)},
    docstring=__doc__,
)
