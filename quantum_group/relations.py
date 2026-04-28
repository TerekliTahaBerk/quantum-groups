"""
relations.py
============

U_q(sl_2)'nin tanımlayıcı bağıntıları ve bunların doğrulanması.

Tanımlayıcı bağıntılar
----------------------
    (R1)  K K^{-1} = K^{-1} K = 1
    (R2)  K E K^{-1} = q^{ 2} E
    (R3)  K F K^{-1} = q^{-2} F
    (R4)  [E, F] = (K - K^{-1}) / (q - q^{-1})

Sembolik düzeyde bu bağıntılar yalnızca "tanım" olarak yazılabilir; cebrin
tutarlılığı somut bir temsille (matrislerle) doğrulanır.
`verify_on_representation` fonksiyonu, bir temsilin bu dört bağıntıyı
sağlayıp sağlamadığını sıfır-eşitliği matris testleriyle denetler.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

import sympy as sp

from .generators import E, F, K, K_inv, commutator
from .utils import q


# ---------------------------------------------------------------------------
# Sembolik bağıntı listesi (referans dokümantasyon olarak)
# ---------------------------------------------------------------------------

def symbolic_relations() -> List[Tuple[str, sp.Expr, sp.Expr]]:
    """U_q(sl_2)'nin dört tanımlayıcı bağıntısını (LHS, RHS) çiftleri olarak
    döndürür. Sembolik olarak yalnızca isimlendirme amaçlıdır."""
    return [
        ("R1: KK^{-1} = 1", K * K_inv, sp.Integer(1)),
        ("R2: KEK^{-1} = q^2 E", K * E * K_inv, q**2 * E),
        ("R3: KFK^{-1} = q^-2 F", K * F * K_inv, q**(-2) * F),
        ("R4: [E,F] = (K - K^-1)/(q - q^-1)",
         commutator(E, F),
         (K - K_inv) / (q - q**(-1))),
    ]


def pretty_print_relations() -> str:
    """Bağıntıları okunabilir biçimde yazdırır."""
    out = ["U_q(sl_2) tanımlayıcı bağıntıları:"]
    for name, lhs, rhs in symbolic_relations():
        out.append(f"  {name}:  {lhs}  =  {rhs}")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Matrissel doğrulama
# ---------------------------------------------------------------------------

@dataclass
class RelationCheck:
    """Tek bir bağıntının matris doğrulamasının sonucu."""
    name: str
    holds: bool
    residual: sp.Matrix  # LHS - RHS; bağıntı sağlanırsa sıfır matrisi

    def __repr__(self) -> str:  # pragma: no cover - kozmetik
        status = "OK" if self.holds else "BAŞARISIZ"
        return f"<{self.name}: {status}>"


def _is_zero_matrix(M: sp.Matrix) -> bool:
    """Bir SymPy matrisinin (sembolik olarak) sıfır olup olmadığını test eder."""
    M_simplified = sp.simplify(M)
    return all(sp.simplify(entry) == 0 for entry in M_simplified)


def verify_on_representation(
    E_mat: sp.Matrix,
    F_mat: sp.Matrix,
    K_mat: sp.Matrix,
    Kinv_mat: sp.Matrix,
    q_sym: sp.Expr = q,
) -> Dict[str, RelationCheck]:
    """E, F, K, K^{-1} matrislerinin U_q(sl_2) bağıntılarını sağlayıp
    sağlamadığını matris düzeyinde doğrular.

    Parametreler
    ------------
    E_mat, F_mat, K_mat, Kinv_mat : sympy.Matrix
        Üreteçlerin somut matris temsilleri. Tümü aynı (n+1) x (n+1)
        boyutunda olmalıdır.
    q_sym : sympy ifadesi
        Bağıntılarda kullanılacak q parametresi.

    Dönüş
    -----
    Bağıntı adı -> RelationCheck sözlüğü.
    """
    n = E_mat.rows
    I = sp.eye(n)

    checks: Dict[str, RelationCheck] = {}

    # R1: K K^{-1} = I
    res = K_mat * Kinv_mat - I
    checks["R1"] = RelationCheck("R1: KK^{-1} = 1", _is_zero_matrix(res), res)

    # R2: K E K^{-1} = q^2 E
    res = K_mat * E_mat * Kinv_mat - q_sym**2 * E_mat
    checks["R2"] = RelationCheck("R2: KEK^{-1} = q^2 E", _is_zero_matrix(res), res)

    # R3: K F K^{-1} = q^{-2} F
    res = K_mat * F_mat * Kinv_mat - q_sym**(-2) * F_mat
    checks["R3"] = RelationCheck("R3: KFK^{-1} = q^{-2} F", _is_zero_matrix(res), res)

    # R4: [E, F] = (K - K^{-1}) / (q - q^{-1})
    res = (E_mat * F_mat - F_mat * E_mat) - (K_mat - Kinv_mat) / (q_sym - q_sym**(-1))
    checks["R4"] = RelationCheck(
        "R4: [E,F] = (K - K^{-1})/(q - q^{-1})",
        _is_zero_matrix(res),
        res,
    )

    return checks


def all_relations_hold(checks: Dict[str, RelationCheck]) -> bool:
    """Tüm bağıntıların sağlanıp sağlanmadığını döndürür (kolaylık fonksiyonu)."""
    return all(c.holds for c in checks.values())
