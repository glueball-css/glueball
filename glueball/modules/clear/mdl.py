"""
Options for repeating background images
"""
from defaults import *
from utils import CssModule, Style


mdl = CssModule(
    'Clear',
    BREAKPOINTS,
    [FULL],
    styles=[Style('.c-fix', {'*zoom': '1'}),
            Style('.c-fix:before, .c-fix:after', {'content': '" "', 'display': 'table'}),
            Style('.c-fix:after', {'clear': 'both'})],
    dynamic={'.c': ['clear']},
    values={'Options': [('l', 'r', 'b', 'n'), ('left', 'right', 'bottom', 'none')]},
    docstring=__doc__
)
