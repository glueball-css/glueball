"""
Full spectrum of hsla colors for background
"""

from defaults import *
from utils import CssModule, Style


mdl = CssModule(
    'Background color',
    BREAKPOINTS,
    [FULL],
    dynamic={'.bgc': ['background-color']},
    values={'Colors': (
        [c.suffix for c in SPECTRUM],
        [str(c) for c in SPECTRUM])},
    docstring=__doc__
)
