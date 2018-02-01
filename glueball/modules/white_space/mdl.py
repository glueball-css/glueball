"""
White space is used to control how whitespace is rendered.
"""
from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = [
    ('n',       'normal'),
    ('nw',      'nowrap'),
    ('p',       'pre'),
]


mdl = CssModule(
    'White space',
    [UP],
    dynamic={'.ws': ['white-space']},
    values=vals,
    docstring=__doc__
)
