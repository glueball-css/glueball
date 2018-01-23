"""
Modifiers
"""
from defaults import *
from utils import CssModule, Style


mdl = CssModule(
    'Overflow',
    BREAKPOINTS,
    [UP],
    dynamic={'.o': ['overflow'], 'ox': ['overflow-x'], 'oy': ['overflow-y']},
    values={'Values': [('v', 'h', 's', 'a'), ('visible', 'hidden', 'scroll', 'auto')]},
    docstring=__doc__
)
