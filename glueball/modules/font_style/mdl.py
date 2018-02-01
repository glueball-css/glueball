"""
Normal or italic
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

mdl = CssModule(
    'Font style',
    [UP],
    dynamic={'.': ['font-style']},
    values=[('n', 'normal'), ('i', 'italic')],
    docstring=__doc__
)
