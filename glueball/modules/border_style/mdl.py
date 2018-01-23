"""
Style for all borders and individual borders
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

values = [
    ('n',       'none'),
    ('dashed',  'dashed'),
    ('dotted',  'dotted'),
    ('solid',   'solid'),
]

mdl = CssModule(
    'Border style',
    BREAKPOINTS,
    [UP],
    dynamic={
        '.bs': ['border-style'],
        '.bts': ['border-top-style'],
        '.brs': ['border-right-style'],
        '.bbs': ['border-bottom-style'],
        '.bls': ['border-left-style']},
    values={'Styles': values},
    docstring=__doc__
)
