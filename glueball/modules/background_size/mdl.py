"""
Contain or cover
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = (
    ('contain', 'contain'),
    ('cover', 'cover')
)

mdl = CssModule(
    'Background size',
    [UP],
    dynamic={'.': ['background-size']},
    values=vals,
    docstring=__doc__
)
