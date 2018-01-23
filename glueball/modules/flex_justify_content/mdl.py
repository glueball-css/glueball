"""
Defines the alignment along the main axis.
It distributes extra free space leftover when the flex items on a line are inflexible,
or have reached their maximum size.
"""
from defaults import *
from utils import CssModule, Style


mdl = CssModule(
    'Flex justify content',
    BREAKPOINTS,
    [FULL],
    dynamic={'.fxjc': ['justify_content']},
    values={'Distributions': [
        ('fxs', 'fxe', 'c', 'sb', 'sa', 'se'),
        ('flex-start', 'flex-end', 'center', 'space-between', 'space-around', 'space-evenly')]},
    docstring=__doc__
)
