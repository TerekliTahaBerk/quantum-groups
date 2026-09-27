# Manuscript-Code Mapping

This file maps the manuscript claims and code listings for
"Quantum Grup Yapılarının Python Ortamında Modellenmesi" (the submitted thesis
in Turkish) to repository modules and tests. Status values describe the current
repository state.

The submitted thesis PDF is `thesis/Lisans Bitirme Tezi.pdf`. The thesis LaTeX
build source is `thesis/thesis_ytu.tex`; the JOSS manuscript source is
`paper/paper.md`. `thesis/thesis.tex` is an earlier Turkish article source,
not the JOSS paper. Historical thesis files are accompanied by `thesis/ERRATA.md`.
The publication audit and source-access limitations are recorded in `AUDIT.md`.

| Manuscript item | Repository implementation | Tests | Status | Notes |
| --- | --- | --- | --- | --- |
| Code: `q_integer` | `quantum_group/utils.py::q_integer` | `tests/test_relations.py` | Implemented | Includes `[0]_q`, `[1]_q`, `[2]_q`, symmetry, and classical-limit checks. |
| `q_factorial`, `q_binomial` | `quantum_group/utils.py::q_factorial`, `q_binomial` | `tests/test_relations.py` | Implemented | Classical limits checked for representative values. |
| `classical_limit` | `quantum_group/utils.py::classical_limit` | `tests/test_relations.py`, `tests/test_representations.py` | Implemented | Uses SymPy limit at `q -> 1`. |
| Code: `build_representation` | `quantum_group/representations.py::build_representation` | `tests/test_representations.py` | Implemented | Returns a `Representation` data class with `E`, `F`, `K`, `K_inv`, and weights. |
| Draft name: `build_representation_core` | `quantum_group/representations.py::build_representation_core` | `tests/test_relations.py` | Implemented | Compatibility wrapper around `build_representation`. |
| Highest/lowest weight vectors | `highest_weight_vector`, `lowest_weight_vector` | `tests/test_representations.py` | Implemented | Checks `E v_0 = 0`, `F v_n = 0`, and highest `K` weight. |
| Code: relation residual checks | `quantum_group/relations.py::verify_on_representation` | `tests/test_relations.py` | Implemented | Returns `RelationCheck` objects with residual matrices. |
| Draft name: `verify_relations_core` | `quantum_group/relations.py::verify_relations_core` | `tests/test_relations.py` | Implemented | Compatibility wrapper around `verify_on_representation`. |
| Entrywise zero helper | `quantum_group/relations.py::is_zero_matrix` | `tests/test_relations.py` | Implemented | Public helper for symbolic zero-matrix checks. |
| Hopf coproduct | `quantum_group/hopf.py::coproduct` | `tests/test_hopf.py` | Implemented | Uses explicit representation matrices for `Delta(E)`, `Delta(F)`, `Delta(K)`, `Delta(K_inv)`. |
| Hopf counit | `quantum_group/hopf.py::counit` | `tests/test_hopf.py` | Implemented | Generator-level counit values. |
| Hopf antipode | `quantum_group/hopf.py::antipode` | `tests/test_hopf.py` | Implemented | Checks antipode identities on selected `V_n`. |
| Hopf axioms | `verify_all_hopf_axioms`, `verify_coassociativity`, `verify_antipode` | `tests/test_hopf.py` | Implemented | Representation-level symbolic checks. |
| Kronecker helper | `quantum_group/hopf.py::kron_list` | Indirect coverage through Hopf/GL tests | Implemented | Public helper; older private helpers remain for compatibility. |
| Tensor product action | `quantum_group/tensor.py::tensor_product` | `tests/test_tensor.py` | Implemented | Uses coproduct formulas on `V_m \otimes V_n`. |
| Clebsch-Gordan summands | `cg_summands`, `cg_decomposition_summary` | `tests/test_tensor.py` | Implemented | Covers `V_1⊗V_1`, `V_2⊗V_2`, `V_3⊗V_2`. |
| Highest-weight vectors in tensor products | `find_highest_weight_vectors` | `tests/test_tensor.py` | Implemented | Checks `E v = 0` and `K v = q^k v`. |
| `U_q(sl_2)` R-matrix | `quantum_group/r_matrix.py::R_matrix_V1` | `tests/test_r_matrix.py` | Implemented | Exact 4x4 entries tested. |
| QYBE residual | `qybe_residual`, `qybe_holds` | `tests/test_r_matrix.py` | Implemented | Checks 8x8 residual is zero. |
| Braided R-matrix | `R_check_V1` | `tests/test_r_matrix.py` | Implemented | `R_check = tau R`. |
| Braid relation | `braid_relation_residual`, `braid_relation_holds` | `tests/test_r_matrix.py` | Implemented | Checked for `R_check`. |
| Hecke/skein relation | `hecke_skein_relation_check` | `tests/test_r_matrix.py` | Implemented | Verifies the Hecke relation, not a Jones polynomial. The historical name `jones_skein_relation_check` remains as a deprecated alias (emits `DeprecationWarning`). |
| R-check spectrum | `R_check_eigenvalues` | `tests/test_r_matrix.py` | Implemented | Generic spectrum; historical API uses the opposite coproduct. Eigenvalues merge at q² = −1. |
| `GL_q(2|1)` parity | `super_parity_gl21` | `tests/test_supergroup_gl21.py` | Implemented | Convention `[0, 0, 1]`. |
| `GL_q(2|1)` basis ordering | `basis_pairs_gl21` | `tests/test_supergroup_gl21.py` indirectly | Implemented | Row-major `e_i ⊗ e_j`; documented in module. |
| 9x9 `GL_q(2|1)` R-matrix | `R_matrix_GLq21` | `tests/test_supergroup_gl21.py` | Implemented | All 81 entries checked against Çelik–Çelik p.261 in `test_audit_regressions.py`. |
| Super-permutation | `super_permutation_matrix` | `tests/test_supergroup_gl21.py` | Implemented | Checks involution and `P[8,8] = -1`. |
| Graded `R13` | `R13_GLq21`, `embed_R_in_tensor_power` | `tests/test_supergroup_gl21.py` | Implemented | Uses super-permutation; tested against ordinary swap difference. |
| Graded YBE residual | `graded_yang_baxter_residual_GLq21`, `graded_yang_baxter_holds_GLq21` | `tests/test_supergroup_gl21.py` | Implemented | 27x27 residual checked symbolically and numerically. |
| `V^{⊗4}` embeddings | `all_Rij_GLq21`, `embed_R_in_tensor_power` | `tests/test_supergroup_gl21.py` | Implemented | Six 81x81 placements checked against an independent basis-action formula in `test_audit_regressions.py`; even operators only. |
| Far commutativity | `braid_far_commutativity_residual_GLq21` | `tests/test_supergroup_gl21.py` | Implemented | Checks `R12 R34 = R34 R12`. |
| Local YBE on four tensor factors | `local_ybe_on_four_tensor_GLq21` | `tests/test_supergroup_gl21.py` | Implemented | Checks all four triples in `V^{⊗4}`. |
| Classical limit comparison | `classical_K_to_h`, `classical_commutator_EF` | `tests/test_limits.py` | Implemented | Representation-level checks for selected `V_n`. |
| Root-of-unity examples | `root_of_unity_substitution` | `tests/test_limits.py` | Implemented | Exploratory examples only; not full small quantum group theory. |
| Crystal graph `B(n)` | `quantum_group/crystal.py::build_crystal` | `tests/test_representations.py` | Implemented | Combinatorial graph model, not a full global basis construction. |
| Visualization: weights/crystals | `plot_weight_diagram`, `plot_crystal_graph`, `plot_combined` | `tests/test_visualization.py` | Implemented | Smoke-tested with noninteractive backend. |
| Manuscript PDF figures | `thesis/figures/generate_figures.py` | Manual validation command | Implemented | Generates `R_sl2_V1.pdf`, `R_gl21_structure.pdf`, and `ybe_products_27.pdf`. |
| Jones polynomial | None | None | TODO | The repository checks braid/Hecke relations only; Markov trace and Jones polynomial computation are out of scope. |
| Full `GL_q(2|1)` Gauss/Hopf superalgebra verification | None | None | TODO | Future work; current code verifies the R-matrix and graded YBE infrastructure. |

