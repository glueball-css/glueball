"""
Border box for relevant elements
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

styles = [
   ('html, body, div, article, aside, section, main, nav, footer, header, form, fieldset, legend, pre, code, a, '
    'h1, h2, h3, h4, h5, h6, p, ul, ol, li, dl, dt, dd, blockquote, figcaption, figure, textarea, table, td, th, '
    'tr, input[type="email"], input[type="number"], input[type="password"], input[type="tel"], input[type="text"], '
    'input[type="url"], .border-box', {'box-sizing': 'border-box'})]

mdl = CssModule(
    'Border box',
    [FULL],
    styles=styles,
    docstring=__doc__
)
