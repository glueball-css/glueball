"""
Captions, border collapse, table layout, empty cells and table border spacing
"""
from defaults import *
from utils import CssModule, Style

styles = [
    Style('.tcs-t', {'caption-side': 'top'}),
    Style('.tcs-b', {'caption-side': 'bottom'}),
    Style('.tbc-s', {'border-collapse': 'separate'}),
    Style('.tbc-c', {'border-collapse': 'collapse'}),
    Style('.tl-a', {'table-layout': 'auto'}),
    Style('.tl-f', {'table-layout': 'fixed'}),
    Style('.tec-s', {'empty-cells': 'show'}),
    Style('.tec-h', {'empty-cells': 'hide'}),
]


mdl = CssModule(
    'Table',
    BREAKPOINTS,
    [FULL],
    styles=styles,
    dynamic={'.tbs': ['table-border-spacing']},
    values={'Spacing': SPACING},
    docstring=__doc__
)
