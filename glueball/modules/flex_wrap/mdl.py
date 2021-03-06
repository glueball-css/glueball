"""
Defines whether the flex items are forced in a single line or can be flowed into multiple lines.
If set to multiple lines, it also defines the cross-axis which determines the direction new lines are stacked in.
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = [
    ('n', 'nowrap'),
    ('w', 'wrap'),
    ('wr', 'wrap-reverse')
]

mdl = CssModule(
    'Flex wrap',
    [FULL],
    dynamic={'.fw': ['flex-wrap']},
    values=vals,
    docstring=__doc__
)
