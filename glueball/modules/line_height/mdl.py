"""
Modifiers
"""
from defaults import *
from utils import CssModule, Style

vals = (
    ['-2', '-1', 'n', '1', '2', '3', '4'],
    ['0.75', '0.875', 'normal', '1', '1.125', '1.25', '1.5', '2']
)

mdl = CssModule(
    'Line height',
    BREAKPOINTS,
    [FULL],
    dynamic={'.lh': ['line-height']},
    values={'Heights': vals},
    docstring=__doc__
)
