"""Highest-weight vectors of V_2 (x) V_1 (SciPost paper, Listing 4)"""
from quantum_group import (build_representation, tensor_product,
                           find_highest_weight_vectors, cg_summands)

T = tensor_product(build_representation(2), build_representation(1))
print("summands V_k, k =", cg_summands(2, 1))
for k, v in find_highest_weight_vectors(T):
    print(f"k = {k}:", list(v))
