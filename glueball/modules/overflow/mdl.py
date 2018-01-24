"""
Modifiers
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = [('v', 'visible'), ('h', 'hidden'), ('s', 'scroll'), ('a', 'auto')]

mdl = CssModule(
    'Overflow',
    [UP],
    dynamic={
        '.o': ['overflow'],
        'ox': ['overflow-x'],
        'oy': ['overflow-y']},
    values={'Values': vals},
    docstring=__doc__
)
