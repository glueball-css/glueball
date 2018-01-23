"""
Top, right, bottom and left offsets.
"""
from defaults import *
from utils import CssModule, Style


mdl = CssModule(
    'Coordinates',
    BREAKPOINTS,
    [UP],
    dynamic={
        '.top': ['top'],
        '.right': ['right'],
        '.bottom': ['bottom'],
        '.left': ['left']},
    values={'Offsets': [('-2', '-1', '0', '1', '2'), ('-2rem', '-1rem', '0', '1rem', '2rem')]},
    docstring=__doc__
)
