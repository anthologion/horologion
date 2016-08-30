{% extends "base.md" %}
{% import "macros.jj" as pmacros %}
{% import "common/common.jj" as common %}
{% block title %}Midnight Service{% endblock %}

{% block content -%}
In the name of the Father and of the Son and of the Holy Spirit. Amen.

{{ common.comeletus() }}

## Prayers
Now that You have raised me from my bed of sleep, O Lord, enlighten my mind and
heart. Open my lips that I may sing to You: Holy, Holy, Holy are You, O God!

Having risen from sleep, I thank You, O Holy Trinity, for in Your great
goodness and forbearance You have not become angry with me in my negligence and
sinfulness, nor have You destroyed me in my transgressions, but in Your
compassion You have raised me up as I lay in despair that I might sing the
glories of Your majesty. Through the prayers of the Theotokos, have mercy on us! 

Enlighten the eyes of my understanding. Open my heart to receive Your words;
teach me Your commandments; help me to do Your will, confessing You from my
heart, singing and praising Your all-holy name of the Father and of the Son and
of the Holy Spirit, now and ever and unto ages of ages. Amen. 


{% set psalms = cycle_psalms_weekly([121,134]) %}
{% for psalm_num in psalms %}
## Psalm {{psalm_num}}
{{psalm(psalm_num)}}
{%endfor%}
{{pmacros.repetition(pmacros.lhm(), 3, verbose=False)}}
Through the prayers of our holy fathers, may the Lord have mercy on us. Amen.
{%- endblock %}

