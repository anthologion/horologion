{% extends "base.md" %}
{% import "macros.jj" as pmacros %}
{% block title %}Midnight Service{% endblock %}

{% block content -%}
In the name of the father...

## Prayers
{{pmacros.repetition("Test", 3, verbose=True)}}

{% set psalms = cycle_psalms_weekly([121,134]) %}
{% for psalm_num in psalms %}
## Psalm {{psalm_num}}
{{psalm(psalm_num)}}
{%endfor%}
{%- endblock %}

