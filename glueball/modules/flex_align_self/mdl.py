"""
Overrides the align-items value for specific flex items.
"""
from defaults import *
from utils import CssModule, Style


mdl = CssModule(
    'Flex align self',
    BREAKPOINTS,
    [FULL],
    dynamic={'.fxas': ['align-self']},
    values={'Alignment options': [
        ('fxs', 'fxe', 'c', 'b', 's'),
        ('flex-start', 'flex-end', 'center', 'baseline', 'stretch')]},
    docstring=__doc__
)
