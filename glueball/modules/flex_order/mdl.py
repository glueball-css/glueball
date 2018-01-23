"""
The order property changes the default ordering of flex items.
"""
from defaults import *
from utils import CssModule, Style

# Make sure we have an ordering option for every fractional item
vals = [str(i) for i in range(max(DENOMINATORS+[10])+1)]
# And if you want it at the end, or really at the end, or really really
vals.extend(['99', '999', '9999', '99999'])

mdl = CssModule(
    'Flex order',
    BREAKPOINTS,
    [UP],
    dynamic={'.fxo': ['order']},
    values={'Order options': [vals, vals]},
    docstring=__doc__
)
