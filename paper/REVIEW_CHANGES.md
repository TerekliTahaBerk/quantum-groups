# Changes since v1.0.0 (summary for reviewers)

Updated 27 September 2026. No JOSS submission or review exists yet; this is
a factual summary for the author and for future reviewers. The itemized list
is the `[1.1.0]` section of `../CHANGELOG.md`; verification is recorded in
`PREFLIGHT.md`.

**Correctness (commit `bc5c370`).** An audit (`../AUDIT.md`) found that the
historical upper-triangular `R_matrix_V1` intertwines the opposite of the
package coproduct, so the thesis identified braid eigenspaces with the wrong
tensor-product submodules. QYBE, braid and Hecke tests had not detected this.
The historical matrix is unchanged; coproduct-compatible R and braid
matrices and an intertwining residual were added and tested for all four
generators and on the full `V_2`/`V_0` sectors. The 9×9 `GL_q(2|1)` matrix
was compared with the original Çelik–Çelik article (all entries agree; the
page range was corrected to 259–269), and new tests compare all six
four-factor placements with an independent signed basis-action formula,
with an ordinary-swap negative control. Integer inputs now stay exact,
q-arithmetic is evaluated as Laurent polynomials, root-of-unity orders are
validated, and the counit check uses the public counit values. Tests now
check complete Clebsch–Gordan change-of-basis matrices for `(1,1)`, `(2,2)`
and `(3,2)`. Corrections to the archived thesis are in `../thesis/ERRATA.md`.

**Maintainability and validation (this revision).** Shared matrix helpers
moved to `quantum_group/linalg.py`, removing cross-module imports of private
functions (old names kept as aliases). Public functions reject invalid
arguments (non-integral or negative sizes and indices, mismatched or
non-square matrices, invalid tensor positions and parities, `q = 0`) with
tested errors. `python -m pytest` runs tests and doctests everywhere; CI
covers Python 3.10–3.13, the oldest supported dependencies, and a wheel
install running the README quickstart. The development-status classifier is
now Beta. Generated files were removed and the historical thesis material is
documented as such.

**Manuscript.** Restructured to JOSS's current sections: a non-specialist
Summary, a concrete Statement of need, an explicit build-versus-contribute
argument, design trade-offs, a research-impact statement limited to
demonstrated use, and an AI-usage disclosure based on the Git record. No new
mathematical result is claimed.
