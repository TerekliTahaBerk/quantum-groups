# Cover letter (for the *Comments for the Editor* field)

> **Status: not yet pasteable — one thing left.** All fields are filled
> except the PyPI identifier, which needs `quantum-group==1.1.0` to be
> published (`DISTRIBUTION.md` step C). Re-check the venue declaration on
> the day of submission (the paragraph marked below). If an equivalent JOSS
> submission exists at that moment, do not submit to JORS until that
> process has ended or been withdrawn.

---

Dear Editor,

I submit the manuscript **"quantum-group: Exact SymPy Verification of
Explicit U_q(sl_2) and GL_q(2|1) Matrix Identities"** for consideration as
a **Software Metapaper** in the *Journal of Open Research Software*.

**Software and purpose.** `quantum-group` is a Python package for verifying
explicit matrix identities from the theory of quantum groups: the defining
relations and Hopf identities of U_q(sl_2) on finite-dimensional modules,
tensor products and Clebsch–Gordan vectors, the Yang–Baxter, braid, Hecke and
coproduct-intertwining identities of the fundamental R-matrix, and the
graded Yang–Baxter equation for the GL_q(2|1) R-matrix of Çelik and Çelik
(Rep. Math. Phys. 88, 2021). Every identity is returned as an exact SymPy
residual matrix, so a failed check shows which entries, and hence which
convention, disagree.

**Research-software contribution.** Published quantum-group matrices are
easy to misuse because results depend on basis order, tensor placement, the
coproduct and graded sign rules, and several such errors pass the usual
Yang–Baxter test. The package fixes these conventions in documented
functions, keeps both a historical and a coproduct-compatible R-matrix API
for reproducibility, encodes the Koszul sign rule once for all tensor
placements, and is backed by 198 automated tests and 4 doctests, including
negative controls that require known wrong conventions to fail. It exposed a
real convention error in my own undergraduate thesis. The manuscript claims
no new mathematical results; the contribution is the software and its
verification method.

**Relation to existing software.** GAP's QuaGroup and SageMath are far
broader systems for quantized enveloping algebras of semisimple Lie
algebras. `quantum-group` does not replace them: it is a small, inspectable
verification layer for concrete matrix calculations in a given text's
conventions, including a graded example outside QuaGroup's documented scope.

**Availability of the exact version described.**
- Licence: MIT. Repository: https://github.com/TerekliTahaBerk/quantum-groups
- Version 1.1.0 = commit **103d5384e70e8b0b746b296a0bdbd2d156ba8dde**,
  tagged as GitHub Release `v1.1.0`.
- Installation: `python -m pip install quantum-group==1.1.0` (PyPI).
- Archive: Zenodo, DOI **10.5281/zenodo.23015576**, a `git archive` of that
  commit. The earlier DOI 10.5281/zenodo.22997681 archives version 1.0.0
  only.
- Quality control: continuous integration on Python 3.10–3.13, the oldest
  supported dependency versions, wheel installation, and Linux, macOS and
  Windows. The paper's example (Listing 1) and its expected output are in
  the repository and are compared automatically in CI.

**Reuse potential.** The residual and graded-embedding functions accept
arbitrary SymPy matrices and parity lists, so researchers can check R-matrix
transcriptions, determine which coproduct an R-matrix intertwines, turn
literature identities into regression tests, and apply the graded placement
machinery to other super vector spaces. The paper states where extensions
would require substantial new software.

**Prior publication and related manuscripts.** This manuscript has not been
published elsewhere and is not under consideration by any other journal.
For transparency: (i) the software was developed for and used in my
undergraduate thesis at Yıldız Technical University (June 2026, in
Turkish), which the manuscript cites; (ii) the public repository also
contains a separate draft software paper prepared for the *Journal of Open
Source Software* (`paper/paper.md`). That draft has not been submitted to
JOSS or elsewhere, and it will not be submitted while this manuscript is
under consideration at JORS (author's confirmation, 27 September 2026). The
two texts concern the same software but
were written separately; the JORS manuscript is organized around
architecture, quality control, availability and reuse.
**[Re-confirm both statements on the day of submission.]**

**Competing interests.** The author has no competing interests to declare.

**Funding.** This work received no specific funding.

**Use of generative AI.** As required by the Ubiquity Press policy, the
manuscript contains a section describing the use of generative AI. No AI
tools were used during the original development and thesis work
(April–June 2026). In September 2026 Claude Code (Anthropic; Claude Opus
5.5) was used in preparing this software version, its tests and
documentation — including translating Turkish docstrings and comments into
English and a mathematical and technical audit that led to the
parameter-handling corrections, the coproduct-compatible R-matrix functions
and the audit regression tests — and in drafting the manuscript and
submission materials. No other AI tool was used. The tools are not authors.
I reviewed and validated all AI-assisted output and take responsibility for
the software and the manuscript.

**Suggested reviewers.** None has collaborated with me or on this software,
and I have no personal or professional relationship with any of them.

1. Anne Schilling, University of California, Davis — anne@math.ucdavis.edu
2. Nicolas M. Thiéry, Université Paris-Saclay — Nicolas.Thiery@universite-paris-saclay.fr
3. Max Horn, RPTU Kaiserslautern-Landau — mhorn@rptu.de
4. Vidas Regelskis, University of Hertfordshire — v.regelskis@herts.ac.uk
5. Paul Zinn-Justin, University of Melbourne — pzinn@unimelb.edu.au

**Article processing charge.** I request a full waiver of the £824.00
Software Metapaper APC. This software was developed as part of my
undergraduate thesis and has received no specific funding (see Funding,
above); I have no institutional or grant funding available to cover the
charge.

Thank you for considering this submission.

Yours sincerely,

Taha Berk Terekli
Department of Mathematics, Yıldız Technical University, Istanbul, Türkiye
ORCID: 0009-0004-8266-1116
terekli@tahaberk.com
