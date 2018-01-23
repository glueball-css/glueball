"""
Full spectrum of hsla colors for border
"""

from defaults import *
from utils import CssModule, Style


mdl = CssModule(
    'Border color',
    BREAKPOINTS,
    [FULL],
    dynamic={'.bc': ['border-color']},
    values={'Border colors': (
        [c.suffix for c in SPECTRUM]+['t'],
        [str(c) for c in SPECTRUM]+['transparent'])},
    docstring=__doc__
)
