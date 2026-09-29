"""Graded checks on four factors and a reordered basis (SciPost paper, Listing 5)"""
import sympy as sp
from quantum_group import (R_matrix_GLq21, embed_R_in_tensor_power,
                           local_ybe_on_four_tensor_GLq21,
                           braid_far_commutativity_residual_GLq21, is_zero_matrix)
from quantum_group.linalg import kron

print("local YBE on V^(x)4:", local_ybe_on_four_tensor_GLq21())
print("R12 R34 = R34 R12:", is_zero_matrix(braid_far_commutativity_residual_GLq21()))

# Reorder the basis so that the odd vector comes first: f = (e_2, e_0, e_1).
perm = [2, 0, 1]
Pi = sp.Matrix(3, 3, lambda k, i: int(perm[k] == i))     # new = Pi * old
R_new = kron(Pi, Pi) * R_matrix_GLq21() * kron(Pi, Pi).T
for parity in ([1, 0, 0], [0, 0, 1]):                     # updated / stale
    R12, R13, R23 = (embed_R_in_tensor_power(R_new, ij, 3, parity)
                     for ij in [(0, 1), (0, 2), (1, 2)])
    Y = R12 * R13 * R23 - R23 * R13 * R12
    print("parities", parity, "graded YBE holds:", is_zero_matrix(Y),
          "| nonzero entries:", sum(sp.simplify(x) != 0 for x in Y))
