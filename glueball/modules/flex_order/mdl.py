"""
The order property changes the default ordering of flex items.
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, DENOMINATORS
from ...core import CssModule

# Make sure we have an ordering option for every fractional item (and minimally 10)
vals = list(range(max(DENOMINATORS+[10])+1)) + [99, 999, 9999, 99999]

mdl = CssModule(
    'Flex order',
    [UP],
    dynamic={'.fxo': ['order']},
    values={'Order options': zip(vals, vals)},
    docstring=__doc__
)
