"""
Full spectrum of hsla colors for background
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, SPECTRUM, GRAYS
from ...core import CssModule

spectrum_vals = [(c.get_selector(), str(c)) for c in SPECTRUM]
gray_vals = [(c.get_selector(), str(c)) for c in GRAYS]

mdl = CssModule(
    'Background color',
    [UP],
    dynamic={'.bgc': ['background-color']},
    values=spectrum_vals,
    pseudos={
        'hvr': ([UP], spectrum_vals),
        'odd': ([FULL], gray_vals),
        'evn': ([FULL], gray_vals),
    },
    docstring=__doc__,
)
