"""
Width for all borders and individual borders
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, SPACING
from ...core import CssModule


mdl = CssModule(
    'Border width',
    [UP],
    dynamic={
        '.bw': ['border-width'],
        '.btw': ['border-top-width'],
        '.brw': ['border-right-width'],
        '.bbw': ['border-bottom-width'],
        '.blw': ['border-left-width']},
    values=SPACING,
    docstring=__doc__
)
