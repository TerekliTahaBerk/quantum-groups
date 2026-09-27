# Mathematical and technical audit

Date: 27 September 2026. Audited revision: `dbe56afbb831a0734c964227e2c46209fca05848`.

**Updated status (27 September 2026): the author supplied the original
Çelik–Çelik PDF and authorized corrections.** Its matrix and grading have
now been compared directly; the source-specific gap is closed (§11).
The substantive mathematical findings below describe the **baseline revision**.
Corrections and the current regression suite are listed in §12. Historical
line references and failure reproductions are retained so the audit remains
reviewable. They must not be read as current unfixed defects.

Jimbo's originals remain available only as previews and Kassel only as a
chapter VI excerpt. No claim is made to have read their inaccessible parts.
The revised manuscript attributes the exact R normalization to the directly
inspected Drinfeld formula and the GL matrix to the supplied original.
The retained computational claims are checked independently below; an
exhaustive page-by-page audit of all cited books is not claimed.

**Repository status (updated 27 September 2026).** The corrections in §12
were committed to `main` as `bc5c370`, after the `v1.0.0` tag, and GitHub
Actions passed on that commit. They are therefore *not* contained in the
v1.0.0 release or its Zenodo archive; they are part of the unreleased 1.1.0
(`CHANGELOG.md`). The current verification record is `paper/PREFLIGHT.md`.
No JOSS submission or message to an editor has been made. Archived thesis
files are accompanied by `thesis/ERRATA.md`. Part 2's bounded feasibility assessment follows the
completed GL comparison in §13 and identifies no defensible new mathematical
result to implement within this scope.

## 1. Principal findings at the baseline revision

1. **The thesis incorrectly identifies the eigenspaces of `R_check_V1()` with the submodules computed using the package coproduct.** The returned unbraided matrix uses the opposite convention. The docstring acknowledges this correctly, but the thesis and spectral docstring still make an incompatible identification. An explicit nonzero residual appears below. The existing QYBE, braid, Hecke and eigenvalue tests all pass despite this error.
2. **The representation proof uses the wrong basis normalization.** Thesis line 791 divides by `[k]_q!`, whereas the theorem and code use `v_k=F^k v_0`. Its irreducibility argument also omits a necessary nonvanishing/connectivity step, and its classification argument assumes rather than establishes highest-weight existence.
3. **The universal-image normalization is correct.** Independent evaluation of Drinfeld's original formula gives `q^(-1/2) R_matrix_V1()`. Multiplication by `q^(1/2)` removes the half powers without a sign error. This scalar does not repair the coproduct mismatch.
4. **The implemented graded matrix satisfies the claimed identities.** Its 27×27 YBE residual is identically zero; both product matrices have 58 generically nonzero entries. All six four-factor embeddings match an independent component construction; all four local triples and all three disjoint pair commutators vanish. This does not certify that the matrix was transcribed correctly from Çelik–Çelik.
5. **Generic symbolic calculations really are exact.** Passing an ordinary Python integer `2` nevertheless produces floating-point entries through negative integer powers. The baseline paper already discloses this boundary and the incompleteness of `simplify`; these are not new prose errors in the audited revision. The authorized fix now makes integer inputs exact as well.
6. **Several scope and attribution claims need tightening:** the suite checks generator-level Hopf identities, not an abstract Hopf algebra; CG tests check highest-weight vectors, not complete change-of-basis decompositions; general embeddings require an even operator; root-of-unity descriptions need domain/integral-form qualifications. A CG explanatory binomial ratio is wrong, although the actual vector is correct.

The published-page range also needs verification/correction: the authors' institutional publication record and a later paper by Çelik give **259–269**, whereas the repository bibliography and thesis give **259–272**.

## 2. Evidence standard and sources actually inspected

“Confirmed” below concerns the precise assertion and evidence stated in its row. It does not mean all cited sources were read. “Gap found” includes missing proof or missing evidence; it is not automatically a counterexample. All matrix indices in computations are zero-based unless explicitly stated otherwise.

### Literature access ledger

