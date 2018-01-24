"""
Options
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = [
    ('s', 'static'),
    ('r', 'relative'),
    ('a', 'absolute'),
    ('f', 'fixed')
]


mdl = CssModule(
    'Position',
    # BREAKPOINTS,
    media=[UP],
    dynamic={'.p': ['position']},
    values={'Values': vals},
    docstring=__doc__
)
