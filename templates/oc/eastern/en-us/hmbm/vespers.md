{% extends "base.md" %}
{% import "macros.jj" as pmacros %}
{% import "common/common.jj" as common %}
{% block title %}Vespers{% endblock %}

{% block content -%}
{{ common.theusual() }}

## Psalm 104(103)
{{ psalm(104) }}

{% set psalms = cycle_psalms_weekly([141,142]) %}
{% for psalm_num in psalms %}
## Psalm {{psalm_num}}
{{psalm(psalm_num)}}
{%endfor%}
{{pmacros.repetition(pmacros.lhm(), 3, verbose=False)}}
Through the prayers of our holy fathers, may the Lord have mercy on us. Amen.
{%- endblock %}

