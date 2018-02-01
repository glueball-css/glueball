"""
Controls display property
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = [
    ('n',       'none'),
    ('i',       'inline'),
    ('b',       'block'),
    ('ib',      'inline-block'),
    ('it',      'inline-table'),
    ('t',       'table'),
    ('tcell',   'table-cell'),
    ('trow',    'table-row'),
    ('trowg',   'table-row-group'),
    ('tcol',    'table-column'),
    ('tcolg',   'table-column-group'),
    ('f',       'flex'),
    ('if',      'inline-flex')
]

mdl = CssModule(
    'Display',
    [UP, DOWN],
    dynamic={'.d': ['display']},
    values=vals,
    docstring=__doc__
)
