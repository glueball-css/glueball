"""
Selection of list style types
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = (
    'disc',
    'none',
    'circle',
    'square',
    'decimal',
    'cjk-decimal',
    'decimal-leading-zero',
    'lower-alpha',
    'lower-greek',
    'lower-latin',
    'lower-roman',
    'upper-alpha',
    'upper-greek',
    'upper-latin',
    'upper-roman',
)


mdl = CssModule(
    'List style type',
    [FULL],
    dynamic={'.lst': list(zip(vals, vals))},
    values={'Types': vals},
    docstring=__doc__
)
