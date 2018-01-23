"""
Modifiers, also negative
"""
from defaults import *
from utils import CssModule, Style

vals = (
    ['-2', '-1', 'n', '1', '2', '3', '4'],
    ['-0.125em', '-0.0625em', 'normal', '0.0625em', '0.125em', '0.25em', '0.5em']
)

mdl = CssModule(
    'Letter spacing',
    BREAKPOINTS,
    [FULL],
    dynamic={'.ls': ['letter-spacing']},
    values={'Spacings': vals},
    docstring=__doc__
)
