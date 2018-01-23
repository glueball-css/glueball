"""
Percentages and values for height
"""
from defaults import *
from utils import CssModule, Style


mdl = CssModule(
    'Height',
    BREAKPOINTS,
    [UP],
    dynamic={'.h': ['height']},
    values={'Modifiers': SIZING, 'Percentages': PERCENTAGES},
    docstring=__doc__
)
