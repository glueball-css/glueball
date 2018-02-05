"""
Overrides the align-items value for specific flex items.
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = [
    ('fs', 'flex-start'),
    ('fe', 'flex-end'),
    ('c', 'center'),
    ('b', 'baseline'),
    ('s', 'stretch')
]

mdl = CssModule(
    'Align self',
    [FULL],
    dynamic={'.as': ['align-self']},
    values=vals,
    docstring=__doc__
)
