# Change summary for the current review

Prepared 27 September 2026. Draft for the author; not sent to the editor.

The revision corrects the relationship between the fundamental R-matrix and
the coproduct used by the software. The historical upper-triangular matrix
remains available, while explicit coproduct-compatible R and braid APIs now
have generator-intertwining and eigenspace tests. This matters because QYBE
and Hecke tests alone did not detect the convention mismatch.

The original Çelik–Çelik article was checked directly. Its 9×9 R-matrix and
grading agree with the implementation; the bibliographic page range has been
corrected from 259–272 to 259–269. New independent component tests cover all
six four-factor embeddings and all three disjoint-pair commutators. A negative
control demonstrates the nonzero residual produced by an ordinary flip.

The tests now verify full Clebsch–Gordan change-of-basis matrices for the
three manuscript examples, rather than only counting highest-weight vectors.
Integer inputs preserve exact arithmetic, q-arithmetic avoids removable
singularities, root-of-unity orders are validated, and the asymptotics helper
returns the documented leading term. Counit verification now consumes the
public counit values.

The English manuscript states precisely what is checked at representation
level and retains its software-verification framing. It makes no new
mathematical claim. Jones/Markov-trace and noncommutative Gauss extensions
were evaluated but did not meet the requested novelty/scope threshold.
The AI disclosure now includes the audit-assisted implementation, regression
tests and manuscript revisions. Corrections to archived thesis proofs and
conventions are documented separately in `thesis/ERRATA.md`.

Validation: 158 pytest cases and three doctests, with local environment and
rendering status recorded in `PREFLIGHT.md`. These changes are uncommitted;
remote CI, official journal typesetting and an updated release archive are
subsequent publication steps, not outcomes claimed by this note.
