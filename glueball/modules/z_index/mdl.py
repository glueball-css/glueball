"""
Place
"""
from defaults import *
from utils import CssModule, Style

val = [str(i) for i in range(10)] + ['99', '999', '9999', '99999']

mdl = CssModule(
    'Z index',
    BREAKPOINTS,
    [UP],
    dynamic={'.z': ['z-index']},
    values={'Values': (val, val)},
    docstring=__doc__
)
