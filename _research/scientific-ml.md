---
title: Scientific Machine Learning & Differentiable Mechanics
order: 3
summary: I use physics-informed learning and neural operators for mechanics problems
  shaped by sparse measurements and history dependence. Differentiable finite elements
  connect forward simulation, parameter sensitivities, and inverse identification.
figure:
  alt: Fourier neural operator representation of ferroelectric actuator response
  caption: Neural-operator modelling of history-dependent ferroelectric response as
    part of a broader programme in scientific machine learning and differentiable
    mechanics.
  path: /assets/images/research/scientific-ml.webp
  width: 569
  height: 517
kicker: Learning & differentiable simulation
---
My scientific-machine-learning work is built around mechanics problems in which physical structure, sparse measurements, and history dependence matter. I have used physics-informed neural networks for forward and inverse modelling of piezoelectric microsystems, including identification of electromechanical parameters from experimental observations. I have also developed Fourier neural-operator models for history-dependent hysteresis in ferroelectric and ferromagnetic materials, treating the response as an operator between excitation and material-response histories.

The current direction is differentiable computational mechanics. Rather than using a neural surrogate as a separate approximation layer, I am developing differentiable finite-element formulations in which constitutive updates, nonlinear equilibrium, and inverse identification can be differentiated end to end. This provides a common foundation for parameter identification, sensitivity analysis, and physics-constrained learning.
