# Cover letter (for the *Comments for the Editor* field)

> **Status: not yet pasteable.** Fill the `[bracketed]` fields from the
> author's confirmed declarations and the completed distribution steps
> (`DISTRIBUTION.md`), and re-check the venue declaration on the day of
> submission. If an equivalent JOSS submission exists at that moment, do not
> submit to JORS until that process has ended or been withdrawn.

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
- Version 1.1.0 = commit **[snapshot SHA]**. There is no GitHub Release for
  1.1.0; the version is identified by this commit.
- Installation: `python -m pip install quantum-group==1.1.0` (PyPI).
- Archive: Zenodo, DOI **[1.1.0 DOI]**, a `git archive` of that commit. The
  earlier DOI 10.5281/zenodo.22997681 archives version 1.0.0 only.
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
under consideration at JORS. The two texts concern the same software but
were written separately; the JORS manuscript is organized around
architecture, quality control, availability and reuse.
**[Re-confirm both statements on the day of submission.]**

**Competing interests.** [confirmed statement]

**Funding.** [confirmed statement]

**Use of generative AI.** As required by the Ubiquity Press policy, the
manuscript contains a section describing the use of Claude Code (Anthropic;
[model]) and Codex (OpenAI; [model]) in preparing the software version, its
tests and documentation, and in drafting the manuscript and submission
materials. The tools are not authors. [Confirmation of human review and
validation, in the author's words.]

**Suggested reviewers.** [Five names and e-mail addresses from
`POTENTIAL_REVIEWERS.md`, each copied from the official page.] None has
collaborated with me or on this software. [Confirm.]

**Article processing charge.** [One of: "The APC will be paid on
acceptance." / "I request a waiver/discount because …" / "The APC will be
covered by …".]

Thank you for considering this submission.

Yours sincerely,

Taha Berk Terekli
[Current affiliation]
ORCID: 0009-0004-8266-1116
terekli@tahaberk.com
