# Export U_q(sl_2) data computed by GAP's QuaGroup package, for the
# cross-check in quagroup_crosscheck.py. Run from this directory with
#   gap -q -l ";<dir containing pkg/quagroup>" quagroup_export.g > quagroup_data.txt
# Action matrices (ActionMatrix below) are written in the column convention
# used by quantum-group: entry [i][j] is the coefficient of basis vector i in
# (generator . basis vector j). RMatrix_Vn is QuaGroup's own output, printed
# unchanged: QuaGroup builds it row by row from the images of the basis vectors
# (gap/rmat.gi, method RMatrix), i.e. in GAP's row-vector convention.
SizeScreen([4096, 200]);;
LoadPackage("quagroup");
U := QuantizedUEA(RootSystem("A", 1));;
gens := GeneratorsOfAlgebra(U);;   # [ F, K, K^-1, E ]
names := [ "F", "K", "K_inv", "E" ];;

ActionMatrix := function(g, V)
  local b, n, i, j, M, c;
  b := BasisVectors(Basis(V)); n := Length(b);
  M := List([1..n], i -> List([1..n], j -> 0));
  for j in [1..n] do
    c := Coefficients(Basis(V), g ^ b[j]);
    for i in [1..n] do M[i][j] := c[i]; od;
  od;
  return M;
end;;

PrintMat := function(label, M)
  Print(label, " = ", M, "\n");
end;;

Print("# QuaGroup ", GAPInfo.PackagesLoaded.quagroup[2], ", GAP ", GAPInfo.Version, "\n");
for n in [1, 2, 3] do
  V := HighestWeightModule(U, [n]);;
  Print("basis_V", n, " = \"", BasisVectors(Basis(V)), "\"\n");
  for k in [1..4] do PrintMat(Concatenation(names[k], "_V", String(n)), ActionMatrix(gens[k], V)); od;
od;
for n in [1, 2] do
  V := HighestWeightModule(U, [n]);;
  PrintMat(Concatenation("RMatrix_V", String(n)), RMatrix(V));
  T := TensorProductOfAlgebraModules(V, V);;
  Print("basis_T", n, " = \"", BasisVectors(Basis(T)), "\"\n");
  for k in [1..4] do PrintMat(Concatenation(names[k], "_T", String(n)), ActionMatrix(gens[k], T)); od;
od;
QUIT;
