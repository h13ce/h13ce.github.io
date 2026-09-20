---
layout: page
title: "Binh Huy Nguyen"
permalink: /
---

**Tenure-track Assistant Professor**  
CEMEF · Mines Paris–PSL

Computational mechanics · Functional materials · Scientific machine learning · MEMS

I develop computational and experimental approaches for nonlinear multiphysics systems, connecting material modelling, device-scale characterization, differentiable simulation, and multiscale mechanics. Across these directions, a recurring theme is to connect internal material behaviour with observable structural response and to make that connection useful for simulation, identification, and design.

[Research]({{ "/research/" | relative_url }}) · [Publications]({{ "/publications/" | relative_url }}) · [Software]({{ "/software/" | relative_url }}) · [CV]({{ "/cv/" | relative_url }}) · [Google Scholar](https://scholar.google.com/citations?user=zMf1WedEf5gC&hl=en) · [ORCID](https://orcid.org/0000-0003-0830-3121) · [GitHub](https://github.com/h13ce)

## Research

{% assign research_items = site.research | sort: "order" %}
{% for item in research_items %}
### [{{ item.title }}]({{ item.url | relative_url }})

{{ item.summary }}

*Representative figure selected; web asset pending design pass.*
{% endfor %}

## Selected publications

The publication layer is prepared at [Publications]({{ "/publications/" | relative_url }}). A small set of representative papers will be highlighted here after the research-page narrative and visual system are fixed.

## Software

[DiffFEM](https://github.com/h13ce/difffem) is the first software project planned for this section: a JAX-based differentiable finite-element framework for forward, inverse, and multiphysics simulation.
