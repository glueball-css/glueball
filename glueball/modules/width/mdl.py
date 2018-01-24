"""
Percentages and values for width
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY, DENOMINATORS, SIZING, PERCENTAGES
from ...core import CssModule

# fractions = ([], [])
#
# for den in DENOMINATORS:
#     for num in range(1, den):
#         fractions[0].append('%d-%d' % (num, den))
#         fractions[1].append('{:.5%}'.format(num/den))

fractions = [('%d-%d' % (num, den), '{:.5%}'.format(num/den)) for den in DENOMINATORS for num in range(1, den)]

mdl = CssModule(
    'Width',
    [UP],
    dynamic={'.w': ['width']},
    values={'Modifiers': SIZING, 'Percentages': PERCENTAGES, 'Fractions': fractions},
    docstring=__doc__
)
