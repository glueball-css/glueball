"""
Options for repeating background images
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

styles = [
    ('.clear-fix', {'*zoom': '1'}),
    ('.clear-fix:before, .c-fix:after', {'content': '" "', 'display': 'table'}),
    ('.clear-fix:after', {'clear': 'both'})
]

vals = [
    ('l',   'left'),
    ('r',   'right'),
    ('b',   'bottom'),
    ('n',   'none'),
]

mdl = CssModule(
    'Clear',
    [FULL],
    styles=styles,
    dynamic={'.clear': ['clear']},
    values=vals,
    docstring=__doc__
)
