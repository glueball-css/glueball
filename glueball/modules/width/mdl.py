"""
Percentages and values for width
"""
from defaults import *
from utils import CssModule, Style

fractions = ([], [])

for den in DENOMINATORS:
    for num in range(1, den):
        fractions[0].append('%d-%d' % (num, den))
        fractions[1].append('{:.5%}'.format(num/den))

mdl = CssModule(
    'Width',
    BREAKPOINTS,
    [UP],
    dynamic={'.w': ['width']},
    values={'Modifiers': SIZING, 'Percentages': PERCENTAGES, 'Fractions': fractions},
    docstring=__doc__
)
