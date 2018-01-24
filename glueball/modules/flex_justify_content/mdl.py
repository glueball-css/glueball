"""
Defines the alignment along the main axis.
It distributes extra free space leftover when the flex items on a line are inflexible,
or have reached their maximum size.
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = [
    ('fxs', 'flex-start'),
    ('fxe', 'flex-end'),
    ('c', 'center'),
    ('sb', 'space-between'),
    ('sa', 'space-around'),
    ('se', 'space-evenly')
]

mdl = CssModule(
    'Flex justify content',
    [FULL],
    dynamic={'.fxjc': ['justify-content']},
    values={'Distributions': vals},
    docstring=__doc__
)
