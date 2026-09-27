# Research figure sources and web exports

The first visual version uses all five author-controlled primary selections below. Source documents and proposal text are not included in this repository. This README is excluded from the generated site.

## Primary selections

| Research theme | Selected source | Intended role |
| --- | --- | --- |
| Ferroelectric MEMS | `h13ce/ERCStg/Figures/Microbender_sample_exp_setup.png` | Experimental anchor: device + LDV characterization |
| Flexoelectric MEMS & Microfabrication | `h13ce/ERCStg/CV/cv_flexo_exp.svg` | Fabrication/experiment showcase |
| Scientific Machine Learning & Differentiable Mechanics | `h13ce/ERCStg/CV/cv_fno_ferro.png` | Neural-operator demonstrator; later pair with DiffFEM |
| Multiscale Computational Mechanics | `h13ce/ERCStg/Figures/stress_vM_11_FNO_512_m11_compressed.pdf` | Resolved heterogeneous stress field |
| Nonlinear & Topological Phononics | `h13ce/ERCStg/CV/cv_TI_bistable.svg` | Bistable mechanism and switchable topological state |

## Secondary candidates

- Ferroelectric MEMS: `CV/cv_ferro_solid.svg`, `CV/cv_ferro.svg`
- Flexoelectric MEMS: `Figures/ProcessFlow.eps`, `Figures/XSEM.eps`, `CV/cv_flexo_sim2.png`
- Scientific ML: `Figures/FNO_Ferro_actuator.pdf`, future public DiffFEM figures
- Multiscale mechanics: `CV/cv_homogenization.png`
- Topological phononics: `CV/cv_TI_soft.svg`, `Figures/Hex_Annular_30x30_WP_defect_t97.pdf`

## Asset rule

Prefer original author-controlled artwork or regenerated plots over publisher-typeset composite figures. Keep the scientific content unchanged while adapting crop, resolution, and typography for the web.


## Incorporated assets

| Web asset | Export |
| --- | --- |
| `ferroelectric-mems.webp` | Original 976 × 380 PNG converted to WebP, quality 92. |
| `flexoelectric-mems.svg` | Inkscape plain SVG, drawing-sized viewBox; editor metadata removed. |
| `scientific-ml.webp` | Original 569 × 517 PNG converted to WebP, quality 92; no upscaling. |
| `multiscale-mechanics.webp` | PDF rendered with Poppler at 1600 px maximum dimension; exterior white margin trimmed, all legends retained; WebP quality 92. |
| `topological-phononics.svg` | Inkscape plain SVG, drawing-sized viewBox; editor metadata removed. |

SVGs are self-contained (embedded image data, no external references). The
phononics source includes raster panels, whose original resolution is preserved.
No scientific panel was removed or recoloured. Layout uses object containment,
not image cropping. Alt text and captions live alongside research narratives.

## Additional work figures — second visual pass

Derivatives in `../works/` preserve complete scientific panels, labels, and scales.
PNG sources were converted to WebP at quality 92 without upscaling. The PDF
was rendered with Poppler at a 1400 px maximum dimension, then encoded as WebP.

| Work | Source in h13ce/ERCStg |
| --- | --- |
| ferro-microactuator | Figures/Microcantilever-LDV-measurement.png |
| afe-actuator | Figures/AFE-AFE-like.png |
| electro-gradient-semiconductor | Figures/Flexo_semiconductor.png |
| pinn-microbender | Figures/PINNs_Piezo.png |
| tunable-topological | Figures/Hex_Annular_30x30_WP_defect_t97.pdf |
