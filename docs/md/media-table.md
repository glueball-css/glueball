{# Include the breakpoint diagram table.

First column holds the prefixes and next columns the default breakpoints
as defined in {{ media }}.

Each of the tbody rows corresponds with a media query (min and max). A colored
bar represents the coverage of each query.
#}

| Prefix  | {% for m, low, up in media %} >{{ low }} | {% endfor %}
| :------:  | {% for m, low, up in media %} :---------: | {% endfor %}
{% for bp, min, max in bps %}| {% if bp %} `{{bp}}` {% else %} (none) {% endif %} |{% for m, low, up in media %}{% if min <= low and max >= up %}▒▒▒▒▒{% endif %}|{% endfor %}
{% endfor %}
