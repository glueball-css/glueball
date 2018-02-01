"""
Line height settings
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = [
    (-2,    '0.75'),
    (-1,    '0.875'),
    (1,     '1'),
    (2,     '1.125'),
    (3,     '1.25'),
    (4,     '1.5'),
    ('n',   'normal'),
]

mdl = CssModule(
    'Line height',
    [FULL],
    dynamic={'.lh': ['line-height']},
    values=vals,
    docstring=__doc__
)
