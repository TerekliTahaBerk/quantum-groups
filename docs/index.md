# quantum-group

Exact symbolic verification of R-matrix and Yang–Baxter identities for
`U_q(sl_2)` and `GL_q(2|1)`.

`quantum-group` builds the explicit matrices behind concrete quantum-group
calculations with SymPy, forms the difference between the two sides of an
identity, and checks that every entry of this residual simplifies exactly to
zero. It covers finite-dimensional `U_q(sl_2)` representations and the graded
`GL_q(2|1)` R-matrix of Çelik and Çelik (2021). It verifies identities on
concrete representations; it is not a general quantum-group computer algebra
system and not a theorem prover.

!!! info "Paper"
    Taha Berk Terekli (2026), *quantum-group: Exact symbolic verification of
    R-matrix and Yang–Baxter identities for U_q(sl_2) and GL_q(2|1)*.
    [arXiv:2610.07867](https://arxiv.org/abs/2610.07867),
    DOI [10.48550/arXiv.2610.07867](https://doi.org/10.48550/arXiv.2610.07867).
    The paper's mathematical background and worked examples complement this
    site; see [Citation](citation.md) for how to cite it.

```bash
python3 -m pip install quantum-group
```

## Main features

<!-- include: README.md#Main features -->

## Where to go next

| Task | Page |
| --- | --- |
| Install the package and run a first calculation | [Getting started](getting-started.md) |
| Coproduct, basis and grading conventions; what is out of scope | [Conventions and scope](conventions.md) |
| Reproduce the paper's listings and verification claims | [Reproducing the paper](reproducibility.md) |
| Look up a function | [API reference](api/index.md) |
| Report a bug or ask a question | [GitHub issues](https://github.com/TerekliTahaBerk/quantum-groups/issues) |
