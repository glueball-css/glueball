"""
Captions, border collapse, table layout, empty cells and table border spacing
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, SPACING
from ...core import CssModule

styles = [
    ('.tcs-t', {'caption-side': 'top'}),
    ('.tcs-b', {'caption-side': 'bottom'}),
    ('.separate', {'border-collapse': 'separate'}),
    ('.collapse', {'border-collapse': 'collapse'}),
    ('.tl-a', {'table-layout': 'auto'}),
    ('.tl-f', {'table-layout': 'fixed'}),
    ('.tec-s', {'empty-cells': 'show'}),
    ('.tec-h', {'empty-cells': 'hide'}),
    ('.odd_striped-gray-95:nth-child(odd)', {'background-color': 'hsl(0, 0%, 98%)'}),
    ('.odd_striped-gray-90:nth-child(odd)', {'background-color': 'hsl(0, 0%, 95%)'}),
    ('.even_striped-gray-95:nth-child(even)', {'background-color': 'hsl(0, 0%, 98%)'}),
    ('.even_striped-gray-90:nth-child(even)', {'background-color': 'hsl(0, 0%, 95%)'}),
]

mdl = CssModule(
    'Table',
    [FULL],
    styles=styles,
    dynamic={'.tbs': ['border-spacing']},
    values={'Spacing': SPACING},
    docstring=__doc__
)
