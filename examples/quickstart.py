"""README quickstart, kept as a script so CI can run it verbatim.

Run from any directory after installing the package:

    python examples/quickstart.py
"""

from quantum_group import (
    build_representation,
    verify_on_representation,
    R_matrix_V1_coproduct,
    intertwining_holds_V1,
    qybe_holds,
    graded_yang_baxter_residual_GLq21,
    is_zero_matrix,
)

# U_q(sl_2): the 3-dimensional module V_2 satisfies the defining relations.
rep = build_representation(2)
checks = verify_on_representation(rep.E, rep.F, rep.K, rep.K_inv)
assert all(check.holds for check in checks.values())

# The fundamental R-matrix compatible with the package coproduct satisfies
# the QYBE and intertwines the coproduct for every generator.
assert qybe_holds(R_matrix_V1_coproduct())
assert all(intertwining_holds_V1(X) for X in ("E", "F", "K", "K_inv"))

# GL_q(2|1): the graded Yang-Baxter residual is an exact 27x27 zero matrix.
residual = graded_yang_baxter_residual_GLq21()
assert residual.shape == (27, 27) and is_zero_matrix(residual)

print("quickstart: all checks passed")
