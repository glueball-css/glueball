from .mediarule import MediaRule


class Breakpoints:
    """Breakpoints for media and methods to generate CSS media-rules

    Instance attributes
    -------------------
    _bps:       Dict of breakpoint name and min-width value
    _unit:      Unit for the values
    _index      Tuple of breakpoint keys sorted by the values (for convenience)
    """

    def __init__(self, breakpoints, breakpoint_unit='em'):
        self._bps = breakpoints
        self._unit = breakpoint_unit
        self._index = []
        self._make_index()

    def _make_index(self):
        """Create a list of keys sorted by value for convenience"""
        self._index = [y for x, y in sorted(zip([float(v) for v in self._bps.values()], self._bps.keys()))]

    def _next_biggest(self, bp):
        """Next biggest breakpoint name or None of biggest"""
        return self._index[self._index.index(bp)+1] if self._index.index(bp)+1 < len(self._index) else None

    def _min_size(self, bp):
        """Return minimal size + unit for given breakpoint or None for smallest breakpoint"""
        if self._bps[bp] > 0:
            return self._bps[bp], self._unit
        return None

    def _max_size(self, bp):
        """Return maximum size for given breakpoint or None for largest breakpoint"""
        if self._next_biggest(bp):
            return self._bps[self._next_biggest(bp)] - 0.01, self._unit
        return None

    def make_media(self, lower='', upper='', styles=None):
        """Create media-rule with media style rules for given breakpoints"""
        no_upper = not upper or upper == self._index[-1]
        no_lower = not lower or lower == self._index[0]

        if no_upper and no_lower:
            # No media queries
            return MediaRule(styles=styles)
        elif no_upper:
            # Lower bound media query
            return MediaRule(
                {'min-width': self._min_size(lower)},
                [style.create_media(lower) for style in styles]
            )
        elif no_lower:
            # Upper bound media query
            return MediaRule(
                {'max-width': self._max_size(upper)},
                [style.create_media(self._index[0]+upper) for style in styles]
            )
        else:
            # Upper and lower bound media queries
            return MediaRule({
                'min-width': self._min_size(lower),
                'max-width': self._max_size(upper)},
                [style.create_media(lower + upper) for style in styles]
            )

    def media_full(self):
        """List with single query string with max upper and min lower bound"""
        return [self._index[0]+self._index[-1]]

    def media_up(self):
        """Return list of lower bound query strings (maximum upper bound)"""
        return [lower+self._index[-1] for lower in self._index]

    def media_down(self):
        """Return list of upper bound query strings (minimal lower bound)"""
        return [self._index[0]+upper for upper in self._index[::-1]]

    def media_only(self):
        """Return list of query strings only for every exact breakpoint"""
        return [bp+bp for bp in self._index]

    def media_other(self):
        """Every query that was not covered by the other functions"""
        results = []
        if len(self._index) < 4:
            return results
        for lower in self._index[1:-2]:  # First and last covered by media_up and down
            for upper in self._index[2:-1][::-1]:  # Reverse order to get largest first
                if lower != upper:
                    results.append(lower+upper)
        return results

    def all_breakpoints(self, media):
        """Compile a single list of query strings from strings and methods"""
        breakpoints = []
        for bp in media:
            if type(bp) is str:
                if bp not in breakpoints:
                    breakpoints.append(bp)
            else:
                # bp is a method that returns a list of query strings
                query_strings = bp()
                for query in query_strings:
                    if query not in breakpoints:
                        breakpoints.append(query)
        return breakpoints

    def all_media_rules(self, media, styles):
        """Create all requested media rules"""
        media_rules = []
        for bp in self.all_breakpoints(media):
            # Split the query string in upper and lower breakpoint
            lower, upper = bp[:int(len(bp) / 2)], bp[int(len(bp) / 2):]
            media_rules.append(self.make_media(lower, upper, styles))
        return media_rules

    def _max_templ(self, bp):
        """For use in template
        Return large number instead of None for max size"""
        if self._next_biggest(bp):
            return self._bps[self._next_biggest(bp)] - 0.01
        return 9999

    def media_table(self):
        """For use in template
        List of (key, min-size, max-size) for all breakpoints"""
        return [(bp, self._bps[bp], self._max_templ(bp)) for bp in self._index]

    def bp_table(self, media):
        """For use in template
        List of (suffix, lower, upper) for all query strings"""
        bps = []
        for bp in self.all_breakpoints(media):
            bp_item = []  # bp string, min, max
            lower, upper = bp[:int(len(bp) / 2)], bp[int(len(bp) / 2):]
            bp_string = ''
            if not (lower == self._index[0] and upper == self._index[-1]):
                bp_string += lower
            if upper != self._index[-1]:
                bp_string += upper
            bp_item.append(bp_string)
            bp_item.append(self._bps[lower])
            bp_item.append(self._max_templ(upper))
            bps.append(bp_item)
        return bps
