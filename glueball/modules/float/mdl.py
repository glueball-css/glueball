"""
Float left, right or none
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = [
    ('l', 'left'),
    ('r', 'right'),
    ('n', 'none')
]


mdl = CssModule(
    'Float',
    [UP],
    dynamic={'.float': ['float']},
    values=vals,
    docstring=__doc__
)
