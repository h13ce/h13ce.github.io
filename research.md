---
layout: page
title: "Research"
permalink: /research/
---

My research spans computational mechanics, functional materials, scientific machine learning, MEMS, and multiscale modelling. The homepage is organized around five research directions.

{% assign research_items = site.research | sort: "order" %}
{% for item in research_items %}
## [{{ item.title }}]({{ item.url | relative_url }})

{{ item.summary }}

{% if item.figure_placeholder %}
*Figure placeholder: {{ item.figure_placeholder }}*
{% endif %}
{% endfor %}

## Foundations

Earlier and continuing methodological work includes finite and boundary element methods, isogeometric analysis, nonlinear and multiphysics mechanics, and inverse problems.
