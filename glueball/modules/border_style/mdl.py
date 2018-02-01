"""
Style for all borders and individual borders
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = [
    ('n',       'none'),
    ('dash',    'dashed'),
    ('dot',     'dotted'),
    ('s',   '   solid'),
]

mdl = CssModule(
    'Border style',
    [UP],
    dynamic={
        '.bs': ['border-style'],
        '.bts': ['border-top-style'],
        '.brs': ['border-right-style'],
        '.bbs': ['border-bottom-style'],
        '.bls': ['border-left-style']},
    values=vals,
    docstring=__doc__
)
