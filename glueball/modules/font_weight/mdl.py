"""
Only numbers, not bold or normal
"""

from defaults import *
from utils import CssModule, Style


vals = ([str(i) for i in range(1, 10)], [str(i) for i in range(100, 901, 100)])

mdl = CssModule(
    'Font weight',
    BREAKPOINTS,
    [UP],
    dynamic={'.fw': ['font-weight']},
    values={'Weights': vals},
    docstring=__doc__
)
