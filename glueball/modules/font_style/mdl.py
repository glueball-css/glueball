"""
Normal or italic
"""

from defaults import *
from utils import CssModule, Style


mdl = CssModule(
    'Font style',
    BREAKPOINTS,
    [UP],
    dynamic={'.fs': ['font-style']},
    values={'Styles': [('n', 'i'), ('normal', 'italic')]},
    docstring=__doc__
)
