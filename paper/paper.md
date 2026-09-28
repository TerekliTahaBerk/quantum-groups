---
title: 'quantum-group: Exact SymPy verification of explicit $U_q(\mathfrak{sl}_2)$ and $GL_q(2|1)$ matrix identities'
tags:
  - Python
  - SymPy
  - quantum groups
  - Yang-Baxter equation
  - Lie superalgebras
  - representation theory
authors:
  - name: Taha Berk Terekli
    orcid: 0009-0004-8266-1116
    affiliation: 1
affiliations:
  - name: Department of Mathematics, Yıldız Technical University, Istanbul, Türkiye
    index: 1
date: 27 September 2026
bibliography: paper.bib
---

# Summary

Many results in algebra and mathematical physics are stated as identities
between explicit matrices whose entries depend on a parameter. Checking such
an identity by hand means multiplying matrices with tens or hundreds of rows
while keeping track of conventions: which factor of a tensor product comes
first, and which signs appear when two objects are exchanged. A single slip
gives a result that looks plausible but is wrong. `quantum-group` is a small
Python package that builds these matrices exactly with SymPy
[@meurer2017sympy], forms the difference between the two sides of an
identity, and checks that every entry of this *residual* matrix simplifies to
zero, so that the calculation can be rerun, inspected and turned into a test.

The package covers two concrete examples from the theory of quantum groups:
deformations of classical symmetry algebras, depending on a parameter $q$,
that produce solutions of the Yang–Baxter equation used in statistical
mechanics and knot theory [@drinfeld1987; @jimbo1985; @jimbo1986; @kassel1995].
For $U_q(\mathfrak{sl}_2)$ it builds the finite-dimensional modules $V_n$,
checks the defining relations and generator-level Hopf identities on them,
computes tensor products and highest-weight vectors, and verifies the
fundamental R-matrix: the quantum Yang–Baxter equation (QYBE), braid and
Hecke relations, and compatibility with the package's coproduct. For the quantum supergroup $GL_q(2|1)$ of
@celik2021, in which one basis vector is odd so that exchanges acquire signs,
it constructs the published $9\times9$ R-matrix and verifies the graded
Yang–Baxter equation on three and four tensor factors.

# Statement of need

The intended users are researchers and students who read or write papers
containing explicit quantum-group matrices and need to confirm them: that a
transcribed R-matrix satisfies the Yang–Baxter equation, that it intertwines
a stated coproduct, that a claimed Clebsch–Gordan decomposition has the
stated highest-weight vectors, or that graded signs are placed correctly.
The workflow is a few lines in a Python session or notebook: build the
matrices, call a `*_residual` function to obtain the exact difference matrix,
inspect any nonzero entries, and keep the check as a pytest regression.

This needs neither GAP nor SageMath, nor translating a paper's conventions
into those of a general algebra engine: the package is pure Python with
three common dependencies, and every result is an ordinary `sympy.Matrix`.
On the author's own thesis, such a check exposed a convention error that
passing Yang–Baxter, braid and Hecke tests had not revealed (see Research
impact statement).

# State of the field

GAP's QuaGroup [@gap; @quagroup; @degraaf2001] and SageMath's
`QuantumGroup` interface to it [@sagemath] are far broader: they compute with
quantized enveloping algebras $U_q(\mathfrak{g})$ of semisimple Lie
algebras, including PBW-type bases, highest-weight modules, R-matrices and
crystal bases. SageMath also implements crystals for the quantum general
linear superalgebras of @bkk2000.

| Capability | quantum-group | QuaGroup / SageMath `QuantumGroup` |
|---|---|---|
| Algebras | $U_q(\mathfrak{sl}_2)$; one $GL_q(2|1)$ R-matrix | $U_q(\mathfrak{g})$, $\mathfrak{g}$ semisimple |
| R-matrices | $4\times4$ and $9\times9$ explicit matrices | general highest-weight modules |
| Graded YBE for the Çelik–Çelik matrix | implemented and tested | not in the documented interfaces |
| Output | exact residual matrices | algebraic computation results |
| Runtime | Python; SymPy, NetworkX, Matplotlib | GAP; SageMath for its interface |

