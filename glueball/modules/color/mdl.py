"""
Full spectrum of hsla colors for font
"""
try:
    from defaults import *
except:

from utils import CssModule, Style


mdl = CssModule(
    'Color',
    BREAKPOINTS,
    [FULL],
    dynamic={'c.': ['color']},
    values={'Colors': (
        [c.suffix for c in SPECTRUM],
        [str(c) for c in SPECTRUM])},
    docstring=__doc__
)
