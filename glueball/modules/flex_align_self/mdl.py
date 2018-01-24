"""
Overrides the align-items value for specific flex items.
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
    'Flex align self',
    [FULL],
    dynamic={'.fxas': ['align-self']},
    values={'Alignment options': vals},
    docstring=__doc__
)
