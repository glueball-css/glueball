"""
Percentages and values for maximum width
"""
from defaults import *
from utils import CssModule, Style


mdl = CssModule(
    'Max width',
    BREAKPOINTS,
    [FULL],
    dynamic={'.mw': ['max-width']},
    values={'Modifiers': SIZING, 'Percentages': PERCENTAGES},
    docstring=__doc__
)
