"""
quantum_group
=============

U_q(sl_2) kuantum grubunun sembolik ve hesaplamalı modeli.

Paket içeriği
-------------
* QuantumGroupSL2  — üst seviye cephe sınıfı
* build_representation — V_n temsilini matris olarak inşa eder
* verify_on_representation — bağıntıları matris düzeyinde doğrular
* q_integer, q_factorial, q_binomial — q-aritmetik yardımcıları
* plot_weight_diagram, plot_crystal_graph — görselleştirme

Tipik kullanım
--------------
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
    all_relations_hold,
    RelationCheck,
)
from .representations import (
    Representation,
    build_representation,
    highest_weight_vector,
    lowest_weight_vector,
    weight_of,
)
from .utils import q, q_integer, q_factorial, q_binomial, classical_limit
from .crystal import (
    build_crystal, crystal_nodes, crystal_string, f_tilde, e_tilde, CrystalNode,
)
from .visualization import plot_weight_diagram, plot_crystal_graph, plot_combined

__all__ = [
    "QuantumGroupSL2",
    "E", "F", "K", "K_inv", "q",
    "all_generators", "commutator",
    "symbolic_relations", "pretty_print_relations",
    "verify_on_representation", "all_relations_hold", "RelationCheck",
    "Representation", "build_representation",
    "highest_weight_vector", "lowest_weight_vector", "weight_of",
    "q_integer", "q_factorial", "q_binomial", "classical_limit",
    "build_crystal", "crystal_nodes", "crystal_string",
    "f_tilde", "e_tilde", "CrystalNode",
    "plot_weight_diagram", "plot_crystal_graph", "plot_combined",
]
