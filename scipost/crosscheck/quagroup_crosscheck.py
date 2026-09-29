"""Cross-check against GAP's QuaGroup (SciPost paper, Listing 6)"""
import re
import sympy as sp
from quantum_group import (q, build_representation, coproduct, swap_matrix,
                           verify_on_representation, R_matrix_V1_coproduct,
                           qybe_holds, braid_relation_residual, is_zero_matrix)
from quantum_group.linalg import kron

G = {}  # matrices exported from QuaGroup by quagroup_export.g
for line in open(__file__.replace("quagroup_crosscheck.py", "quagroup_data.txt")):
    if m := re.match(r"(\w+) = (\[.*\])$", line.strip()):
        G[m[1]] = sp.Matrix(sp.sympify(m[2].replace("^", "**"), {"q": q}))
Z = is_zero_matrix

for n in (1, 2, 3):                      # QuaGroup's V_n vs the package's V_n
    E, F, K, Ki = (G[f"{X}_V{n}"] for X in ("E", "F", "K", "K_inv"))
    ok = all(c.holds for c in verify_on_representation(E, F, K, Ki).values())
    D = sp.diag(*[1 / sp.prod([sum(q**(k - 1 - 2*i) for i in range(k))
                               for k in range(1, j + 1)]) for j in range(n + 1)])
    r = build_representation(n)          # D = diag(1/[j]!): divided powers
    print(f"V_{n}: relations {ok}, equal after D:",
          Z(D * E * D.inv() - r.E) and Z(D * F * D.inv() - r.F) and K == r.K)

for n in (1, 2):                         # QuaGroup's V_n (x) V_n and R-matrix
    E, F, K, Ki = (G[f"{X}_V{n}"] for X in ("E", "F", "K", "K_inv"))
    I, P = sp.eye(n + 1), swap_matrix(n + 1)
    Delta = {"E": kron(E, I) + kron(K, E), "F": kron(F, Ki) + kron(I, F),
             "K": kron(K, K)}
    print(f"V_{n} (x) V_{n}: action = package coproduct:",
          all(Z(Delta[X] - G[f"{X}_T{n}"]) for X in "EFK"))
    for label, th in (("as printed", G[f"RMatrix_V{n}"]),
                      ("transposed", G[f"RMatrix_V{n}"].T)):
        commutes = all(Z(th * P * G[f"{X}_T{n}"] - G[f"{X}_T{n}"] * th * P)
                       for X in ("E", "F", "K"))
        print(f"  RMatrix {label}: QYBE {qybe_holds(th)},",
              f"braid {Z(braid_relation_residual(th * P))},",
              f"theta P commutes with Delta {commutes}")

th, R21 = G["RMatrix_V1"].T, R_matrix_V1_coproduct()
print("theta = q * R_21(1/q):", Z(th - q * R21.subs(q, 1 / q)))
D2 = sp.diag(1, 1, 1 / (q + 1 / q))
th2 = kron(D2, D2) * G["RMatrix_V2"].T * kron(D2, D2).inv()   # package basis
Rc2, cp = th2 * swap_matrix(3), coproduct(build_representation(2))
print("V_2 R-matrix in package basis: QYBE", qybe_holds(th2), "| commutes",
      all(Z(Rc2 * cp[X] - cp[X] * Rc2) for X in ("E", "F", "K")),
      "| eigenvalues", {sp.factor(k): v for k, v in Rc2.eigenvals().items()})
