# Mathematical corrections to the archived thesis

Date: 27 September 2026. Applies to `thesis_ytu.tex` at revision
`dbe56afbb831a0734c964227e2c46209fca05848` and its existing PDF derivatives.
The archived thesis/PDFs have not been silently replaced. The current English
manuscript, the SciPost Physics Codebases userguide in `../scipost/`,
incorporates these scope and convention corrections (as did the earlier
JOSS draft, now `../archive/joss/paper.md`). Line numbers below refer to the archived source.

| Location | Correction |
|---|---|
| Theorem 4.1, lines 789–795 | The stated generator matrices use **v_k = F^k v_0**, without division by [k]_q!. The classification is a cited theorem; the displayed sketch only constructs the modules. |
| Lines 511, 1663 | There are three axiom families checked on four generators: **12 result records**, comprising **20 matrix equalities** (4 coassociativity, 8 counit, 8 antipode), not nine identities. These are representation-level checks. |
| Line 1062 | The coefficient tends to **−3/2**. Its magnitude corresponds to binom(3,1)/binom(2,1), not binom(3,1)/binom(2,0). |
| Equation (R), chapter 8 | The displayed upper-triangular R is multiplied by q^(1/2) relative to the fundamental universal image and intertwines the **opposite** of the package coproduct. |
| Proposition 8.4 and spectral figure, lines 1226–1260 | For the package coproduct, the braid with the stated V2/V0 eigenspaces is **B = P R_21 = R P**, not P R. The generic eigenvalues coincide, but the eigenspaces differ. “Symmetric” means q-deformed sectors, not ordinary flip eigenspaces. The unsubstantiated physical interpretation of these eigenvalues should be removed. |
| Proposition 9.1, lines 1460–1473 | Require R to be **even**. Use the signed basis-action proof below; plain Kronecker insertion does not define an odd operator on arbitrary factors without prefix signs. |
| Root-of-unity section, lines 1668–1694 | Require a primitive root of order N>2. In the implemented undivided family E^N=0 for every n, while F^N is nonzero when n≥N. Reducibility does not imply a direct-sum decomposition. This example does not construct the small quantum group. |
| Crystal section | B(n) is a combinatorial model. A crystal basis requires a lattice, divided powers and Kashiwara operators; it is not obtained by taking literal entrywise limits of E and F. For n≥1, nonzero E entries have leading term q^(−(n−1)); for n=1 they remain finite. |
| Software description, lines 544–548 and 967–984 | Runtime dependencies are SymPy, NetworkX and Matplotlib. The relation-check listing is pseudocode: the public API takes `E_mat`, `F_mat`, `K_mat`, `Kinv_mat` and returns `RelationCheck` objects, not bare Booleans. |
| Bibliography, lines 1799–1802 | Çelik–Çelik: **259–269**, confirmed from the original PDF. Drinfeld proceedings publication year: **1987** (congress held in 1986). |

## Corrected representation argument

Work over Q(q), or specialize to a nonzero complex q which is not a root
of unity. Set v_k=F^k v_0 for 0≤k≤n, with Fv_n=0. Induction using
[E,F]=(K−K^−1)/(q−q^−1) gives
E v_k=[k]_q[n−k+1]_q v_(k−1), and K v_k=q^(n−2k)v_k.
The identity
[k+1]_q[n−k]_q−[k]_q[n−k+1]_q=[n−2k]_q verifies the commutator,
including the endpoints. The K-conjugation identities follow by comparing
adjacent diagonal entries, so these matrices define a representation.

The K eigenvalues are distinct. A nonzero invariant subspace contains a
basis vector: apply the polynomial spectral projector
∏_(j≠k)(K−q^(n−2j)I)/(q^(n−2k)−q^(n−2j)) to a vector with nonzero kth
component. All interior E coefficients are nonzero, so repeated E reaches
v_0, and repeated F then generates every v_k. Hence the module is
irreducible. Classification of all finite-dimensional type-1 irreducibles
requires the highest-weight theorem, cited in Kassel VI.3.5; it does not
follow merely from the existence of this family.

For comparison, the divided basis w_k=F^k v_0/[k]_q! gives
F w_k=[k+1]_q w_(k+1) and E w_k=[n−k+1]_q w_(k−1).
It is this distinction that the original proof omitted.

## Coproduct and spectral correction

Write Δ_p(E)=E⊗1+K⊗E and Δ_p(F)=F⊗K^−1+1⊗F. The historical R obeys the
intertwining equation for Δ_p^op. Define R_p=P R P. Then
R_p Δ_p(X)=Δ_p^op(X) R_p and B=P R_p commutes with Δ_p(X).
The singlet is s=(0,−q^−1,1,0)^T and Bs=−q^−1s. By contrast,
(PR+q^−1 I)s=(0,1−q^−2,q−q^−1,0)^T, which is generically nonzero.
On the highest vector of V2, B acts by q, and commutation with Δ_p(F)
propagates this to its three descendants. At q²=−1 the two eigenvalues
coalesce, and B has a nonzero rank-one nilpotent part; the generic spectral
decomposition cannot be specialized unchanged.

## Proof of the even-operator embedding formula

Let R be even, let the input tuple be (v_0,…,v_(n−1)), and let an entry
R^(ab)_(v_i v_j) be nonzero. Moving v_j left across the intervening factors
gives sign (−1)^(p(v_j) S), where S=Σ_(i<k<j)p(v_k). After R acts, moving
the second output b back gives sign (−1)^(p(b) S). Their product is
(−1)^((p(v_j)+p(b)) S). The output replaces positions i,j by a,b and leaves
the other factors fixed. This is precisely conjugation by the indicated
adjacent super-permutations. Evenness ensures insertion after the prefix
has no additional graded tensor-product sign. For adjacent factors S=0.
This proves the placement formula for every n; finite tests verify the
implementation rather than serving as the proof of the general statement.

## Root-of-unity example

At q=i in V2, E=0, K=diag(−1,1,−1), and F is a single nilpotent Jordan
block. The subspace span(v_2) is invariant, so the representation is
reducible. It is nevertheless indecomposable: a direct-sum module splitting
would split F into at least two Jordan blocks. At a primitive Nth root,
N>2, the first vanishing q-integer has index ord(q²)=N/gcd(N,2).
Any N consecutive E steps encounter a vanishing q-integer (or a boundary),
whereas F retains unit coefficients until the boundary. Conventions for
restricted/unrestricted integral forms must be specified before asserting
results about a small quantum group.
