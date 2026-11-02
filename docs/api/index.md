# API reference

Everything listed here is importable from the top-level package,
for example `from quantum_group import qybe_holds`; the pages are grouped
by the module that defines each object. The paper's Appendix A gives the
same interface in condensed form.

Naming follows one pattern: a `*_residual` function returns the exact SymPy
difference matrix of an identity, and its `*_holds` companion returns whether
every entry of that residual simplifies to zero.

| Module | Contents |
| --- | --- |
| [`quantum_group_sl2`](quantum_group_sl2.md) | `QuantumGroupSL2`, a facade over the `U_q(sl_2)` functions |
| [`generators`, `relations`](relations.md) | Symbolic generators and the defining relations as residual checks |
| [`representations`](representations.md) | The modules `V_n`: matrices of `E`, `F`, `K`, `K_inv`, weights |
| [`hopf`](hopf.md) | Coproduct, counit, antipode and generator-level Hopf identities |
| [`tensor`](tensor.md) | Tensor products and Clebsch–Gordan highest-weight vectors |
| [`r_matrix`](r_matrix.md) | The R-matrix on `V_1 ⊗ V_1`: QYBE, braid, Hecke, intertwining |
| [`supergroup_gl21`](supergroup_gl21.md) | The graded `GL_q(2|1)` R-matrix and its placements on `V^{⊗n}` |
| [`limits`](limits.md) | Classical limits and root-of-unity substitutions |
| [`crystal`, `visualization`](crystal.md) | The crystal graph `B(n)` and weight/crystal plots |
| [`utils`, `linalg`](utils.md) | `q`-integers, factorials, binomials; Kronecker and zero tests |
