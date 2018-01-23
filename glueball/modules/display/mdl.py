"""
Controls display property
"""

from defaults import *
from utils import CssModule, Style

values = {
    'Display options': (
        ('n', 'i', 'b', 'ib', 'it', 't', 'tcell', 'trow', 'trowg', 'tcol', 'tcolg', 'f', 'if',),
        ('none', 'inline', 'block', 'inline-block', 'inline-table', 'table', 'table-cell', 'table-row',
            'table-row-group', 'table-column', 'table-column-group', 'flex', 'inline-flex',)
    )
}

mdl = CssModule(
    'Display',
    BREAKPOINTS,
    [UP, DOWN],
    dynamic={'.d': ['display']},
    values=values,
    docstring=__doc__
)