## Publication-audit regressions

All rows below are covered by `tests/test_audit_regressions.py` in addition to
the original module-specific tests.

| Claim | Implementation / evidence | Scope |
|---|---|---|
| Coproduct intertwining | `R_matrix_V1_coproduct`, `intertwining_residual_V1`, `intertwining_holds_V1` | All four generators on V1⊗V1; wrong-convention negative control |
| Compatible braid sectors | `R_check_V1_coproduct` | Full V2 and V0 descendant sectors; QYBE, braid and quadratic Hecke identities |
| Universal-image normalization | Independent Drinfeld §13 fundamental evaluation | Higher E/F powers vanish on V1; no assertion about uncomputed higher representations |
| Full CG basis change | `tensor_product`, `find_highest_weight_vectors` plus descendant columns in tests | (1,1), (2,2), (3,2); determinant nonzero over Q(q), all four intertwining equations |
| GL source transcription and embeddings | Çelik–Çelik p.261; independent signed component formula | Every matrix entry, all six n=4 placements and three disjoint pair commutators |
| Grading negative control | Ordinary flip substituted for super-permutation | Two explicit nonzero residual entries |
| Exact specializations | `q_integer`, `q_binomial`, `build_representation`, `R_matrix_V1` | Integer/rational parameters, q=−1 and q=i; q-arithmetic is Laurent polynomial |
| Root and crystal qualifications | `root_of_unity_substitution`, `crystal_asymptotics_E_pattern` | N>2 validation; E^N versus F^N; leading-term extraction |
| Counit dependency | `verify_counit`, `verify_all_hopf_axioms` | Mutation regression confirms checks consume the public counit values |
