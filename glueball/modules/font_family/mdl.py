"""
System fonts with appropriate fallbacks.
"""

from ..defaults import BREAKPOINTS, UP, DOWN, FULL, ONLY
from ...core import CssModule

families = {
    '.sans': "-apple-system, BlinkMacSystemFont, 'avenir next', avenir, 'helvetica neue', helvetica, ubuntu, roboto, "
             "noto, 'segoe ui', arial, sans-serif",
    '.serif': "georgia, times, serif",
    '.system-sans': "sans-serif",
    '.system-serif': "serif",
    'code, .code': "Consolas, monaco, monospace",
    '.courier': "'Courier Next', courier, monospace",
    '.helvetica': "'helvetica neue', helvertica, sans-serif",
    '.avenir': "'avenir next', avenir, sans-serif",
    '.athelas': "athelas, georgia, serif",
    '.georgia': "georgia, serif",
    '.times': "times, serif",
    '.bodoni': "'Bodoni MT', serif",
    '.calisto': "calisto, serif",
    '.garamond': "garamond, serif",
    '.baskerville': "baskerville, serif",
}

mdl = CssModule(
    'Font family',
    BREAKPOINTS,
    [FULL],
    styles=[(k, {'font-family': v}) for k, v in families.items()],
    docstring=__doc__
)
