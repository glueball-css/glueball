"""
Selection of list style types
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = [
    ('disc', 'disc'),
    ('n', 'none'),
    ('circle', 'circle'),
    ('square', 'square'),
    ('deci', 'decimal'),
    ('cjkdeci', 'cjk-decimal'),
    ('decilz', 'decimal-leading-zero'),
    ('lowa', 'lower-alpha'),
    ('lowg', 'lower-greek'),
    ('lowl', 'lower-latin'),
    ('lowr', 'lower-roman'),
    ('upa', 'upper-alpha'),
    ('upg', 'upper-greek'),
    ('upl', 'upper-latin'),
    ('upr', 'upper-roman')
]


mdl = CssModule(
    'List style type',
    [FULL],
    dynamic={'.lst': ['list-style-type']},
    values={'Types': vals},
    docstring=__doc__
)
