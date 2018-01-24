"""
Establishes the main-axis, thus defining the direction flex items are placed
inside the flex container.
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = [
    ('row', 'row'),
    ('col', 'row-reverse'),
    ('rowr', 'column'),
    ('colr', 'column-reverse')
]

mdl = CssModule(
    'Flex direction',
    [FULL],
    dynamic={'.fd': ['flex-direction']},
    values={'Directions': vals},
    docstring=__doc__
)
