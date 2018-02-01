"""
Defines the default behaviour for how flex items are laid out along the cross axis on the current line.
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
    'Align items',
    [FULL],
    dynamic={'.ai': ['align-items']},
    values=vals,
    docstring=__doc__
)