: Comparison with the quantum-group interfaces of GAP and SageMath, not with
all of their functionality. \label{tab:comparison}

Why build rather than contribute? QuaGroup's documented scope is
$U_q(\mathfrak{g})$ for semisimple $\mathfrak{g}$. The $GL_q(2|1)$ example, a
quantum supergroup defined by an RTT presentation with a graded R-matrix
[@celik2021], lies outside that documented scope. For
$U_q(\mathfrak{sl}_2)$ the same identities can be computed in QuaGroup; the
aim here is instead to expose the explicit matrices and residuals, in the
basis order and coproduct of a given text, inside an ordinary SymPy
environment. `quantum-group` is thus a small verification layer
complementary to these systems, not a competing general quantum-group CAS;
for general $U_q(\mathfrak{g})$ computations they should be preferred.

# Software design

*Explicit matrices instead of an abstract algebra engine.* Every check runs
on concrete finite-dimensional representations; the noncommutative symbols
in `generators.py` only display relations, and no rewriting system is
implemented. Each statement stays directly comparable with printed matrices,
at the price that a vanishing residual verifies an identity on the given
representation only. Identities needing a noncommutative graded algebra,
such as the Gauss decomposition of @celik2021, are left out rather than
approximated with commuting symbols.

*Residuals are part of the API.* Functions such as `qybe_residual`,
`intertwining_residual_V1` and `graded_yang_baxter_residual_GLq21` return
the exact difference matrix, which shows *where* an identity fails:
replacing the super-permutation by an ordinary flip leaves exactly two
nonzero entries. Calculations use an exact nonzero symbol $q$, and Python
integers become exact SymPy numbers. Identities are rational in $q$ and hold
where denominators are defined; $q$-arithmetic uses Laurent-polynomial forms
so that removable singularities specialize correctly. A residual that SymPy
does not simplify to zero is not by itself a proof of inequality.

*Conventions are visible.* Basis orders are documented, parities are
explicit arguments, and the coproduct
$\Delta(E)=E\otimes1+K\otimes E$, $\Delta(F)=F\otimes K^{-1}+1\otimes F$ is
fixed and stated. For $GL_q(2|1)$, the parities are $(0,0,1)$ and the
super-permutation is $P_s(e_i\otimes e_j)=(-1)^{p(i)p(j)}e_j\otimes e_i$;
the matrix entries and $R_{13}=(P_s\otimes I)R_{23}(P_s\otimes I)$ follow
the display on page 261 of @celik2021.

*One sign rule for all placements.* An R-matrix acting on non-adjacent
factors of $V^{\otimes n}$ is built by conjugating the adjacent placement
with graded adjacent swaps, so the Koszul sign rule is encoded once, in
$P_s$, instead of being written out for every placement. The construction
is valid only for parity-preserving (even) operators, which the function
checks. Tests compare all six placements on $V^{\otimes4}$ with an
independent signed basis-action formula.

*Dense symbolic matrices, accepted cost.* Operators on $V^{\otimes n}$ are
stored as dense $3^n\times3^n$ SymPy matrices, which keeps every entry
printable but grows exponentially: in the recorded benchmark, building all
$R_{ij}$ on $V^{\otimes5}$ ($243\times243$) takes about 15 s. Sparse or tensor-network representations would
scale further but hide the matrices the package exists to show, and the
targeted calculations need at most four or five factors.

*Stable outputs under correction.* An audit found that the historical
upper-triangular `R_matrix_V1` intertwines the *opposite* of the package
coproduct. Changing its output would silently alter results already used in
the thesis, so it was kept and documented, and the coproduct-compatible
`R_matrix_V1_coproduct` ($R_{21}=PRP$) and `intertwining_residual_V1` were
added alongside it, with tests for both conventions.

