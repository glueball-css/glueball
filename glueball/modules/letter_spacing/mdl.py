"""
Modifiers, also negative
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = [
    (-2,    '-0.125em'),
    (-1,    '-0.0625em'),
    (0,     '0'),
    (1,     '0.0625em'),
    (2,     '0.125em'),
    (3,     '0.25em'),
    (4,     '0.5em'),
    ('n',   'normal'),
]

mdl = CssModule(
    'Letter spacing',
    [FULL],
    dynamic={'.ls': ['letter-spacing']},
    values={'Spacings': vals},
    docstring=__doc__
)
