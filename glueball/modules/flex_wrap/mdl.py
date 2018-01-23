"""
Defines whether the flex items are forced in a single line or can be flowed into multiple lines.
If set to multiple lines, it also defines the cross-axis which determines the direction new lines are stacked in.
"""
from defaults import *
from utils import CssModule, Style


mdl = CssModule(
    'Flex wrap',
    BREAKPOINTS,
    [FULL],
    dynamic={'.fxw': ['flex-wrap']},
    values={'Directions': [
        ('n', 'w', 'wr'),
        ('nowrap', 'wrap', 'wrap-reverse')]},
    docstring=__doc__
)