The test suite, including doctests, is run by `python -m pytest` in GitHub
Actions on Python 3.10–3.13 and against the oldest supported dependency
versions. `MANUSCRIPT_CODE_MAPPING.md` links each computational claim to its
implementation and test.

*Scope and limitations.* Checks on finite matrices do not prove identities
in the abstract Hopf algebra or classify representations. Root-of-unity
examples do not construct the small quantum group, and the graph $B(n)$ is a
combinatorial crystal model, not a crystal-basis algorithm. The package does
not implement the RTT relations, Hopf superalgebra or Gauss decomposition
of @celik2021, a Markov trace, or the Jones polynomial.

# Research impact statement

Realized use is so far the author's own research. The package was developed for and used in the author's undergraduate thesis at Yıldız Technical University
[@terekli2026thesis], supervised by S. Çelik, a co-author of the
$GL_q(2|1)$ source paper. In the thesis, the package produced the table of
$q$-integers, the three matrix figures (regenerated by
`thesis/figures/generate_figures.py`), the Clebsch–Gordan highest-weight
vectors for $V_1\otimes V_1$, $V_2\otimes V_2$ and $V_3\otimes V_2$, the
comparison of $V_2$ in the classical, generic and root-of-unity regimes, and
the verification of the graded Yang–Baxter residual (all 729 entries), the
six four-factor placements, the four local Yang–Baxter triples and the
commutation of $R_{12}$ with $R_{34}$.

After the undergraduate thesis was submitted in June 2026, the package was
used to audit the thesis itself
(`AUDIT.md`). An explicit intertwining residual, now exposed as
`intertwining_residual_V1`, showed that the thesis's R-matrix
intertwines the opposite of the coproduct used in the text, so the thesis
identified braid eigenspaces with the wrong tensor-product submodules. This
and other corrections are recorded in `thesis/ERRATA.md`, and the tests now
check complete Clebsch–Gordan change-of-basis matrices for the three
examples above. This is the class of error the package is meant to catch,
found in a real calculation. We claim no new mathematical results
and are not aware of external users; reuse is supported by pip packaging,
continuous integration, recorded benchmarks and the claim-to-test mapping.

# AI usage disclosure

Generative AI was used in the publication-preparation phase that began in
September 2026. Claude Code (Anthropic) assisted with packaging and
continuous integration, the benchmark script, README and contributor
documentation, the changelog, the first draft of this paper, bibliography
checks, the renaming of the Hecke check with a deprecation alias, translating
Turkish docstrings, comments and documentation into English, a mathematical
and technical audit (source comparison, symbolic calculations, corrections
to parameter handling and asymptotics, the coproduct-compatible R-matrix
APIs, regression tests), the shared matrix-helper refactoring, input
validation and its tests, repository cleanup, and revision of this paper,
`AUDIT.md`, `thesis/ERRATA.md` and the status documents. No other AI tool
was used at any stage; an earlier revision of this disclosure and of
`AUDIT.md` incorrectly attributed part of this work to a separate tool
("Codex"), which was never in fact used, and that attribution has been
corrected. Commits produced with Claude Code are authored or co-authored by
"Claude" in the Git history, with the model recorded in their
`Co-Authored-By` trailers where present.

AI-assisted code is covered by the automated tests, and AI-assisted
mathematical statements were checked with executable symbolic tests and
against the primary sources recorded in `AUDIT.md`, including the original
Çelik–Çelik article. The author reviewed, edited and validated all
AI-assisted outputs, made the core scientific and design decisions, and is
responsible for the software, the mathematical claims and this disclosure.

# Acknowledgements

The author thanks Prof. Dr. Salih Çelik for supervising the thesis from which
this package originated. This work received no specific funding.

# References
