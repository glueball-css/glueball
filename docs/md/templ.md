# module: {{ mdl.name }}
{{ mdl.docstring }}

{% if mdl.styles %}
## Basic styles

The basic styles do not depend on the provided values.
They do however adhere to the breakpoints and pseudo selectors.

```css
{% for style in mdl.styles %}
{{ style.__str__() }}
{% endfor %}
```
{% endif %}


{% if mdl.static %}
## Static declarations
A static declaration is not altered by the provided values.

{% for prop, val in mdl.static.items() %}
+ `{{ prop }}: {{ val }};`
{% endfor %}
{% endif %}

{% if mdl.dynamic %}
## Dynamic properties
The value of a dynamic property is determined by the provided values.

| Base selector | Dynamic props |
| ------------- | ------------- |
{% for base, props in mdl.dynamic.items() %}| `{{ base }}` |{% for prop in props %}`{{ prop }}`{{ ", " if not loop.last }}|{% endfor %}
{% endfor %}
{% endif %}


{% if mdl.values %}
## Provided values
The following values determine the dynamic properties and selectors.

Suffix  | Value
--------- | ---------
{% for sfx, val in mdl.values %}`{{sfx}}` | `{{ val }}`
{% endfor %}
{% endif %}


## Media
{% set media = mdl._breakpoints.media_table() %}
{% set bps = mdl._breakpoints.bp_table(mdl.media) %}

{% include 'docs/md/media-table.md' %}


{% if mdl.pseudos %}
## Pseudo selectors
The following pseudo selectors are available:
{% for pseudo, (pseudo_media, vals) in mdl.pseudos.items() %}
### {{ pseudo }}
The pseudo selector `{{ pseudo }}` has the following media queries available:
{% set bps = mdl._breakpoints.bp_table(pseudo_media) %}
{% include 'docs/md/media-table.md' %}

{% endfor %}
{% endif %}


## CSS rules
```css
{% for rule in mdl.get_all_rules() %}
{{ rule.__str__() }}
{% endfor %}
```

- - - - -
_**note: This documentation was auto-generated from the source files.**_
- - - - -