"""
Selection of list style types
"""
from defaults import *
from utils import CssModule, Style

vals = (
    ['disc', 'n', 'circle', 'square', 'deci', 'cjkdeci', 'decilz', 'lowa', 'lowg', 'lowl', 'lowr', 'upa', 'upg', 'upl', 'upr'],
    ['disc',
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
        'upper-roman']
)

mdl = CssModule(
    'List style type',
    BREAKPOINTS,
    [FULL],
    dynamic={'.lst': ['letter-style-type']},
    values={'Types': vals},
    docstring=__doc__
)
