"""
Vertical alignment of inline and inline-blocks inside a block-element.
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = [
    ('t',       'top'),
    ('b',       'bottom'),
    ('tt',      'text-top'),
    ('tb',      'text-bottom'),
    ('m',       'middle'),
    ('sup',     'super'),
    ('sub',     'sub'),
    ('base',    'baseline'),
]


mdl = CssModule(
    'Vertical align',
    [FULL],
    dynamic={'.va': ['vertical-align']},
    values={'Alignment options': vals},
    docstring=__doc__
)
