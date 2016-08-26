{% extends "base.md" %}
{% import "macros.jj" as pmacros %}
{% block title %}Midnight Service{% endblock %}

{% block content -%}
In the name of the father...

## Prayers
{{pmacros.repetition("Test", 3, verbose=True)}}

## {{psalm(134)}}
{%- endblock %}

