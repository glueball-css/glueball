"""
Align a flex container's lines within it, when there is extra space in the cross-axis.
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = [
    ('fs', 'flex-start'),
    ('fe', 'flex-end'),
    ('c', 'center'),
    ('sb', 'space-between'),
    ('sa', 'space-around'),
    ('s', 'stretch'),
]

mdl = CssModule(
    'Align content',
    [FULL],
    dynamic={'.ac': ['align-content']},
    values={'Alignment options': vals},
    docstring=__doc__
)
