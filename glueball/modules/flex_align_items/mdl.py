"""
Defines the default behaviour for how flex items are laid out along the cross axis on the current line.
"""
from defaults import *
from utils import CssModule, Style


mdl = CssModule(
    'Flex align items',
    BREAKPOINTS,
    [FULL],
    dynamic={'.fxai': ['align-items']},
    values={'Alignment options': [
        ('fxs', 'fxe', 'c', 'b', 's'),
        ('flex-start', 'flex-end', 'center', 'baseline', 'stretch')]},
    docstring=__doc__
)
