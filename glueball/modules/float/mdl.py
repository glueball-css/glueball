"""
Positioning
"""

from defaults import *
from utils import CssModule, Style


mdl = CssModule(
    'Float',
    BREAKPOINTS,
    [UP],
    dynamic={'.f': ['float']},
    values={'Values': [('l', 'r', 'n'), ('left', 'right', 'none')]},
    docstring=__doc__
)
