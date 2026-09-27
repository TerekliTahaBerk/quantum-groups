"""
quantum_group
=============

Symbolic and computational models of U_q(sl_2) and GL_q(2|1) structures.

Package contents
----------------
* QuantumGroupSL2 — high-level facade class
* build_representation — constructs the V_n representation as matrices
* verify_on_representation — checks relations at the matrix level
* verify_all_hopf_axioms — checks Hopf algebra axioms
* tensor_product, find_highest_weight_vectors — tensor products and CG calculations
* R_matrix_V1, qybe_holds — R-matrix and Yang-Baxter verification
* hecke_skein_relation_check — Hecke relation on V_1
* classical_K_to_h, root_of_unity_substitution — classical and root-of-unity limits
* q_integer, q_factorial, q_binomial — q-arithmetic helpers
* plot_weight_diagram, plot_crystal_graph — visualization

Typical use
-----------
>>> from quantum_group import QuantumGroupSL2
>>> Uq = QuantumGroupSL2()
>>> rep = Uq.representation(3)
>>> all(c.holds for c in Uq.verify(rep).values())
True
"""

from .quantum_group_sl2 import QuantumGroupSL2
from .generators import E, F, K, K_inv, all_generators, commutator
from .relations import (
    symbolic_relations,
    pretty_print_relations,
    verify_on_representation,
    verify_relations_core,
    all_relations_hold,
    is_zero_matrix,
    RelationCheck,
)
from .representations import (
    Representation,
    build_representation,
    build_representation_core,
    highest_weight_vector,
    lowest_weight_vector,
    weight_of,
)
from .utils import q, q_integer, q_factorial, q_binomial, classical_limit
from .crystal import (
    build_crystal, crystal_nodes, crystal_string, f_tilde, e_tilde, CrystalNode,
)
from .visualization import plot_weight_diagram, plot_crystal_graph, plot_combined
from .hopf import (
    coproduct, counit, antipode, kron_list,
    verify_all_hopf_axioms, verify_antipode, verify_coassociativity,
    HopfAxiomCheck,
)
from .tensor import (
    TensorRepresentation, tensor_product,
    cg_summands, find_highest_weight_vectors, cg_decomposition_summary,
)
from .r_matrix import (
    R_matrix_V1, R_check_V1, swap_matrix,
    qybe_holds, braid_relation_holds,
    qybe_residual, braid_relation_residual,
    R_check_eigenvalues, hecke_skein_relation_check,
    jones_skein_relation_check,
)
from .limits import (
    classical_K_to_h, classical_commutator_EF,
    root_of_unity_substitution, three_limit_summary,
)
from .supergroup_gl21 import (
    super_parity_gl21,
    basis_pairs_gl21,
    R_matrix_GLq21,
    super_permutation_matrix,
    R12_GLq21,
    R13_GLq21,
    R23_GLq21,
    graded_yang_baxter_residual_GLq21,
    graded_yang_baxter_holds_GLq21,
    summarize_GLq21_ybe,
    embed_R_in_tensor_power,
    all_Rij_GLq21,
    braid_far_commutativity_residual_GLq21,
    local_ybe_on_four_tensor_GLq21,
)

__all__ = [
    "QuantumGroupSL2",
    "E", "F", "K", "K_inv", "q",
    "all_generators", "commutator",
    "symbolic_relations", "pretty_print_relations",
    "verify_on_representation", "verify_relations_core",
    "all_relations_hold", "is_zero_matrix", "RelationCheck",
    "Representation", "build_representation", "build_representation_core",
    "highest_weight_vector", "lowest_weight_vector", "weight_of",
    "q_integer", "q_factorial", "q_binomial", "classical_limit",
    "build_crystal", "crystal_nodes", "crystal_string",
    "f_tilde", "e_tilde", "CrystalNode",
    "plot_weight_diagram", "plot_crystal_graph", "plot_combined",
    "coproduct", "counit", "antipode", "kron_list",
    "verify_all_hopf_axioms", "verify_antipode", "verify_coassociativity",
    "HopfAxiomCheck",
    "TensorRepresentation", "tensor_product",
    "cg_summands", "find_highest_weight_vectors", "cg_decomposition_summary",
    "R_matrix_V1", "R_check_V1", "swap_matrix",
    "qybe_holds", "braid_relation_holds",
    "qybe_residual", "braid_relation_residual",
    "R_check_eigenvalues", "hecke_skein_relation_check",
    "jones_skein_relation_check",
    "classical_K_to_h", "classical_commutator_EF",
    "root_of_unity_substitution", "three_limit_summary",
    "super_parity_gl21", "basis_pairs_gl21", "R_matrix_GLq21",
    "super_permutation_matrix", "R12_GLq21", "R13_GLq21", "R23_GLq21",
    "graded_yang_baxter_residual_GLq21", "graded_yang_baxter_holds_GLq21",
    "summarize_GLq21_ybe", "embed_R_in_tensor_power", "all_Rij_GLq21",
    "braid_far_commutativity_residual_GLq21", "local_ybe_on_four_tensor_GLq21",
]
