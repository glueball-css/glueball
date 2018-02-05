"""
Flex grow.
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, DENOMINATORS
from ...core import CssModule

vals = list(zip(range(10), range(10)))

mdl = CssModule(
    'Flex grow',
    [UP],
    dynamic={'.fg': ['flex-grow']},
    values=vals,
    docstring=__doc__
)
