---
title: 'quantum-group: A lightweight SymPy package for verifying $U_q(\mathfrak{sl}_2)$ and $GL_q(2|1)$ structures'
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

Quantum groups are deformations of Lie groups and Lie algebras that depend on
a parameter $q$ and recover the classical objects as $q \to 1$. They were
introduced by Drinfeld and Jimbo [@drinfeld1987; @jimbo1985] and are closely
tied to the quantum Yang-Baxter equation (QYBE), braid group representations
and knot invariants. The simplest example is $U_q(\mathfrak{sl}_2)$. Quantum
*super*groups such as $GL_q(2|1)$ extend these ideas to $\mathbb{Z}_2$-graded
spaces. There, the Yang-Baxter equation carries parity-dependent signs
[@celik2021].

`quantum-group` is a Python package, built on SymPy [@meurer2017sympy], that
turns the defining identities of these structures into explicit, symbolic
matrix computations. For $U_q(\mathfrak{sl}_2)$ it constructs the
finite-dimensional representations $V_n$ and checks the defining relations,
the Hopf algebra axioms and tensor product decompositions. It also verifies
the R-matrix on $V_1 \otimes V_1$ against the QYBE, the braid relation and the
Hecke relation. For $GL_q(2|1)$ it builds the $9 \times 9$ R-matrix of
@celik2021 and the graded super-permutation, and verifies the graded
Yang-Baxter equation on $V^{\otimes 3}$ and all $R_{ij}$ placements on
$V^{\otimes 4}$.

# Statement of need

The package targets researchers and students in computational representation
theory who want to check concrete identities in quantum groups quickly and
reproducibly, in particular for $\mathbb{Z}_2$-graded (super) structures. It
is also meant for readers of papers on quantum supergroups who want to
reproduce R-matrix computations without installing a full computer algebra
system.

| | quantum-group | GAP QuaGroup | SageMath `QuantumGroup` |
|---|---|---|---|
| Scope | $U_q(\mathfrak{sl}_2)$; $GL_q(2\|1)$ example | $U_q(\mathfrak{g})$, $\mathfrak{g}$ semisimple | as QuaGroup (interface) |
| R-matrices | yes (4×4, 9×9) | yes | yes (via QuaGroup) |
| Graded (super) YBE | yes, $GL_q(2\|1)$ | not found | not found |
| Parameter $q$ | SymPy symbol | indeterminate | generic or specialized |
| Installation | `pip`; SymPy | GAP | SageMath + optional package |

: Comparison with existing software. "Not found" means absent from the
sources we inspected (see State of the field). \label{tab:comparison}

# State of the field

The established tools for quantized enveloping algebras are the GAP
[@gap] package QuaGroup [@quagroup; @degraaf2001] and SageMath's
`QuantumGroup` class [@sagemath], which is an interface to QuaGroup. Both are
far more general than `quantum-group`. They handle $U_q(\mathfrak{g})$ for
every finite-dimensional semisimple Lie algebra $\mathfrak{g}$ and provide
R-matrices, crystal and canonical bases, and the Hopf structure. SageMath
also implements the crystals of @bkk2000 for the general linear Lie
superalgebra $\mathfrak{gl}(m|n)$.

We inspected the source code and manual of QuaGroup (version 1.8.4, commit
`72751e5`) and SageMath's `quantum_groups` and `crystals` modules (commit
`3801b3c`). We found no quantum supergroup, graded R-matrix or graded
Yang-Baxter functionality in either. This statement reflects only those
sources.

We therefore wrote a separate package rather than contributing to these
systems, for two reasons. First, the graded structure is the central object
here. Parity-dependent super-permutations and sign conventions do not fit
the data models of QuaGroup or Sage's quantum group module, which are
organised around semisimple root systems. Second, we wanted a small reference
implementation that needs only `pip install` and pure Python, so that its
matrices can be read and checked in a few lines of SymPy. `quantum-group`
does not aim to replace QuaGroup or SageMath, and it covers far less of the
theory.

# Software design

Every identity is checked with the same *zero-residual* pattern. The package
builds both sides as exact SymPy matrices, forms their difference and
simplifies each entry. The identity holds if and only if every entry
simplifies to zero. Functions come in pairs: `*_residual` returns the residual
matrix for inspection, and `*_holds` or `*_check` returns a Boolean. Nothing
is evaluated in floating point.

The modules follow the mathematics. `generators` and `representations`
construct $E$, $F$, $K$, $K^{-1}$ on $V_n$. `relations` checks the defining
relations. `hopf` provides the coproduct, counit and antipode. `tensor`
handles tensor products and Clebsch-Gordan decompositions, and `r_matrix`
covers the R-matrix, the QYBE, the braid relation and the Hecke relation.
`supergroup_gl21` builds the graded R-matrix and the super-permutation and
embeds $R_{ij}$ into $V^{\otimes n}$ by conjugating with graded adjacent
swaps. Smaller modules cover classical and root-of-unity limits, the
combinatorial crystal graph $B(n)$ and plotting.

The $U_q(\mathfrak{sl}_2)$ R-matrix is the image of the universal R-matrix on
$V_1 \otimes V_1$, rescaled by $q^{1/2}$ [@drinfeld1987; @jimbo1986;
@kassel1995]. Its docstring records the coproduct convention and how it
relates to the coproduct used in the package.

The test suite has 126 `pytest` cases and runs on GitHub Actions for Python
3.10, 3.11 and 3.12. `MANUSCRIPT_CODE_MAPPING.md` maps each mathematical
claim to its implementing function and its test. A benchmark script records
running times. On a 2.1 GHz Xeon, every check on $V^{\otimes 4}$
($81 \times 81$ matrices) finishes in under 2 s. On $V^{\otimes 5}$
($243 \times 243$) one graded Yang-Baxter check takes about 15 s, most of it
spent building the embeddings.

# Research impact statement

`quantum-group` was developed as the verification infrastructure for an
undergraduate thesis at Yıldız Technical University on modelling quantum
group structures in Python. Its main research use is independent,
reproducible computational verification. It checks that the $9 \times 9$
R-matrix of the quantum supergroup $GL_q(2|1)$ given by @celik2021 satisfies
the graded Yang-Baxter equation, with all $27 \times 27$ residual entries
simplifying symbolically to zero. It also checks far commutativity and every
local Yang-Baxter triple on $V^{\otimes 4}$. The package does not claim new
mathematical results, and it does not verify the Gauss decomposition or the
Hopf superalgebra structure of @celik2021. Its contribution is to make these
computations explicit, executable and continuously tested, so that others can
reuse them for related R-matrices.

<!-- TODO (author): JOSS requires an "AI usage disclosure" section; complete before submission. -->

# Acknowledgements

The author thanks Prof. Dr. Salih Çelik for supervising the thesis from which
this package originated.

# References
