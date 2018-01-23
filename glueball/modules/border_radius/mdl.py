"""
Radius for every corner and individual corners
"""
from defaults import *
from utils import CssModule, Style

vals = (SPACING[0]+['100p'], SPACING[1]+['100%'])

mdl = CssModule(
    'Border radius',
    BREAKPOINTS,
    [FULL],
    dynamic={
        '.br': ['border-radius'],
        '.btrr': ['border-top-right-radius'],
        '.bbrr': ['border-bottom-right-radius'],
        '.bblr': ['border-bottom-left-radius'],
        '.btlr': ['border-top-left-radius']},
    values={'Radii': vals},
    docstring=__doc__
)
