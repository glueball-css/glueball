from glueball.settings import PSEUDO_LOOKUP

class Selector:
    """Create a css selector from a base and various modifiers.
    The __str__ method provides a string for use in CSS.

    Instance attributes
    -------------------
    base:       Base selector
    kind:       Extracted from elem:
                    '' = element
                    '.' = class
                    '#' = id
    pseudo:     Pseudo selector to be affixed
    value:      Value to be affixed
    media:      Media modifier to be affixed
    """
    def __init__(self, elem, pseudo=None, value=None, media=None):
        if elem[0] in ['.', '#']:
            self.kind = elem[0]
            self.base = elem[1:]
        else:
            self.kind = ''
            self.base = elem
        self.pseudo = pseudo
        self.value = value
        self.media = media

    def create_media(self, media):
        """Create a duplicate instance, with media modifier added"""
        return Selector(self.kind+self.base, self.pseudo, self.value, media)

    def __str__(self):
        """Build the CSS string representation:

        <kind>[<media>_][<hover>_]<base>[[-]<value][:<hover]
        ---> .sm_hover_bgc-red:hover
        ---> .ml3
        ---> blockquote
        """

        # Switch id or element to class selector if any modifiers have been used
        s = "." if any([self.value, self.pseudo, self.media]) else self.kind
        # media prefix, i.e. "sl_"
        if self.media:
            s += self.media + '_'
        # pseudo prefix, i.e. "hover_"
        if self.pseudo:
            s += self.pseudo + '_'
        s += self.base
        # value suffix, i.e. "-left" or "10p"
        if self.value:
            # No hyphen when the value is a (negative) number or the base is an empty string
            if self.value[0].isdigit() or self.value[0] == '-' or not self.base:
                s += self.value
            else:
                s += '-' + self.value
        # pseudo suffix, i.e. ":hover"
        if self.pseudo:
            s += ":" + PSEUDO_LOOKUP[self.pseudo]
        return s
