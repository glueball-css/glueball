"""
Top, right, bottom and left offsets.
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

vals = [
    (-2,    '-2rem'),
    (-1,    '-1rem'),
    (0,     '0'),
    (1,     '1rem'),
    (2,     '2rem'),
]

mdl = CssModule(
    'Coordinates',
    [UP],
    dynamic={
        '.top':     ['top'],
        '.right':   ['right'],
        '.bottom':  ['bottom'],
        '.left':    ['left']},
    values=vals,
    docstring=__doc__
)
