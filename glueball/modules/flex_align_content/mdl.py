"""
Align a flex container's lines within it, when there is extra space in the cross-axis.
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = [
    ('fxs', 'flex-start'),
    ('fxe', 'flex-end'),
    ('c', 'center'),
    ('sb', 'space-between'),
    ('sa', 'space-around'),
    ('s', 'stretch'),
]

mdl = CssModule(
    'Flex align content',
    BREAKPOINTS,
    [FULL],
    dynamic={'.fxac': ['align-content']},
    values={'Alignment options': vals},
    docstring=__doc__
)
