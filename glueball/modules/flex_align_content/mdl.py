"""
Align a flex container's lines within it, when there is extra space in the cross-axis.
"""
from defaults import *
from utils import CssModule, Style


mdl = CssModule(
    'Flex align content',
    BREAKPOINTS,
    [FULL],
    dynamic={'.fxac': ['align-content']},
    values={'Alignment options': [
        ('fxs', 'fxe', 'c', 'sb', 'sa', 's'),
        ('flex-start', 'flex-end', 'center', 'space-between', 'space-around', 'stretch')]},
    docstring=__doc__
)
