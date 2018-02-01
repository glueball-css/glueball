"""
Radius for every corner and individual corners
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, SPACING
from ...core import CssModule

vals = SPACING + [('100p', '100%')]

mdl = CssModule(
    'Border radius',
    [FULL],
    dynamic={
        '.br': ['border-radius'],
        '.btrr': ['border-top-right-radius'],
        '.bbrr': ['border-bottom-right-radius'],
        '.bblr': ['border-bottom-left-radius'],
        '.btlr': ['border-top-left-radius']},
    values=vals,
    docstring=__doc__
)
