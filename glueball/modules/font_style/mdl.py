"""
Normal or italic
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

mdl = CssModule(
    'Font style',
    BREAKPOINTS,
    [UP],
    dynamic={'.fs': ['font-style']},
    values={'Styles': [('n', 'normal'), ('i', 'italic')]},
    docstring=__doc__
)
