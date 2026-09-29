"""Which coproduct does an R-matrix intertwine? (SciPost paper, Listing 2)"""
import sympy as sp
from quantum_group import (build_representation, coproduct, swap_matrix,
                           R_matrix_V1, R_matrix_V1_coproduct, qybe_holds,
                           is_zero_matrix)

D = coproduct(build_representation(1))   # Delta(X) on V_1 (x) V_1, 4x4
P = swap_matrix(2)                       # ordinary flip of the two factors

def intertwining_residual(R, X):
    """R Delta(X) - Delta^op(X) R, with Delta^op(X) = P Delta(X) P."""
    return R * D[X] - P * D[X] * P * R

for name, R in [("R_matrix_V1", R_matrix_V1()),
                ("R_matrix_V1_coproduct", R_matrix_V1_coproduct())]:
    print(name, "- QYBE:", qybe_holds(R))
    for X in ("E", "F", "K"):
        res = intertwining_residual(R, X)
        nonzero = {ij: sp.factor(x) for ij, x in sorted(res.todok().items())
                   if sp.simplify(x) != 0}
        print(f"  {X}:", "zero" if is_zero_matrix(res) else nonzero)
