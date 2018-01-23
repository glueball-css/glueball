import re
from .selector import Selector


class StyleRule:
    """Represents a CSS style rule

    Selector can be a string or a list of Selector objects. A string will be parsed into
    a list of selectors, together with the pseudo and value modifiers.

    Instance attributes
    -------------------
    selectors:      List of Selector objects
    declarations:   Dictionary of CSS declarations (property + value)
    """
    def __init__(self, selectors, declarations, pseudo=None, value=None):
        self.declarations = declarations or {}
        if type(selectors) is str:
            self.selectors = [Selector(elem, pseudo, value) for elem in re.split(',\s+', selectors)]
        else:
            self.selectors = selectors

    def create_media(self, media):
        """Create a duplicate with media modifier"""
        return StyleRule([sel.create_media(media) for sel in self.selectors], self.declarations)

    def __str__(self):
        decl = " ".join(["{}: {};".format(k, str(v)) for k, v in self.declarations.items()])
        return "%s { %s }" % (", ".join([str(s) for s in self.selectors]), decl)
