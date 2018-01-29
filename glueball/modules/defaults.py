"""
Defaults for CSS modules
"""
import itertools

from glueball.core import Breakpoints
from glueball.hsla import Hsla, HUES

BREAKPOINTS = Breakpoints({
    't': 0,
    's': 36,
    'm': 48,
    'l': 62,
    'x': 75,
})

# shortcut methods
FULL = BREAKPOINTS.media_full  # No media query: equal to query string 'tx'
ONLY = BREAKPOINTS.media_only  # Only specific breakpoints: 'tt', 'ss', 'mm', 'll', 'xx'
UP = BREAKPOINTS.media_up      # Lower bound queries: 'tx', 'sx', 'mx', 'lx', 'xx'
DOWN = BREAKPOINTS.media_down  # Upper bound queries: 'tx', 'tl', 'tm', 'ts', 'tt'

SIZING = list(zip(range(10), (
    '0',
    '1rem',
    '2rem',
    '4rem',
    '8rem',
    '16rem',
    '32rem',
    '48rem',
    '64rem',
    '96rem',
)))

SPACING = list(zip(range(10), (
    '0',
    '0.125rem',
    '0.25rem',
    '0.5rem',
    '1rem',
    '2rem',
    '4rem',
    '8rem',
    '16rem',
    '999rem',
)))

NEGATIVE_SPACING = list(zip(range(-1, -10, -1), (
    '-0.125rem',
    '-0.25rem',
    '-0.5rem',
    '-1rem',
    '-2rem',
    '-4rem',
    '-8rem',
    '-16rem',
    '-999rem',
)))

PERCENTAGES = [('%dp' % i, '%d%%' % i) for i in range(10, 101, 10)]

TYPE_SCALE = list(zip(range(1, 10), (
    '.625rem',
    '.75rem',
    '.875rem',
    '1rem',
    '1.25rem',
    '1.5rem',
    '2rem',
    '2.5rem',
    '3.5rem',
)))

WEIGHT = list(zip(range(1, 10), range(100, 901, 100)))

# For use in width and height fractions and flex-order values.
# This allows for a detailed and versatile grid system.
# Beware: the number of CSS rules increases with the provided values.
# The value 12 may be a sensible maximum.
DENOMINATORS = [5, 7, 12]

# Grays from various luminosities
GRAYS = [Hsla('gray', lum=l) for l in (98, 95, 90, 80, 50, 65, 35, 20, 10, 5)]

# Blacks and whites from various alpha values
BLACKWHITE = [Hsla(h, alpha=a) for h in ['black', 'white'] for a in (100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 2)]

# Colors from a cartesian product of hues, sats and lums
COLORS = [Hsla(*hsl) for hsl in itertools.product(list(HUES)[::3], (100, 60), (92, 70, 50, 25))]

SPECTRUM = COLORS + GRAYS + BLACKWHITE
