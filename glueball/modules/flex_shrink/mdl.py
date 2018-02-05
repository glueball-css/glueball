"""
Flex shrink.
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, DENOMINATORS
from ...core import CssModule

vals = list(zip(range(10), range(10)))

mdl = CssModule(
    'Flex shrink',
    [UP],
    dynamic={'.fs': ['flex-shrink']},
    values=vals,
    docstring=__doc__
)
