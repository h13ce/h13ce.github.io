---
title: "Scientific Machine Learning & Differentiable Mechanics"
order: 3
summary: >-
  Physics-informed learning, neural operators, differentiable finite elements,
  inverse analysis, and gradient-based computational mechanics.
figure:
  status: "placeholder"
  source_repository: "h13ce/ERCStg"
  source_path: "CV/cv_fno_ferro.png"
  alt: "Fourier neural operator representation of ferroelectric actuator response"
  caption: "Neural-operator modelling of history-dependent ferroelectric response as part of a broader programme in scientific machine learning and differentiable mechanics."
---

My scientific-machine-learning work is built around mechanics problems in which physical structure, sparse measurements, and history dependence matter. I have used physics-informed neural networks for forward and inverse modelling of piezoelectric microsystems, including identification of electromechanical parameters from experimental observations. I have also developed Fourier neural-operator models for history-dependent hysteresis in ferroelectric and ferromagnetic materials, treating the response as an operator between excitation and material-response histories.

The current direction is differentiable computational mechanics. Rather than using a neural surrogate as a separate approximation layer, I am developing differentiable finite-element formulations in which constitutive updates, nonlinear equilibrium, and inverse identification can be differentiated end to end. This provides a common foundation for parameter identification, sensitivity analysis, and physics-constrained learning.

### Figure placeholder

**Selected source:** `h13ce/ERCStg/CV/cv_fno_ferro.png`

For the final homepage this can represent the neural-operator strand. A DiffFEM demonstrator should eventually become the complementary visual for the differentiable-mechanics strand once the public software release and manuscript figures are fixed.
