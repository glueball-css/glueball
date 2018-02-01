"""
Horizontal alignment of inline and inline-blocks inside a block-element.
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = [
    ('l', 'left'),
    ('r', 'right'),
    ('c', 'center'),
    ('j', 'justify'),
]

mdl = CssModule(
    'Text align',
    [FULL],
    dynamic={'.ta': ['text-align']},
    values=vals,
    docstring=__doc__
)