| Source | Material actually inspected | What it supports; limitations |
| --- | --- | --- |
| [Drinfeld, *Quantum Groups*, ICM proceedings](https://ncatlab.org/nlab/files/Drinfeld-QuantumGroups.pdf) | Full article available; relevant text in §§6, 10, 13; visually inspected printed pp. 807, 816–817. | Symmetric coproduct, universal series, fundamental vector matrix, and quasitriangular intertwining convention. Evaluation below is an independent computation. The proceedings year is 1987, although the congress was in 1986. |
| [Jimbo 1985 publisher record](https://link.springer.com/article/10.1007/BF00704588) | Abstract and bibliographic metadata; PDF request redirects to subscription preview. | Confirms topic and reference, **not** an equation-by-equation convention comparison. |
| [Jimbo 1986 publisher record](https://link.springer.com/article/10.1007/BF00400222) | Abstract and bibliographic metadata; PDF request redirects to subscription preview. | Same limitation. The claim that the returned matrix is exactly a particular Jimbo normalization remains unverified against that original article. |
| [Kassel, chapter VI excerpt, pp. 121–130](https://storage.lpetrov.cc/courses/integrable_seminar/kassel%20Uq.pdf) | Definitions VI.1.1; root-order convention VI.1; specialization discussion VI.2; representation theorem VI.3.5 and formulas (3.1)–(3.3), pp. 128–129 visually inspected. | Confirms defining relations and distinction between divided and undivided bases. Chapters VII–IX containing additional Hopf/R material were not obtained. |
| [Kassel book record](https://link.springer.com/book/10.1007/978-1-4612-0783-2) | Publisher contents and metadata. | Identifies relevant chapters; not a substitute for their text. |
| [Çelik–Çelik institutional record](https://avesis.yildiz.edu.tr/yayin/fd7f0551-9e39-48d9-b095-bf6103a48bc1/a-new-quantum-supergroup-and-its-gauss-decomposition) | Title, authors, abstract, DOI, pp. 259–269. | No article text. Its arXiv link resolves to the unrelated `astro-ph/0106320`; that link cannot be used as evidence. |
| [Çelik–Çelik publisher page](https://www.sciencedirect.com/science/article/pii/S0034487721000732) | HTTP 403, both browser-fetch service and direct public HTTP retrieval. DOI resolver also failed. | **No equations inspected.** Searches of title/DOI and author records did not locate a usable copy. A local PDF or accessible full-text URL was requested from the author. |
| [Çelik, *Cartan calculus on the superalgebra*, references](https://hrcak.srce.hr/en/file/446016) | Reference [8] in this later paper. | Independently lists 259–269; not evidence for the 2021 matrix entries. |
| [QuaGroup manual, introduction](https://gap-packages.github.io/quagroup/doc/chap1.html) and [Sage QuaGroup interface documentation](https://doc.sagemath.org/html/en/reference/algebras/sage/algebras/quantum_groups/quantum_group_gap.html) | Published software documentation. | Supports broad comparison scope and interface relationship. Does not reproduce the manuscript's exact historical-commit search or prove absence of every super-related feature. |

No inference from a title, abstract, citation, or passing YBE test is used to claim that the inaccessible Çelik–Çelik article has been checked.

### Computational record

Environment: Python 3.12.10, SymPy 1.14.0. Command:

```sh
MPLCONFIGDIR=/tmp/quantum-audit-mpl python3 -m pytest tests/ -q
```

Result: **126 passed in 20.47 seconds**. This is a local run, not an independent rerun of all three CI environments. The workflow configures Python 3.10, 3.11, 3.12.

Additional audit calculations used exact rational-function cancellation (`sympy.cancel`) to check matrix entries, alongside the suite's simplification checks. They included both coproduct conventions, full CG descendant bases, an independent signed basis-action embedding, all four-factor triples, and deliberately incorrect ordinary-swap embeddings. Reproduction code is in §10. No random or floating-point sample was used as proof of a generic identity.

## 3. Claim-by-claim ledger

`T:L` denotes line L of `thesis/thesis_ytu.tex`; `P:L` denotes line L of `paper/paper.md`, at the audited revision. Repeated assertions in abstracts and conclusions are grouped with the detailed claim they repeat. Theorem numbers follow the shared theorem/definition counter and chapter numbers in the source.

| Claim and location | Verification status | Evidence | Fix needed |
| --- | --- | --- | --- |
| Quantum groups and the classical limit; T:484–498, 677–690; P:23–30 | confirmed with caveat | Drinfeld §§1,6 describes algebraic quantization; matrix limits in §8 hold. Specialization of `Q(q)` itself at `q=1` is not defined. | Say deformation of coordinate/enveloping algebras; distinguish representation limits from specializing the abstract algebra. |
| Groups, Lie groups, enveloping algebra; definitions 2.1–2.3, T:563–599 | confirmed with caveat | Standard defining axioms and `T(g)/(xy-yx-[x,y])`; these are background, not program outputs. | In definition 2.2 explicitly assume characteristic zero, as throughout the applications, or require alternating brackets in characteristic two. Antisymmetry alone is insufficient in characteristic two. |
| `sl_2` matrices and brackets, T:602–615 | confirmed | Direct multiplication gives `[h,e]=2e`, `[h,f]=-2f`, `[e,f]=h`. | None. |
| Classical finite-dimensional classification and formulas, theorem 2.4, T:617–629 | confirmed with caveat | Undivided basis formula follows from `[e,f^k]v_0=k(n-k+1)f^{k-1}v_0`; highest-weight reasoning is given in §5. | It is a quoted classical theorem, not a classification computed by this package. Add a precise classical reference rather than implying test coverage of classification. |
| Hopf definition and representation interpretation, definition 2.5 and example 2.6, T:643–673 | confirmed with caveat | Generator formulas on `U(g)` extend multiplicatively/antimultiplicatively and satisfy the identities. | Counit is an algebra map on the abstract algebra, not a map on arbitrary representation matrices; retain labelled terms. |
| `U_q(sl_2)` defining relations over `Q(q)`, definition 3.1, T:686–701 | confirmed | Kassel VI.1.1; §5 verifies the representation identities for arbitrary n. | No algebraic correction; preserve the `q≠0`, generic/specialized distinctions. |
| Coproduct, counit, antipode, T:704–712; `hopf.py:48–82` | confirmed | Algebraic verification in §6 and generator residual tests. | None in these formulas. |
| “Nine Hopf axioms,” T:511–513, 1664–1665 | error found | API returns 3 families × 4 generators = 12 Boolean records, grouping 20 equalities (4 coassociativity + 8 counit + 8 antipode). | Replace count by “three families of generator identities”; do not equate them with an exhaustive abstract Hopf verification. |
| `q`-integer Laurent formula and classical limit, T:716–770 | confirmed with caveat | Finite geometric sum for n>0; termwise limit gives n. Table n=0…5 is correct. | State positive n for the displayed finite sum; extend via `[0]=0`, `[-n]=-[n]`. Specialize a Laurent form at removable singularities. |
| `q_factorial`, `q_binomial` and their limits, mapping rows 1–3 | confirmed with caveat | Generic finite products/quotients; suite tests representative classical limits. | Direct evaluation at roots can divide 0 by 0: see §8. |
| Matrices of `V_n`, theorem 4.1, T:774–783; `representations.py` | confirmed | Arbitrary-n verification in §5, exact code, and symbolic tests n=0…5. | Add “generic q/type 1” to unconditional “irreducible” API prose. |
| Proof basis `v_k=F^k v_0/[k]!`, T:789–793 | error found | That basis gives `Fv_k=[k+1]v_{k+1}`, `Ev_k=[n-k+1]v_{k-1}`, not the theorem. | Remove `/[k]!` in this proof, or change all action formulas and code consistently; first option is minimal. |
| Irreducibility follows from one-dimensional weight spaces, T:793–795 | gap found | Multiplicity-free weights alone do not imply simplicity. Nonzero E/F connections are essential. | Add the weight-projection and nonvanishing argument in §5. |
| Classification of all type-1 simples, theorem 4.1 proof | gap found | The proof assumes a highest weight `q^n` and does not derive its existence/allowed values, termination, or uniqueness. Kassel VI.3.5 supplies these missing steps. | Cite a precise theorem or supply those steps; finite n tests cannot fill this gap. |
| Crystal path `B(n)`, weights and partial maps; T:881–899, 1700–1710 | confirmed with caveat | Graph has n+1 vertices, n arrows, weights n−2k. | Graph is a model of the known crystal, not a computed crystal lattice or literal entrywise limit of E/F; see §8. |
| All identities are exact symbolic zero residuals; T:901–922; P:94–99 | confirmed with caveat | Default calculations contain no `Float`; generic checks are not replaced by numerical substitutions. | Limit “every identity” to implemented identities and documented exact inputs. |
| Zero-residual decision caveat; paper Software design | confirmed with caveat | The baseline paper already notes that simplify is not a decision procedure. For rational functions, numerator reduction supplies the precise criterion. | Retain the caveat and specify the rational-function domain. |
| Residual/Boolean API coverage; paper Software design | confirmed with caveat | The baseline paper already lists Hopf, Hecke and local-YBE exceptions. Defining-relation results are structured records, not separate function pairs. | Describe structured results and actual function pairs separately. |
| Native-integer exactness boundary; paper Software design, representation/R APIs | confirmed with caveat | The baseline paper discloses that native integers can produce Floats; the behavior is reproduced below. | Improve the API by sympifying parameters before exponentiation; update the disclosure after verification. |
| Defining-relation tests on `V_0…V_4`, T:960–965 | confirmed | Actual symbolic parametrization also includes n=5. R1 checks one side; in square matrices a right inverse is also a left inverse. | No false result; may update the stated range. |
| Thesis relation-check listing matches API, T:967–984 | error found | Listing uses `E,F,K,K_inv` keyword names and returns bools; API uses `E_mat,…` and returns `RelationCheck` instances. | Label as pseudocode or synchronize interface/return-value explanation. |
| Tensor action induced by coproduct, T:1009–1020; `tensor.py:45–66` | confirmed | Formula matches `hopf.py`; generator relations pass on listed pairs; §6 proves compatibility. | Require a common deformation parameter for both factors. |
| Generic CG formula for all m,n, T:995–1007; mapping CG rows; P:36,103 | confirmed with caveat | Highest-weight recurrence and generic proof in §5; code starts from a hard-coded list of expected summands. | Do not describe listing summands or testing highest weights alone as a computed proof of the full decomposition. |
| Three displayed CG decompositions and vectors, T:1027–1061 | confirmed | Reproduced entries; full descendant change-of-basis matrices invertible over `Q(q)`; all four generator intertwiners zero, §5. | None in the vectors. Existing suite lacks the stronger full-basis check performed in this audit. |
| Classical ratio is of type `binom(3,1)/binom(2,0)`, T:1062 | error found | That quotient is 3, not 3/2. Direct classical kernel gives `2c_1+3c_2=0`. | Replace with `-3/2` or `-binom(3,1)/binom(2,1)`. |
| Highest-weight verification, T:1066–1076 | confirmed with caveat | E-annihilation and K-weight are checked, but E-annihilation test omits pair (3,2); count and K tests include it. Audit verified it independently. | Add (3,2) to E-annihilation regression coverage if retaining “each example tested” wording. |
| Displayed R is the unscaled universal image for this coproduct; T:1081–1098 and figure 8.1 | error found | §4: actual universal image is `q^(-1/2)R`; it intertwines the opposite convention. | Explicitly state both rescaling and opposite coproduct, or use `R21` consistently with package tensors. |
| Paper's rescaled universal-image statement and convention note, P:110–113; `r_matrix.py:53–82` | confirmed with caveat | Independent Drinfeld-series evaluation and intertwining calculations, §4. | Specify the coproduct in the paper itself; direct Jimbo convention comparison remains pending. Scalar rescaling preserves local identities, not automatically universal hexagon axioms. |
| QYBE, theorem 8.1, T:1163–1190 | confirmed | Exact 8×8 residual zero; source equation and code use the same leg order. | None; this does not establish intertwining. |
| Braid relation, proposition 8.2, T:1193–1207 | confirmed | Exact residual for `P R` zero. Invertibility and far commutation extend to arbitrary strand count, §7. | Distinguish a braid representation on tensor vector spaces from a module-compatible braiding for the package coproduct. |
| Hecke identity, proposition 8.3, T:1211–1223 | confirmed | Direct inverse or quadratic 2×2-block computation, §7. | Thesis points to deprecated-name test; prefer `test_hecke_skein`. |
| Eigenvalues q (3), −q⁻¹ (1), proposition 8.4, T:1227–1233 | confirmed with caveat | Characteristic polynomial `(λ-q)^3(λ+q⁻¹)` over `Q(q)`. | Spectral splitting is generic; q=±i merges eigenvalues and is nonsemisimple. |
| Eigenspaces equal package `V_2,V_0`, T:1235–1239, 1255–1257; `r_matrix.py:182–184` | error found | Singlet residual `(P R+q⁻¹I)(0,-q⁻¹,1,0)^T ≠ 0`, §4. | Use `P R21=R P` for package coproduct, or explicitly transport all modules to the opposite coproduct. |
| Eigenvalues describe “radiationless passage”/“sign-changing half-turn,” T:1238–1239 | gap found | No physical model or mathematical definition ties those phrases to this generic formal parameter. | Remove unsupported interpretation or supply a precise model and source. |
| Hecke braid representation yields Jones via “a Markov trace,” T:1263–1270 | confirmed with caveat | Braid/Hecke relations alone do not specify trace parameter, quantum trace, writhe correction, or unknot normalization. | Say an appropriately normalized sl₂ Markov/quantum trace yields Jones; no polynomial is computed here. |
| GL matrix equals Çelik–Çelik p.261; T:1281–1310; P:38–40,128–130; source docstrings | gap found | Repository and thesis entries agree, but original paper unavailable. | Obtain actual paper, compare every entry and all convention translations; do not certify attribution from YBE alone. |
| GL parity, basis, super-permutation, T:1293–1296,1326–1364 | confirmed with caveat | Standard Koszul action; involution, basis order, and lone odd–odd minus sign checked. | Internal correctness confirmed; original paper's tensor-component convention remains pending. |
| GL R12/R23/R13 placements, T:1397–1410 | confirmed with caveat | R is even; direct signed action matches both conjugation constructions, §7. | Add evenness hypothesis and distinguish ordinary operator entries from coefficients of graded matrix-unit tensors. |
| General-n embedding proposition 9.1, T:1460–1473 | gap found | Correct for even R. No proof appears after the proposition; code/small-n comparisons are not an all-n proof. | Add hypotheses and the basis-vector proof in §7. |
| GL 27×27 symbolic zero residual, T:1499–1539; P:129–131 | confirmed | All entries cancel exactly; wrong ordinary swap produces explicit nonzero entries. | Keep attribution status separate. |
| Both YBE products have 58 nonzero entries, T:1524–1529 | confirmed with caveat | Count independently reproduced as a generic polynomial count. | “Generically nonzero”; special q can reduce the support. Equal supports alone do not prove equality. |
| Six 81×81 placements and four local triples, T:1543–1620; P:40–41,131–132 | confirmed | All six direct-component comparisons and all four residuals zero. | None for this exact matrix. |
| Far commutativity, T:1553–1568,1620; mapping | confirmed with caveat | Repository checks R12/R34. Audit additionally checks R13/R24 and R14/R23. | Phrase actual suite coverage precisely; unbraided R12/R34 is not by itself a braid-group verification. |
| Classical h and commutator, proposition 10.1, T:1639–1657 | confirmed with caveat | Arbitrary-n proof in §8. Tests use exact `limit`, not floating point. | Heading says numerical; change to symbolic. Cited commutator test covers n=1,2,3, not n=4; h-diagonal test covers 1…4. |
| `[N]_ζ=0`, central E^N,F^N,K^(2N), T:1669–1673; `limits.py:24–27` | confirmed with caveat | Correct for primitive N>2 in unrestricted specialization; algebraic proof in §8. | Exclude N=1,2; distinguish order of q² and the choice of quantum-group integral form/quotient. Code does not verify centrality abstractly. |
| V2 at q=i has E=0 and is reducible, T:1675–1692 and table 10.1 | confirmed | Exact substitution; `span(v2)` proper invariant. K=(-1,1,-1), F remains one Jordan block. | Say reducible, not a direct-sum decomposition; “numerical” labels are inaccurate. |
| Small quantum group “appears,” T:1694–1698 | confirmed with caveat | Motivation only; no quotient construction, divided powers, or block classification implemented. | Specify this is external theory, not a consequence verified by the matrix example. |
| Crystal coefficient asymptotics; T:1700–1710; `limits.py:124–145` | error found | Docstring promises a single leading term but function returns a truncated Laurent series; V3 includes constants 1,2,1 as well as q⁻². | Return `as_leading_term` or change documentation. The graph is not derived from this function. |
| “Every mathematical claim” mapped/tested; T:540–542,919–922; P:116–117 | error found | Classification, general proofs, original-source transcription, centrality, and spectrum/CG compatibility are not all tested. | Restrict to explicitly implemented computational claims, with accurate coverage notes. |
| No new mathematics, no Gauss/Hopf superalgebra verification; P:132–137, mapping TODOs, README limitations | confirmed | No RTT quotient algebra, noncommutative Gauss implementation, Markov trace or Jones evaluator exists in inspected source. | Retain framing. No change to publication claims is proposed in this audit. |
| Software comparison; P:52–89 | confirmed with caveat | Current official docs support semisimple scope and Sage interface. QuaGroup manual also gives practical limitations including E8 resource cost. | “Every finite-dimensional semisimple” describes intended theoretical scope, not an unlimited practical guarantee. Historical commit-specific absence claims were not fully re-audited. “Do not fit” data models is a design judgment, not an impossibility theorem. |
| 126 tests and benchmark sizes/times; P:115–121 | confirmed with caveat | Local test count reproduced; stored benchmark records support numbers and machine description. `3^4=81`, `3^5=243`. | Historical timing not reproduced on that Xeon; benchmark times all embeddings before one triple and does not assert returned truth values. |
| Only SymPy dependency, T:544–548 | error found | `pyproject.toml` requires SymPy, NetworkX, Matplotlib; imports include them. | Correct thesis dependency sentence; paper already lists them correctly. |
| Çelik–Çelik page range and Drinfeld year, T:1796–1804; `paper.bib` | error found | Institutional and later-author references say 259–269; thesis lists conference year 1986 as bibliographic year. | Verify final pagination against PDF; distinguish ICM 1986 from publication 1987. Do not leave an author-confirmation comment as sole pagination evidence. |

## 4. Independent universal R derivation and coproduct mismatch

Write `Δp` for the package coproduct and `Δo=τΔp` for its opposite. On `V1`,

\[
 E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
 F=\begin{pmatrix}0&0\\1&0\end{pmatrix},\quad
 H=\operatorname{diag}(1,-1),\quad K=q^H.
\]

### Evaluation of the original universal series

This derivation uses Drinfeld's printed pp. 807, 816–817, not the repository docstring. Put `q=exp(h/2)`. His generators obey
`[X⁺,X⁻]=(2/h)sinh(hH/2)`. On the two-dimensional module choose `X⁺=αE`, `X⁻=βF`, where `αβ=(q-q⁻¹)/h`. They square to zero. Therefore all terms of his universal series with degree ≥2 vanish in this representation.

The degree-zero term is

\[
D=q^{H\otimes H/2}
 =\operatorname{diag}(q^{1/2},q^{-1/2},q^{-1/2},q^{1/2}).
\]

In degree one his coefficient is `h Q₁(h)=h exp(-h/2)=h q⁻¹`. The exponential in this term is
`exp(h(H⊗H+H⊗1−1⊗H)/4)`. The operator `E⊗F` takes `v₁⊗v₀` to `v₀⊗v₁`; on this output the exponent's diagonal integer is `−1+1−(−1)=1`. Thus the nonzero off-diagonal entry is

\[
 hq^{-1}\alpha\beta\,q^{1/2}
 =q^{-1/2}(q-q^{-1}).
\]

Consequently the represented universal element is exactly

\[
U=\begin{pmatrix}
q^{1/2}&0&0&0\\
0&q^{-1/2}&q^{-1/2}(q-q^{-1})&0\\
0&0&q^{-1/2}&0\\
0&0&0&q^{1/2}
\end{pmatrix}=q^{-1/2}R.
\]

This also agrees directly with Drinfeld's vector formula on p.817 at rank n=2. The final check can be made over `Q(t)` with `q=t²`, avoiding ambiguous complex power manipulation: `t U=R(t²)`. Changing the choice of t to −t changes both compensating factors, leaving the final Laurent matrix unchanged. There is no hidden extra sign or phase in the stated rescaling.

Independently, an upper triangular ansatz `diag(q,1,1,q)(I+a E⊗F)` satisfying `R Δo(E)=Δp(E) R` forces `a=q−q⁻¹`; the F equation agrees. This determines the surviving nilpotent coefficient without trusting the docstring.

The rescaled R is a **representation-level** normalization. QYBE and braid equations are homogeneous of degree three, so scalar rescaling preserves them. It does not follow that multiplying a universal element by an arbitrary scalar preserves its universal coproduct/hexagon identities; those have different degrees on the two sides.

### Explicit intertwining computation

For each generator define
`J_X(R)=R Δp(X)−(P Δp(X) P)R`, where P is the ordinary 4×4 swap. Exact cancellation gives

\[
J_E(R)=\begin{pmatrix}
0&q^2-1&q^{-1}-q&0\\
0&0&0&1-q^{-2}\\
0&0&0&q^{-1}-q\\
0&0&0&0
\end{pmatrix},
\]

\[
J_F(R)=\begin{pmatrix}
0&0&0&0\\
1-q^{-2}&0&0&0\\
q^{-1}-q&0&0&0\\
0&q^2-1&q^{-1}-q&0
\end{pmatrix}.
\]

`J_K=J_Kinv=0`. Both displayed residuals are nonzero over `Q(q)`. In contrast, `J_X(P R P)=0` for **all four generators**, and `R Δo(X)−Δp(X) R=0` for all four. The convention note at `r_matrix.py:72–82` is correct.

The package singlet is `s=(0,−q⁻¹,1,0)^T`. It is annihilated by both `Δp(E)` and `Δp(F)`. But

\[
(PR+q^{-1}I)s=(0,1-q^{-2},q-q^{-1},0)^T\ne0.
\]

The correct commuting braid operator for `Δp` is `B_p=P R21=R P`, and `(B_p+q⁻¹I)s=0`. Its q-eigenspace is generated by the three descendants of `v₀⊗v₀`. By comparison, the −q⁻¹ eigenvector of the currently returned `P R` is proportional to `(0,−q,1,0)^T`, the singlet for `Δo`. Same eigenvalue multiplicities do **not** imply same invariant subspaces.

**Recommended correction, not applied:** keep the existing R as an explicitly named opposite-convention example, expose/use `R21` when comparing with `tensor_product`, and add generator-intertwining and singlet-eigenvector tests. Alternatively change the returned convention, with an explicit API/figure/test migration. Merely changing the normalization scalar cannot fix this error.

## 5. General-n representations and Clebsch–Gordan proof obligations

### Representation formulas and basis

Set `a_k=[k][n-k+1]`, `a_0=a_(n+1)=0`. In the undivided basis, `Fv_k=v_(k+1)` and `Ev_k=a_k v_(k−1)`. Then

\[
(EF-FE)v_k=([k+1][n-k]-[k][n-k+1])v_k=[n-2k]v_k.
\]

The last identity follows by expanding the two numerators over `(q−q⁻¹)²`; it is also checked in §10 using independent variables `x=q^k`, `y=q^n`. It includes both boundary values. K conjugation follows from adjacent weights differing by 2; `K Kinv=I` is immediate. This is an arbitrary-n derivation, not an extrapolation from n≤5.

If instead `w_k=F^k v₀/[k]!`, then

\[
Fw_k=[k+1]w_{k+1},\qquad Ew_k=[n-k+1]w_{k-1}.
\]

These are the divided-basis formulas visible in Kassel VI.3.5, (3.1)–(3.3). The theorem's implemented basis is related by `v_k=[k]!w_k`. The error is specifically in the thesis proof, not the implemented generic matrices.

For generic q, K has distinct eigenvalues. A nonzero submodule contains a weight vector: apply a polynomial spectral projector in K to any nonzero vector. Every internal coefficient `[k][n-k+1]` is nonzero, so repeated E reaches v₀ and repeated F reaches every v_k. This establishes simplicity. One-dimensional weight spaces without the nonzero connecting arrows would not suffice.

For completeness of the classification, start with an arbitrary finite-dimensional type-1 simple module. Raising a nonzero weight vector by E must eventually terminate because the weights `q^(r+2j)` are distinct. Its nonzero terminal vector is highest weight. The submodule it generates is the whole simple module. If `F^m v≠0` and `F^(m+1)v=0`, the commutator identity forces `λ²=q^(2m)` for highest K-eigenvalue λ; type 1 excludes the negative sign at generic q, giving λ=q^m. The string formulas give the displayed model and uniqueness. These are the missing reasoning steps, not outcomes of `pytest`.

### CG: mathematical assertion versus implemented algorithm

For highest weight `m+n−2r`, write a candidate as
`u_r=Σ_(i=0)^r c_i v_i⊗w_(r−i)`, with `0≤r≤min(m,n)`. The package coproduct gives the recurrence

\[
c_{i+1}[i+1][m-i]
 +c_i q^{m-2i}[r-i][n-r+i+1]=0\quad(0\le i<r).
\]

The denominators needed to solve it are nonzero for generic q. This constructs one nonzero highest-weight vector for each listed weight. Each generated finite-dimensional highest-weight module is the corresponding simple `V_(m+n−2r)`. Distinct highest weights make the simple summands nonisomorphic and their sum direct; the dimension sum is `(m+1)(n+1)`. This gives the all-m,n decomposition with the highest-weight theorem, without claiming that a finite sample proves it.

The implementation presupposes the summand list, partitions columns using known exponent labels, and computes kernels. `q_sym` is unused in `find_highest_weight_vectors`; K is not consulted. This works for its documented generic standard modules with a common q. It is not a general decomposition algorithm for arbitrary matrices or root-of-unity modules, where weights can collide and additional highest vectors occur. The unused `E_sub` is redundant, not a mathematical error: the actual nullspace uses all target rows in `E_cols`.

For each displayed pair (1,1), (2,2), (3,2), I independently formed columns
`u_k, Δ(F)u_k,…,Δ(F)^k u_k` for all highest weights k in descending order, assembled a square matrix C, and checked

\[
\Delta(X)C=C\bigoplus_k\rho_k(X),\quad X=E,F,K,K^{-1}.
\]

All four residuals are zero in all three examples. Determinants in precisely that column order are:

- (1,1): `−(q²+1)²/q³`.
- (2,2): `−(q⁴+1)⁴(q²−q+1)³(q²+q+1)³/q²²`.
- (3,2): `−(q⁴+1)⁴(q²−q+1)³(q²+q+1)³(q⁴−q³+q²−q+1)⁵(q⁴+q³+q²+q+1)⁵ / (q⁵⁰(q²+1)⁴)`.

All are nonzero rational functions, establishing actual direct-sum changes of basis for these examples. This is stronger than the repository tests and should not be misreported as existing coverage. The displayed (2,2) singlet is correct in the undivided basis, including its classical limit. The (3,2) coefficient `−(q⁴+q²+1)/(q⁶+q⁴)` is also correct; only its explanatory binomial quotient is wrong.

## 6. Hopf structure: what is proved and what the checks mean

Let `Cq=(K−K⁻¹)/(q−q⁻¹)`. Direct algebra using the defining relations gives

\[
[\Delta_p(E),\Delta_p(F)]
=C_q\otimes K^{-1}+K\otimes C_q
=\frac{K\otimes K-K^{-1}\otimes K^{-1}}{q-q^{-1}}.
\]

The cross terms cancel because `KF=q⁻²FK` and `EK⁻¹=q²K⁻¹E`. Conjugation by `K⊗K` scales Δ(E), Δ(F) correctly, so the coproduct respects the defining ideal. The counit values respect the relations. Extending S antimultiplicatively also respects them: for example `S(F)S(E)−S(E)S(F)=FE−EF=(K⁻¹−K)/(q−q⁻¹)`; conjugation relations reverse consistently. This is the algebraic compatibility needed before generator checks extend to an abstract Hopf statement.

Coassociativity on E gives the identical three-term expression
`E⊗1⊗1+K⊗E⊗1+K⊗K⊗E`. On F it gives
`F⊗K⁻¹⊗K⁻¹+1⊗F⊗K⁻¹+1⊗1⊗F`; K and Kinv are group-like. Counit identities reduce directly to E,F,K,Kinv. Antipode identities reduce, for example, to
`−K⁻¹E+K⁻¹E=0`, `E−KK⁻¹E=0`,
`−FKK⁻¹+F=0`, and `FK−FK=0`, with the group-like cases giving I.

The code carries labelled decompositions, which is appropriate: neither the counit nor the coproduct is generally well-defined on a nonfaithful representation's matrix image. For example, the counit is not an algebra homomorphism `Mat_d→k` for d>1. The wording at `hopf.py:123–127` about a contraction from `V⊗V` to V should refer to the algebra factors, not vector-space states.

Technical limitations of the checker:

- `_verify_counit_via_labels` calls `counit()` but ignores its returned values, using a separate hard-coded `label_to_eps`. Thus that checker alone cannot catch an erroneous public counit; `test_counit_values` separately protects current constants.
- Counit and antipode checks use their own labelled coproduct formulas; they are not automatic checks of every change to `coproduct()`.
- `verify_all_hopf_axioms` does not verify universal multiplicativity, antimultiplicativity, units, or all algebra words. Its records do not retain residual matrices.
- Generator checks become a mathematical proof only with the extension/compatibility argument above. Finite representation tests alone cannot establish abstract equality or faithfulness.

These are evidence/maintenance limitations. They do not negate the correctness of the implemented generator formulas.

## 7. R identities, grading and arbitrary tensor powers

### Ordinary braid and Hecke identities

The nontrivial block of `B=P R` is `[[0,1],[1,q−q⁻¹]]`. Its characteristic polynomial is `(λ−q)(λ+q⁻¹)` and it satisfies `B²−(q−q⁻¹)B−I=0`; the remaining two diagonal entries are q. Consequently `B−B⁻¹=(q−q⁻¹)I`, and `det(R)=q²`, `det(B)=−q²` are nonzero for q≠0. Exact QYBE and braid residuals vanish.

For n strands, adjacent copies `B_i` satisfy the braid relation by tensoring the verified three-factor relation with identities. If `|i−j|>1`, their supports are disjoint and the matrices commute. Invertibility supplies inverse generators. This is the missing short justification for the statement about arbitrary `B_n`; no n-dependent induction of symbolic experiments is required. The extra quadratic relation yields the stated Hecke quotient. It does not define a Markov trace by itself.

At q=i, both formal eigenvalues specialize to i; the returned eigenvalue dictionary is `{I:4}` and `rank(B−iI)=1`. Thus there is a nontrivial Jordan block and no generic two-eigenspace decomposition at that specialization. The identity itself remains valid there.

### Complete entry ledger for the implemented GL matrix

Use one-based flattened indices in this table and row-major basis `(11,12,13,21,22,23,31,32,33)`. All omitted entries are zero.

| Output row | Input column | Basis action coefficient | Repository/thesis match | Original 2021 article |
| --- | --- | --- | --- | --- |
| 1 | 1 | 1 | confirmed | pending |
| 2 | 2 | q² | confirmed | pending |
| 2 | 4 | 1−q² | confirmed | pending |
| 3 | 3 | q | confirmed | pending |
| 3 | 7 | 1−q² | confirmed | pending |
| 4 | 4 | 1 | confirmed | pending |
| 5 | 5 | 1 | confirmed | pending |
| 6 | 6 | q | confirmed | pending |
| 6 | 8 | 1−q² | confirmed | pending |
| 7 | 7 | q | confirmed | pending |
| 8 | 8 | q | confirmed | pending |
| 9 | 9 | q² | confirmed | pending |

The matrix is even: every nonzero entry preserves `p(input1)+p(input2)` modulo 2. Its determinant is `q⁸`, and `R(1)=I₉`. These are internal consistency checks only. A family of other matrices could satisfy the same YBE; passing it does not establish transcription fidelity.

The existing `test_R_matrix_nonzero_pattern` checks positions, not all coefficient values. A source-backed exact-entry test is needed after the original paper is inspected.

### Which factor acquires which Koszul sign

For homogeneous maps, the graded tensor action is

\[
(A\otimes_s B)(v\otimes w)=(-1)^{p(B)p(v)}Av\otimes Bw.
\]

The right operator crosses the left input. This is different from saying that the permutation's sign belongs to one factor: the permutation has the symmetric sign `(-1)^(p(v)p(w))`. If a paper writes coefficients of `E_ai⊗_s E_bj`, their conversion to ordinary operator matrix entries contributes `(-1)^((p_b+p_j)p_i)`. Whether the printed 2021 matrix already incorporates this sign is a question for the original text. It cannot be answered from the repository alone.

For the present even operator matrix, moving input tensor factor j left to i+1 contributes `(-1)^(p(v_j) Σ_(i<k<j)p(v_k))`. Moving its output b back contributes the corresponding factor with `p(b)`. Therefore an entry `R^(a,b)_(v_i,v_j)` in a remote embedding has total sign

\[
(-1)^{(p(v_j)+p(b))\sum_{i<k<j}p(v_k)}.
\]

This proves proposition 9.1 for arbitrary n and even R: sequential adjacent super-swaps produce exactly this component formula. For adjacent i,j the sum is empty. No extra sign comes from prefix factors because R is even. For a homogeneous **odd** R, an additional prefix sign would be needed; the current unqualified generic API does not implement that general super tensor product. The GL matrix meets the needed hypothesis.

I independently assembled matrices using this formula, without using the repository's swap/conjugation helpers. Every entry matches all six embeddings for n=4. On three factors the formula also explains why swapping the first two factors around R23 and swapping the last two around R12 give the same R13: evenness gives `p(a)+p(v_i)=p(b)+p(v_j)`.

For the implemented matrix:

- All 729 entries of the graded YBE residual cancel to zero.
- Each side has 58 generically nonzero entries.
- All four 81×81 local triple residuals cancel to zero.
- Commutators for disjoint pairs (12,34), (13,24), (14,23) all vanish. Only the first is checked by the current suite.
- Replacing graded P with an ordinary swap yields exactly two nonzero 27×27 YBE entries, at zero-based positions `(8,24)` and `(17,25)`, both `2q²(q²−1)²`.

The last calculation is a negative control that demonstrates the need for grading. It is not a source-transcription test.

## 8. Limits, specialization and symbolic exactness

### Classical and root-of-unity assertions

For each weight w=n−2k, `(q^w−1)/(q−1)→w`. Together with the commutator identity from §5 this proves the proposition for every n. All relevant code uses exact `sympy.limit`. Recovering a classical algebra, however, requires an integral/formal presentation; substituting q=1 into a field of rational functions or the displayed abstract quotient denominator is not itself that construction. Kassel VI.2 explicitly distinguishes these operations.

At a primitive Nth root with N>2, `[N]=0`. The commutator formula

\[
[E,F^N]=[N]F^{N-1}
\frac{q^{-(N-1)}K-q^{N-1}K^{-1}}{q-q^{-1}}
\]

and its E/F counterpart show centrality of F^N and E^N in the unrestricted specialized algebra; K conjugation also commutes because q^(2N)=1. K^N is already central, so the weaker statement about K^(2N) is true. The least positive vanishing q-integer has index `ell=ord(q²)=N/gcd(N,2)`. For even N, confusing N with ell obscures the relevant nilpotency and small-quantum-group conventions.

N=2 is excluded from this argument: q=−1 makes the displayed quotient undefined. Its Laurent continuation instead has `[2]_(−1)=−2`, not zero. `limits.py` currently advertises N≥2 and needs correction/validation. N≤0 is also not a valid primitive-root input.

For V2 at q=i the matrices are E=0, F a length-three nilpotent Jordan block, K=diag(−1,1,−1). The subspace spanned by v2 is invariant, proving reducibility. It is **indecomposable**: a direct-sum decomposition into invariant submodules would decompose F into two nonempty nilpotent Jordan systems, impossible for a single block. Thus reducibility here is not semisimplicity or a direct-sum splitting.

In this undivided family E^N specializes to zero for every n, not just n<N (N>2): each coefficient of an N-step E path contains N consecutive q-integers and hence a multiple of ell. F^N, by contrast, is nonzero when n≥N. The `root_of_unity_substitution` docstring at lines 84–85 is misleading if its “behavior differs” is read as E^N becoming nonzero. Also, E and F are singular even for generic q; a root may change rank, not first create singularity.

The helper computes specialized powers of matrices; it neither checks centrality against abstract generators nor constructs a small quantum group.

### Exactness and specialization pitfalls

For default q, exponents and coefficients remain exact. There are no `evalf` calls or premature q substitutions in generic relation/Hopf/CG/R/YBE checks. Numeric tests use `sp.Rational(2)` or `sp.Integer(2)`; the root helper uses exact `exp(2*pi*I/N)`. Plotting sizes and benchmark timings are floating point, but are not evidence for algebraic identities.

The baseline paper correctly discloses this input boundary; the following computations reproduce the underlying API limitation:

```python
build_representation(2, q_sym=2)            # Python int -> Float entries
build_representation(2, q_sym=sp.Integer(2)) # exact entries
R_matrix_V1(2)[1, 2]                       # SymPy Float 1.5
q_integer(2, sp.Integer(-1))               # nan
sp.limit(q_integer(2), q, -1)              # -2
q_binomial(4, 2, sp.I)                     # nan
sp.cancel(q_binomial(4, 2)).subs(q, sp.I)   # 2
```

Negative powers of Python integers are evaluated before SymPy receives them. Sympifying arguments early addresses that issue; removable singularities separately require Laurent/polynomial cancellation or limits. Numeric “True” results at a single q never establish a generic-q identity.

The independent audit uses numerator cancellation for expressions in `Q(q)`. A zero numerator certifies the rational-function identity on its domain; a pole in an intermediate formula still needs a defined extension at specialization. `simplify(expr)==0` is a useful sufficient test but not a complete mathematical equality decision procedure for arbitrary accepted `Expr` inputs.

### Crystal language and asymptotics

The graph `B(n)` is the known combinatorial crystal. To construct an actual crystal basis one must specify the q=0 regular ring, a lattice, divided powers, Kashiwara operators, and reduction modulo q. Replacing E and F by literal limits in the package's undivided basis does not supply that construction. The graph and partial maps themselves are correct.

For n≥1 each nonzero E coefficient has leading term `q^(−(n−1))`. For n=1 it is finite (1), and n=0 has no such coefficient. Thus “coefficients diverge” needs qualification. In V3, `crystal_asymptotics_E_pattern` returns off-diagonal values `q⁻²+1, q⁻²+2, q⁻²+1`, rather than just the leading term q⁻². This is the behavior of `series(...,0,2).removeO()`, not a leading-term extractor. `crystal_asymptotics_F` simply returns F and does not compute Kashiwara operators.

## 9. Source-access resolution

The initial audit was held pending the primary GL source. The author supplied
it on 27 September 2026; §11 records the direct comparison. The revised
paper avoids exact Jimbo-normalization attribution unsupported by the
accessible originals, instead citing the independently evaluated Drinfeld
formula. The remaining book-access limitations above are disclosed rather
than being treated as successful literature verification. The author's
subsequent request authorizes the software and English manuscript corrections
in §12; it does not authorize committing, publishing or messaging reviewers.

## 10. Reproduction appendix

**Historical reproduction: run against the baseline revision, not the corrected working tree.**
The final exactness assertions deliberately require the old bugs and are
expected to fail after the fixes. For current verification use
`python3 -m pytest tests/ -q`, especially `test_audit_regressions.py`.

The following self-contained audit program reproduces the central positive and negative checks without editing production modules. Save it outside the package, then run from the repository root with `PYTHONPATH=.`. It asserts the **presence** of the convention error as well as the true identities, so successful execution does not mean the repository has no errors.

```python
import itertools as it
import sympy as sp
from quantum_group import (
    q, build_representation, coproduct, tensor_product,
    find_highest_weight_vectors, R_matrix_V1, R_check_V1,
    swap_matrix, qybe_residual, braid_relation_residual,
    R_matrix_GLq21, R12_GLq21, R13_GLq21, R23_GLq21,
    graded_yang_baxter_residual_GLq21, all_Rij_GLq21,
    q_integer, q_binomial,
)

def zero(M):
    return all(sp.cancel(x) == 0 for x in M)

# Universal image evaluated in a formal square-root extension.
t = sp.Symbol('t', nonzero=True)
A = build_representation(1, q_sym=t**2)
U = sp.diag(t, 1/t, 1/t, t)
U += (t**2-t**-2)/t * sp.kronecker_product(A.E, A.F)
assert zero(t*U-R_matrix_V1(t**2))

# The two coproduct conventions must not be conflated.
A = build_representation(1)
D = coproduct(A)
R, P = R_matrix_V1(), swap_matrix(2)
B = P*R
for name, M in D.items():
    J = R*M-P*M*P*R
    assert zero(J) == (name in ('K', 'K_inv'))
    assert zero((P*R*P)*M-(P*M*P)*(P*R*P))
    assert zero(R*(P*M*P)-M*R)
singlet = sp.Matrix([0, -1/q, 1, 0])
assert zero(D['E']*singlet) and zero(D['F']*singlet)
assert not zero((B+sp.eye(4)/q)*singlet)
assert zero((R*P+sp.eye(4)/q)*singlet)
assert zero(qybe_residual(R))
assert zero(braid_relation_residual(B))
assert zero(B**2-(q-1/q)*B-sp.eye(4))
print('Intertwining counterexample and positive R checks reproduced')

# Exact general-n commutator identity, x=q^k and y=q^n.
x, y = sp.symbols('x y', nonzero=True)
d = q-1/q
identity = ((q*x-1/(q*x))*(y/x-x/y)
            -(x-1/x)*(q*y/x-x/(q*y)))/d**2
assert sp.cancel(identity-(y/x**2-x**2/y)/d) == 0

# Stronger CG checks than the existing highest-vector tests.
for m, n in [(1,1), (2,2), (3,2)]:
    T = tensor_product(build_representation(m), build_representation(n))
    cols = []
    blocks = {g: [] for g in ('E', 'F', 'K', 'K_inv')}
    for k, v in find_highest_weight_vectors(T):
        cols.extend(T.F**j*v for j in range(k+1))
        V = build_representation(k)
        for g in blocks:
            blocks[g].append(getattr(V, g))
    C = sp.Matrix.hstack(*cols).applyfunc(sp.cancel)
    det = sp.factor(C.det(method='domain-ge'))
    assert det != 0
    for g in blocks:
        assert zero(getattr(T,g)*C-C*sp.diag(*blocks[g]))
    print('CG', (m,n), 'determinant:', det)

# Independent even-operator embeddings; no swap helper is used here.
parity = [0,0,1]
def flat(v):
    result = 0
    for a in v:
        result = 3*result+a
    return result

def direct_even_embedding(R, pair, n):
    i, j = pair
    M = sp.zeros(3**n)
    for v in it.product(range(3), repeat=n):
        for a, b in it.product(range(3), repeat=2):
            c = R[3*a+b, 3*v[i]+v[j]]
            if c == 0:
                continue
            assert (parity[a]+parity[b]-parity[v[i]]-parity[v[j]]) % 2 == 0
            out = list(v)
            out[i], out[j] = a, b
            exponent = (parity[v[j]]+parity[b])*sum(
                parity[v[k]] for k in range(i+1,j))
            M[flat(out), flat(v)] = (-1)**exponent*c
    return M

G = R_matrix_GLq21()
assert sp.factor(G.det()) == q**8
ops = all_Rij_GLq21(4)
for pair, M in ops.items():
    assert zero(M-direct_even_embedding(G, pair, 4))
for a,b,c in it.combinations(range(4),3):
    A,B,C = ops[a,b],ops[a,c],ops[b,c]
    assert zero(A*B*C-C*B*A)
for ij,kl in [((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]:
    assert zero(ops[ij]*ops[kl]-ops[kl]*ops[ij])
assert zero(graded_yang_baxter_residual_GLq21())
L = R12_GLq21()*R13_GLq21()*R23_GLq21()
assert sum(sp.cancel(x)!=0 for x in L) == 58
plain = sp.kronecker_product(swap_matrix(3),sp.eye(3))
wrong13 = plain*R23_GLq21()*plain
bad = R12_GLq21()*wrong13*R23_GLq21()-R23_GLq21()*wrong13*R12_GLq21()
entries = {(i,j):sp.factor(bad[i,j]) for i in range(27) for j in range(27)
           if sp.cancel(bad[i,j]) != 0}
expected = 2*q**2*(q**2-1)**2
assert set(entries) == {(8,24),(17,25)}
assert all(sp.cancel(v-expected)==0 for v in entries.values())
print('GL embeddings, YBE and wrong-swap negative control reproduced')

# API exactness and removable-singularity counterexamples.
assert R_matrix_V1(2).atoms(sp.Float)
assert not R_matrix_V1(sp.Integer(2)).atoms(sp.Float)
assert build_representation(2,q_sym=2).K.atoms(sp.Float)
assert q_integer(2,sp.Integer(-1)) is sp.nan
assert sp.limit(q_integer(2),q,-1) == -2
assert q_binomial(4,2,sp.I) is sp.nan
assert sp.cancel(q_binomial(4,2)).subs(q,sp.I) == 2
Bi = R_check_V1(sp.I)
assert Bi.eigenvals() == {sp.I:4}
assert (Bi-sp.I*sp.eye(4)).rank() == 1
print('Exactness, specialization and spectral caveats reproduced')
```

## 11. Primary-source closure: Çelik–Çelik (2021)

The author supplied the original eleven-page PDF on 27 September 2026.
Printed pagination is **259–269**. The unnumbered 9×9 display on printed
p.261, between equation (3) and Theorem 1, was visually inspected, not merely
read through text extraction. Every one of its twelve nonzero entries
matches the ledger in §7, and all remaining 69 entries are zero. No change
of parameter or added component sign is needed. This is the **unbraided R**;
the source defines the checked matrix separately as P R in Theorem 1,
equation (4). The row-major basis is consistent with the displayed T and
the source's Kronecker products.

| Source assertion | Status | Direct evidence / repository consequence |
|---|---|---|
| R entries, p.261 unnumbered display | confirmed | Diagonal (1,q²,q,1,1,q,q,q,q²); off-diagonal entries (2,4), (3,7), (6,8) are 1−q², using one-based indices. `test_gl21_primary_source_entries` fixes every entry. |
| Super-permutation, p.261 paragraph after R | confirmed | Ordinary permutation except the odd–odd (9,9) entry is −1, exactly parity (0,0,1). |
| R12, R23, R13 and graded YBE, same paragraph | confirmed | Source explicitly uses R⊗I, I⊗R, and (P⊗I)R23(P⊗I); matches the code. The independent residual and signed component tests apply directly. |
| Graded product, Definition 4, p.262 | confirmed with scope caveat | (a1⊗a2)(b1⊗b2)=(−1)^(p(a2)p(b1)) a1b1⊗a2b2. Do not add this sign a second time to the already represented operator matrix. |
| RTT, Theorem 1 Eq.(4); relations Eq.(5), pp.261–262 | outside implemented scope | The package has no noncommutative coordinate algebra or reduction modulo these relations; matrix YBE tests do not verify them. |
| Coordinate Hopf superalgebra, Theorem 2, p.263 | outside implemented scope | Generator coproduct, counit and antipode require the coordinate relation algebra. The sl2 Hopf checks cannot establish these claims. |
| Gauss factorization, Eq.(7) p.264, Theorem 6 pp.265–266 | published known result; not implemented | The order is **U D L**, with U,L unitriangular. It is not a numerical LU decomposition of the 9×9 R matrix. |
| Upper/lower quantum matrices, Theorem 7 and Remark 2, p.266 | scope constraint | U D and D L obey RTT; the source explicitly warns against imposing the same RTT form on U or L alone. |
| Bibliographic pagination | error fixed | First page 259, last page 269; `paper/paper.bib` corrected. |

Thus the earlier source-attribution “gap found” in the baseline ledger is
closed, rather than inferred from a passing YBE test. The remaining
inaccessible Jimbo/Kassel sections are still identified in the access ledger;
the final paper makes no equation-specific claim requiring them.

## 12. Authorized remediation and current verification

| Baseline finding | Resolution (committed in `bc5c370`) | Evidence |
|---|---|---|
| Coproduct mismatch | Keep historical upper R API; add `R_matrix_V1_coproduct`, `R_check_V1_coproduct`, `intertwining_residual_V1`, `intertwining_holds_V1`. Distinguish sectors explicitly. | All four generator intertwiners; full descendant sectors; historical-R negative controls; compatible QYBE/braid/Hecke tests. |
| Universal normalization | Cite directly inspected Drinfeld §13; remove unsupported exact Jimbo-normalization attribution. | Fundamental universal-series regression independently constructs the diagonal and nilpotent term. |
| Incomplete CG test coverage | Test square descendant basis C, det(C)≠0 over Q(q), and T_X C=C diag(X_k) for every generator. | Examples (1,1), (2,2), (3,2). This is finite example verification, not a new proof of the general CG theorem. |
| Integer exactness and q-arithmetic specialization | Sympify numerical parameters; Laurent sums and division-free q-binomial recurrence. | Exact integers/rationals, q=−1 and q=i; [4 choose 2]_i=2. |
| Invalid root domain and misleading E asymptotics | Require integer N>2; document E^N versus F^N; use `as_leading_term`. | Invalid-order tests, V4 at q=i, leading terms n=1…4. |
| Counit check ignored its public function | Consume `counit()` values in the labelled computation; remove dead duplicate calculation. | Mutating ε(E) causes the counit check to fail. |
| Evenness precondition omitted | Validate parity, R shape and parity preservation. | Odd operator and malformed shape rejected; six independent n=4 embeddings agree. |
| Grading tests not independent | Add direct basis-action oracle and ordinary-swap negative control. | All three disjoint commutators vanish; wrong-swap residual has exactly the two entries recorded in §7. |
| Manuscript overstated scope / AI assistance | Rewrite English manuscript, mapping and README; correct bibliography and AI disclosure. | Paper explicitly distinguishes matrix checks from abstract proofs, crystals from crystal-basis algorithms, and published identities from novel mathematics. |
| Thesis proof/convention errors | Supply `thesis/ERRATA.md` with corrected proofs and exact archived-source locations. | Historical submitted thesis PDFs remain unchanged; the English JOSS paper is the active revised manuscript. |

The q-binomial recurrence used is
C(n,k)=q^(−k) C(n−1,k)+q^(n−k) C(n−1,k−1), with C(n,0)=C(n,n)=1.
It agrees with the symmetric factorial quotient over Q(q) and defines its
Laurent-polynomial specialization without dividing by a vanishing factorial.
Relation verification still uses the defining commutator quotient, so it
rejects q=±1 and q=0; the classical-limit helper is the appropriate API there.
Floating inputs remain approximate by design.

Verification at the time of the audit: Python 3.12.10, SymPy 1.14.0. The
initial corrected suite passed **156 tests in 7.01 s**; with additional
public-facade exactness and generic q-binomial quotient regressions it had
158 tests plus 3 doctests when committed as `bc5c370`, and CI passed on that
commit. Later test additions and the current counts are recorded in
`paper/PREFLIGHT.md`. New tests belong to a correctness repair; they are not
a claimed new mathematical result.

## 13. Part 2: bounded feasibility and contribution assessment

The GL source comparison above was completed before this assessment.
This is an evidence-based decision about the requested scope, not a claim
that an exhaustive literature search proves no novel extension can exist.

| Rank | Direction | Feasibility | Contribution value / decision |
|---|---|---|---|
| 1 | Jones polynomial via the fundamental Hecke representation | High for a bounded implementation: braid words, inverses, quantum/Markov trace, writhe normalization, Markov-move checks and known knot fixtures. Fix conventions before comparing trefoil/figure-eight variables. | Useful teaching/software extension, but **not a genuine new mathematical result**. Sage already documents Jones polynomials and Markov traces, with explicit trefoil examples. Does not clear the user's novelty threshold. |
| 2 | Independent certified embeddings for even graded R operators | High for small tensor degrees; the component formula and evenness proof are already given in §7 and the errata. | Valuable regression infrastructure; follows standard super-permutation calculus. Included as correctness verification, not as a novel theorem or separate new-result module. |
| 3 | Noncommutative GL_q(2|1) Gauss verification | Medium-to-low within this repository: requires a graded noncommutative algebra, localization/inverses, ordered reduction and either a confluence proof or an independent faithful verification method. | The Gauss result itself is already Theorem 6 of Çelik–Çelik. A reliable formal verification could be useful software work, but no evidence supports a “first” claim; broad scope relative to the current matrix method. |

The [Sage braid documentation](https://doc.sagemath.org/html/en/reference/groups/sage/groups/braid.html)
provides Jones-polynomial and Markov-trace methods. Its conventional trefoil
example gives q+q³−q⁴; adopting another braid orientation or variable would
require an explicit conversion. Reproducing that known value would not
establish novelty, so no Jones implementation is manufactured for this paper.

For Gauss, the source's factorization is

```
U = [[1,u,ξ1], [0,1,ξ2], [0,0,1]]
D = diag(A,B,C)
L = [[1,0,0], [z,1,0], [η1,η2,1]]
UDL = [[A+uBz+ξ1Cη1, uB+ξ1Cη2, ξ1C],
       [Bz+ξ2Cη1,    B+ξ2Cη2,  ξ2C],
       [Cη1,         Cη2,       C]]
```

This ordered multiplication alone is easy but does not verify the theorem:
the entries must satisfy Eqs.(8)–(11), and the coordinate relations must be
recovered without assuming the conclusion. Ordinary commuting SymPy symbols
would erase exactly the relations being tested. Remark 2 further rules out
a naive RTT test on U and L separately. A finite-dimensional matrix
realization could test one representation but would not establish the
coordinate-algebra identities without additional faithfulness arguments.

**Decision: none clears the requested genuine-new-result threshold in a
bounded extension of this package.** No `paper/new_result.md` is created.
The paper retains its software-verification framing and explicitly disclaims
new mathematical results. This is a completed feasibility decision, not an
unimplemented promise or a forced weak novelty claim.
