# Scientific media derivatives

Original scientific media remain unchanged in `FerroActuator/` and `TI/`.
Web playback uses the existing Polytec MP4 and the derivatives below.

| Derivative | Source | Encoding |
| --- | --- | --- |
| derived/ferro-minor-loop.mp4 | FerroActuator/Minor_bipolar_butterfly.gif | H.264, CRF 18, yuv420p, faststart; original timing and panels retained. |
| derived/topological-wave.mp4 | TI/Structure_Hex_Annular_30x30_3models_2.avi | H.264, CRF 20, yuv420p, faststart; original timing and all three panels retained. |

FFmpeg pads to even dimensions if needed; it does not crop, recolour, or change
scientific scales. The GIF derivative is 1920 × 976 (3.6 seconds); the topological
derivative is 1454 × 936 (4 seconds). Existing Polytec video is H.264/yuv420p,
1524 × 910 (approximately 10.93 seconds).

Posters are WebP frames: 3.3 seconds for the minor-loop response, 2.8 seconds for
the topological field, and the first frame for Polytec. Videos have controls,
playsinline, preload none, no autoplay, and no automatic loop. The GIF is only
linked explicitly; the AVI is never embedded and is excluded from the built site.
The original source paths remain in the works data for provenance.

Conversion was performed in the repository's temporary `visual-pass-2-media`
preparation branch using read-only repository permissions and artifact output.
No workflow writes to main or changes GitHub Pages deployment settings.
