"""
Control text case.
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = [
    ('n', 'none'),
    ('c', 'capitalize'),
    ('u', 'uppercase'),
    ('l', 'lowercase'),
]

mdl = CssModule(
    'Text transform',
    [FULL],
    dynamic={'.tt': ['text-transform']},
    values=vals,
    docstring=__doc__
)
