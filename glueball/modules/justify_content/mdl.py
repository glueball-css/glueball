"""
Defines the alignment along the main axis.
It distributes extra free space leftover when the flex items on a line are inflexible,
or have reached their maximum size.
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = [
    ('fs', 'flex-start'),
    ('fe', 'flex-end'),
    ('c', 'center'),
    ('sb', 'space-between'),
    ('sa', 'space-around'),
    ('se', 'space-evenly')
]

mdl = CssModule(
    'Justify content',
    [FULL],
    dynamic={'.jc': ['justify-content']},
    values={'Distributions': vals},
    docstring=__doc__
)
