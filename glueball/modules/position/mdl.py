"""
Options
"""

from defaults import *
from utils import CssModule, Style


mdl = CssModule(
    'Position',
    BREAKPOINTS,
    [UP],
    dynamic={'.p': ['position']},
    values={'Values': [('s', 'r', 'a', 'f'), ('static', 'relative', 'absolute', 'fixed')]},
    docstring=__doc__
)
