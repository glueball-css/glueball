"""
Various speeds for all transitions
"""
from defaults import *
from utils import CssModule, Style

vals = [[str(i) for i in range(1, 10)], (
    'all 0.1s cubic-bezier(.25, .8, .25, 1)',
    'all 0.2s cubic-bezier(.25, .8, .25, 1)',
    'all 0.3s cubic-bezier(.25, .8, .25, 1)',
    'all 0.4s cubic-bezier(.25, .8, .25, 1)',
    'all 0.5s cubic-bezier(.25, .8, .25, 1)',
    'all 0.7s cubic-bezier(.25, .8, .25, 1)',
    'all 1.0s cubic-bezier(.25, .8, .25, 1)',
    'all 2.0s cubic-bezier(.25, .8, .25, 1)',
    'all 4.0s cubic-bezier(.25, .8, .25, 1)',)]

mdl = CssModule(
    'Transition',
    BREAKPOINTS,
    [FULL],
    dynamic={'.t': ['transition']},
    values={'speeds': vals},
    docstring=__doc__
)
