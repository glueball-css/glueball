"""
Defines the default behaviour for how flex items are laid out along the cross axis on the current line.
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = [
    ('fxs', 'flex-start'),
    ('fxe', 'flex-end'),
    ('c', 'center'),
    ('b', 'baseline'),
    ('s', 'stretch')
]

mdl = CssModule(
    'Flex align items',
    BREAKPOINTS,
    [FULL],
    dynamic={'.fxai': ['align-items']},
    values={'Alignment options': vals},
    docstring=__doc__
)
