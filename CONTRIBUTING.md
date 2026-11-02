# Contributing to quantum-group

Thanks for your interest in improving this package. Bug reports, questions,
documentation fixes and new verified checks are all welcome.

## Reporting issues

Open an issue at <https://github.com/TerekliTahaBerk/quantum-groups/issues>.

- **Bugs:** include a minimal code snippet that reproduces the problem, the
  full traceback or the unexpected output, and your Python, SymPy and
  `quantum-group` versions (`python -c "import sympy; print(sympy.__version__)"`).
- **Mathematical questions or suspected wrong results:** state the relation or
  convention you expected (with a reference if possible) and the representation
  or parameter values where it fails.
- **Feature requests:** describe the structure or check you would like to see
  and how it relates to the existing modules.

Please search existing issues before opening a new one. The issue forms
include fields for reproducing examples and mathematical conventions.
See the [documentation index](docs/README.md) and
[reproducibility guide](docs/reproducibility.md) for paper-related work.

## Development setup

```bash
git clone https://github.com/TerekliTahaBerk/quantum-groups.git
cd quantum-groups
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e ".[dev]"        # tests, lint, type check, coverage
python3 -m pip install -e ".[docs]"       # optional: the documentation site
```

Python 3.10 or newer is required. `.[test]` installs only pytest, which is
enough to run the suite.

## Running the tests

The canonical validation command runs the test suite and the package
doctests (configured in `pyproject.toml`); CI runs exactly this:

```bash
python3 -m pytest        # or: make check
```

Targeted runs are useful while iterating:

```bash
python3 -m pytest tests/test_r_matrix.py
python3 -m pytest tests/test_supergroup_gl21.py
```

The `GL_q(2|1)` tensor-power checks manipulate symbolic `81x81` matrices and
are the slowest part of the suite.

## Lint, type checking and coverage

Ruff, mypy and coverage are configured in `pyproject.toml`, and CI runs all
three:

```bash
make lint        # ruff check . && mypy
make coverage    # pytest with coverage; fails below the configured threshold
```

`ruff check --fix .` applies the safe automatic fixes. `examples/` and the
manuscript folders are excluded from linting, because they are quoted
verbatim in the README and the userguide; change them only together with
their quoted copies and expected outputs.

## Documentation site

The site at <https://tereklitahaberk.github.io/quantum-groups/> is built with
MkDocs from `mkdocs.yml` and `docs/`; the API reference is generated from the
docstrings. README sections, the changelog and the quickstart script are
included rather than copied (see `docs/_hooks/repo_files.py`), so edit them
in place. Build or preview the site with:

```bash
make docs          # strict build into site/; warnings are errors, as in CI
make docs-serve    # live preview at http://127.0.0.1:8000/
```

## Support and maintenance

The package is maintained by its author on a best-effort basis. Use GitHub
issues for questions as well as bug reports.

## Pull request process

1. Fork the repository and create a topic branch from `main`.
2. Make your change, adding or updating tests in `tests/` for any new or
   modified behaviour.
3. **Run `python3 -m pytest` locally; the full suite, including doctests,
   must pass before you open a pull request.** Run `make lint` as well.
4. Open a pull request describing what changed and why. For mathematical
   changes, cite the convention or reference you follow.
5. GitHub Actions runs the suite on Python 3.10–3.13, with the oldest
   supported dependency versions, and on Linux, macOS and Windows, and runs
   the examples against an installed wheel, for every push and pull
   request. It also runs ruff, mypy and a coverage threshold, and builds the
   documentation site; a pull request is merged only when CI is green.

Keep pull requests focused: one logical change per pull request is easier to
review.

## Code style

Follow the style of the existing modules in `quantum_group/`:

- Work with exact symbolic objects (`sympy.Matrix`, the shared symbol
  `quantum_group.utils.q`); avoid floating-point approximations in checks.
- Use type hints and `from __future__ import annotations`, as the existing
  modules do.
- Give every module and public function a docstring stating the convention
  and the relation being checked. Write docstrings and comments in English.
- Verification helpers follow the existing pattern: a `*_residual` function
  returning the symbolic difference matrix and a `*_holds` / `*_check`
  function returning `bool` (or a `dict` of named `bool` results).
- Private helpers start with an underscore and are not imported across
  modules. Shared matrix helpers (`kron`, `kron_list`, `is_zero_matrix`) live
  in `quantum_group/linalg.py`; shared argument checks live in
  `quantum_group/_validation.py`.
- Reject invalid arguments with a clear `TypeError` or `ValueError` and add a
  test for each validation path, but do not forbid legitimate symbolic
  input (for example a symbolic `q`).
- New public functions are exported from `quantum_group/__init__.py` and
  listed in `__all__`.
- Do not break the public API. When renaming a public function, keep the old
  name as a thin wrapper that emits a `DeprecationWarning` and calls the new
  function (see `jones_skein_relation_check`, the deprecated alias of
  `hecke_skein_relation_check` in `quantum_group/r_matrix.py`).
- If a change affects a result reproduced in the manuscript, update
  `MANUSCRIPT_CODE_MAPPING.md` accordingly.

## License

By contributing, you agree that your contributions will be licensed under the
MIT License (see `LICENSE`).
