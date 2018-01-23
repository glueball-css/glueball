"""
Style for all borders and individual borders
"""
from defaults import *
from utils import CssModule, Style


mdl = CssModule(
    'Border style',
    BREAKPOINTS,
    [UP],
    dynamic={
        '.bs': ['border-style'],
        '.bts': ['border-top-style'],
        '.brs': ['border-right-style'],
        '.bbs': ['border-bottom-style'],
        '.bls': ['border-left-style']},
    values={'Styles': [('n', 'dashed', 'dotted', 'solid'), ('none', 'dashed', 'dotted', 'solid')]},
    docstring=__doc__
)
