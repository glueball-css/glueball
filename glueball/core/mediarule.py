

class MediaRule:
    """Represents a CSS media rule

    Instance attributes
    -------------------
    features:       Dict of feature and value, i.e. 'min-width' and ('36', 'em',)
    styles:         List of StyleRules contained in MediaRule
    application:    'not'|'only'
    media_type:     'all'|'print'|'screen'|'speech'
    """

    def __init__(self, features=None, styles=None, application=None, media_type=None,):
        self.features = features or {}
        self.styles = styles or []
        self.application = application
        self.media_type = media_type

    def __str__(self):
        # TODO application and media_type not yet implemented
        rules = "\n".join([str(style) for style in self.styles])

        if self.features:
            # Media-rule contains style-rules
            media_selector = " and ".join(["({}: {}{})".format(k, str(v[0]), v[1]) for k, v in self.features.items()])
            return "\n@media {} {{\n{}\n}}".format(media_selector, rules)

        # Without any features or media types, the style-rules will not be contained in a media-rule
        return rules
