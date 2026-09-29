# Cross-check against GAP's QuaGroup

`quagroup_crosscheck.py` (Listing 6 of the SciPost paper) tests data computed
by an independent system, GAP's QuaGroup package, with the residual functions
of `quantum-group`, and records the conventions in which the two systems
differ. It needs only `quantum-group` and the exported data file, not GAP.

| File | Content |
|---|---|
| `quagroup_export.g` | GAP script that exports QuaGroup's module matrices of V_1, V_2, V_3, the action on V_n ⊗ V_n (n = 1, 2) and `RMatrix(V_n)` |
| `quagroup_data.txt` | its output (SHA-256 `6c88ebef400de7d62f8083dbad2201a02bc8ee8a391eb0102e2b0c4ac258e806`) |
| `quagroup_crosscheck.py` | the cross-check |
| `quagroup_crosscheck_expected.txt` | its output, compared by `make -C scipost check` |

Data were generated on 29 September 2026 with GAP 4.12.1 (Ubuntu package
`gap`) and QuaGroup 1.8.4 (github.com/gap-packages/quagroup, commit
`72751e51f8fd0b7d100036ee6078b628370dc101`):

    git clone https://github.com/gap-packages/quagroup.git /tmp/gappkg/pkg/quagroup
    gap -q -l ";/tmp/gappkg" quagroup_export.g > quagroup_data.txt

Findings (all exact):

- QuaGroup's V_1, V_2, V_3 satisfy the four defining relations as checked by
  `verify_on_representation`.
- Same K; QuaGroup's basis is the divided-power basis F^(k) v_0 = F^k v_0 / [k]!,
  so E and F agree after conjugation with D = diag(1/[k]!).
- QuaGroup's action on V_n ⊗ V_n equals the package coproduct
  Δ(E) = E⊗1 + K⊗E, Δ(F) = F⊗K^{-1} + 1⊗F.
- GAP prints `RMatrix` in the row-vector convention (QuaGroup builds it row by row
  from the images of the basis vectors, `gap/rmat.gi`, method `RMatrix`): taken as printed, θP does
  not commute with Δ; transposed, it satisfies the QYBE, the braid relation, and
  θP commutes with Δ.
- θ (transposed) = q · R_21(q^{-1}) for V_1, i.e. QuaGroup's braiding is the
  inverse of the package's, rescaled by q.
- QuaGroup's 9×9 R-matrix of V_2 (not provided by the package), transported to
  the package basis, satisfies the QYBE and commutes with the package coproduct;
  braid eigenvalues q^{-2} (×5), −q^2 (×3), q^4 (×1).
