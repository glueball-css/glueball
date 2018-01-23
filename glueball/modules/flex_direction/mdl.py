"""
Establishes the main-axis, thus defining the direction flex items are placed
inside the flex container.
"""
from defaults import *
from utils import CssModule, Style


mdl = CssModule(
    'Flex direction',
    BREAKPOINTS,
    [FULL],
    dynamic={'.fxd': ['flex-direction']},
    values={'Directions': [
        ('row', 'col', 'rowr', 'colr'),
        ('row', 'row-reverse', 'column', 'column-reverse')]},
    docstring=__doc__
)
