"""
Various speeds for all transitions
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = [
    (1, 'all 0.1s cubic-bezier(.25, .8, .25, 1)'),
    (2, 'all 0.2s cubic-bezier(.25, .8, .25, 1)'),
    (3, 'all 0.3s cubic-bezier(.25, .8, .25, 1)'),
    (4, 'all 0.4s cubic-bezier(.25, .8, .25, 1)'),
    (5, 'all 0.5s cubic-bezier(.25, .8, .25, 1)'),
    (6, 'all 0.7s cubic-bezier(.25, .8, .25, 1)'),
    (7, 'all 1.0s cubic-bezier(.25, .8, .25, 1)'),
    (8, 'all 2.0s cubic-bezier(.25, .8, .25, 1)'),
    (9, 'all 4.0s cubic-bezier(.25, .8, .25, 1)'),
]

mdl = CssModule(
    'Transition',
    [FULL],
    dynamic={'.t': ['transition']},
    values={'Speeds': vals},
    docstring=__doc__
)
