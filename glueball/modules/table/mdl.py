"""
Captions, border collapse, table layout, empty cells and table border spacing
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, SPACING
from ...core import CssModule

styles = [
    ('.tcs-t', {'caption-side': 'top'}),
    ('.tcs-b', {'caption-side': 'bottom'}),
    ('.tbc-s', {'border-collapse': 'separate'}),
    ('.tbc-c', {'border-collapse': 'collapse'}),
    ('.tl-a', {'table-layout': 'auto'}),
    ('.tl-f', {'table-layout': 'fixed'}),
    ('.tec-s', {'empty-cells': 'show'}),
    ('.tec-h', {'empty-cells': 'hide'}),
]

mdl = CssModule(
    'Table',
    [FULL],
    styles=styles,
    dynamic={'.tbs': ['border-spacing']},
    values={'Spacing': SPACING},
    docstring=__doc__
)
