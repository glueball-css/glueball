"""
Options for repeating background images
"""
from defaults import *
from utils import CssModule, Style

mdl = CssModule(
    'Background repeat',
    BREAKPOINTS,
    [FULL],
    dynamic={'.bgr': ['background-repeat']},
    values={'Values': [('n', 'x', 'y'), ('no-repeat', 'repeat-x', 'repeat-y')]},
    docstring=__doc__
)
