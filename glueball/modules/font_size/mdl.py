"""
Progressively larger font sizes.
"""

from defaults import *
from utils import CssModule, Style


mdl = CssModule(
    'Font size',
    BREAKPOINTS,
    [UP],
    dynamic={'.fs': ['font-size']},
    values={'Type scales': TYPE_SCALE},
    pseudos={'hover': [UP], 'focus': [UP]},
    docstring=__doc__
)
