"""
Options for repeating background images
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

styles = [
    ('.c-fix', {'*zoom': '1'}),
    ('.c-fix:before, .c-fix:after', {'content': '" "', 'display': 'table'}),
    ('.c-fix:after', {'clear': 'both'})
]

vals = [
    ('l',   'left'),
    ('r',   'right'),
    ('b',   'bottom'),
    ('n',   'none'),
]

mdl = CssModule(
    'Clear',
    BREAKPOINTS,
    [FULL],
    styles=styles,
    dynamic={'.c': ['clear']},
    values={'Options': vals},
    docstring=__doc__
)
