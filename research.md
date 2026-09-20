---
layout: page
title: "Research"
permalink: /research/
---

My research developed from computational mechanics and higher-order multiphysics modelling toward experimental MEMS, scientific machine learning, differentiable simulation, and multiscale mechanics. The five directions below are presented as connected research streams rather than isolated topics.

{% assign research_items = site.research | sort: "order" %}
{% for item in research_items %}
## [{{ item.title }}]({{ item.url | relative_url }})

{{ item.summary }}

{% if item.figure %}
*Figure placeholder — selected source: `{{ item.figure.source_repository }}/{{ item.figure.source_path }}`*
{% endif %}
{% endfor %}

## Computational foundations

The research programme is supported by earlier and continuing work in finite and boundary element methods, isogeometric analysis, nonlinear and multiphysics mechanics, fracture, inverse problems, and parameter identification. These methods remain part of the computational foundation rather than separate top-level homepage themes.
