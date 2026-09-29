"""Locating a transcription error with the QYBE residual (SciPost paper, Listing 3)"""
import sympy as sp
from quantum_group import q, qybe_residual, is_zero_matrix

# R-matrix typed from a source with one mistyped sign: q + 1/q at (1, 2),
# where the source (the package's R_matrix_V1) has q - 1/q.
R_typed = sp.Matrix([[q, 0, 0,       0],
                     [0, 1, q + 1/q, 0],
                     [0, 0, 1,       0],
                     [0, 0, 0,       q]])
Y = qybe_residual(R_typed)                 # exact 8x8 residual
print("QYBE holds:", is_zero_matrix(Y))
print("nonzero entries:", {ij: sp.factor(x) for ij, x in sorted(Y.todok().items())
                           if sp.simplify(x) != 0})
