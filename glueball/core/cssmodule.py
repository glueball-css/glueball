import re

from ..settings import DOCSITE
from .stylerule import StyleRule
try:
    from ..modules.defaults import BREAKPOINTS
except ImportError:
    BREAKPOINTS = None


class CssModule:
    """A Stylesheet module that contains media and style rules

    Instance attributes
    -------------------
    name:           Module name, also used for filename slugs
    media:          List of media modifiers (query strings like 'ml' or shortcut methods from Breakpoints instance)
    breakpoints:    Instance of Breakpoints, defaults to BREAKPOINTS from module-defaults if not provided
    styles:         Iterable of arguments to create StyleRules (that will be used without modification)
    static:         Dict of declations which will be applied unchanged to the dynamic selector
    dynamic:        Dict of base selector + list of props which form declarations with the different values
    values:         Dict with two-item iterables which get apppied to base selector and dynamic props
    pseudos:        Dictionary of {pseudo: media list}
    """
    def __init__(self,
                 name,
                 media,
                 breakpoints=None,
                 styles=None,
                 static=None,
                 dynamic=None,
                 values={},
                 pseudos=None,
                 docstring=''):
        self.name = name
        self._breakpoints = breakpoints
        self.media = media

        if breakpoints:
            self._breakpoints = breakpoints
        else:
            self._breakpoints = BREAKPOINTS

        self.styles = []
        if styles:
            for args in styles:
                self.styles.append(StyleRule(*args))

        self.static = static or {}
        self.dynamic = dynamic or {}
        self.values = {k: [(str(t[0]), str(t[1])) for t in v] for k, v in values.items()}
        self.pseudos = pseudos or {}
        self.docstring = docstring

    def get_slug(self):
        s = str(self.name).strip().replace(' ', '_').lower()
        return re.sub(r'(?u)[^-\w.]', '', s)

    def get_url(self):
        return self.get_slug().replace('_', '-')

    def _make_root_rules(self, pseudo=None):
        """Generate a list of style-rules, without media modifier"""
        root_rules = []

        # Include the rules that are not dependent on values
        for style in self.styles:
            root_rules.append(style)

        # Generate the dynamic rules
        for sel, props in self.dynamic.items():
            for vals in self.values.values():
                # vals is a tuple of two-item tuples: [0] selector suffices and [1] declaration values
                for val in vals:
                    decl = {prop: str(val[1]) for prop in props}
                    decl.update(self.static)  # add the static declarations
                    root_rules.append(StyleRule(sel, decl, pseudo, str(val[0])))
        return root_rules

    def get_all_rules(self):
        """Return a list of media-rules, which contain the style-rules with media modifications"""

        # Generate from non-pseudo selectors and media modifiers
        rules = self._breakpoints.all_media_rules(self.media, self._make_root_rules())

        # Generate for every pseudo selector together with own media modifiers
        for pseudo, media in self.pseudos.items():
            rules.extend(self._breakpoints.all_media_rules(media, self._make_root_rules(pseudo)))
        return rules

    def print_rules(self):
        return print(self.get_all_rules())

    def __str__(self):
        header = """
/*
module %s
%s

documentation: %s
*/

""" % (self.name.upper(), self.docstring, DOCSITE+'module/'+self.get_slug())
        return header + '\n'.join([str(r) for r in self.get_all_rules()])