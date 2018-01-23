"""
Width for all borders and individual borders
"""
from defaults import *
from utils import CssModule, Style


mdl = CssModule(
    'Border width',
    BREAKPOINTS,
    [UP],
    dynamic={
        '.bw': ['border-width'],
        '.btw': ['border-top-width'],
        '.brw': ['border-right-width'],
        '.bbw': ['border-bottom-width'],
        '.blw': ['border-left-width']},
    values={'Spacing': SPACING,},
    docstring=__doc__
)
