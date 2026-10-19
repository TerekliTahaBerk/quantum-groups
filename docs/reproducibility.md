# Reproducing the paper

Paper: Taha Berk Terekli (2026), *quantum-group: Exact symbolic verification
of R-matrix and Yang–Baxter identities for U_q(sl_2) and GL_q(2|1)*,
[arXiv:2610.07867v1](https://arxiv.org/abs/2610.07867v1),
[DOI: 10.48550/arXiv.2610.07867](https://doi.org/10.48550/arXiv.2610.07867).

The paper documents software **1.1.1**, archived at
[10.5281/zenodo.23039671](https://doi.org/10.5281/zenodo.23039671).
Use tag `v1.1.1` to reproduce that release. The default branch also contains
later documentation updates; see the [changelog](../CHANGELOG.md).

## Install the archived software

Run the commands below in a terminal. Python 3.10–3.13 is exercised in CI.
`make` is required for the convenience targets (on Windows, use Git Bash
with Make, WSL, or run the Python scripts directly).

```bash
git clone --branch v1.1.1 https://github.com/TerekliTahaBerk/quantum-groups.git
cd quantum-groups
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e ".[test]"
python3 -c "import quantum_group; print(quantum_group.__version__)"
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`.
For application use without the source materials:
`python3 -m pip install quantum-group==1.1.1`.

## Run the verification suite and paper listings

From the repository root, with the environment activated:

```bash
make check
make quickstart
make listings
```

`make check` runs pytest and package doctests. `make listings` runs all six
paper listings and compares their output with the tracked expected output;
a mismatch makes the command fail. The listings include negative controls
that deliberately use incompatible conventions.

| Listing | Script | What it demonstrates |
| --- | --- | --- |
| 1 | [sample_verification.py](../examples/sample_verification.py) | Exact checks and an ungraded-swap negative control |
| 2 | [coproduct_check.py](../scipost/examples/coproduct_check.py) | Historical and compatible coproduct conventions |
| 3 | [transcription_check.py](../scipost/examples/transcription_check.py) | Inspecting a transcription residual |
| 4 | [clebsch_gordan.py](../scipost/examples/clebsch_gordan.py) | Highest-weight vectors and a change of basis |
| 5 | [graded_four_factors.py](../scipost/examples/graded_four_factors.py) | Tensor placement and basis-parity consistency |
| 6 | [quagroup_crosscheck.py](../scipost/crosscheck/quagroup_crosscheck.py) | Comparison with stored GAP/QuaGroup data |

GAP is unnecessary for replaying Listing 6: its exported data are tracked.
To regenerate those data, follow the [cross-check guide](../scipost/crosscheck/README.md).
For individual mathematical claims and targeted test commands, see the
[README validation table](../README.md#userguide-and-reproducing-its-calculations)
and [manuscript-to-code mapping](../MANUSCRIPT_CODE_MAPPING.md).

## Build the manuscripts

The PDFs are already tracked. Rebuilding requires a LaTeX distribution
providing `pdflatex`, `bibtex` and the packages used in the preambles
(including the fonts); installing the Python package does not install TeX.

```bash
make paper
make -C arxiv check
make -C arxiv bundle
```

Edit `scipost/paper.tex` and `scipost/references.bib` first. The arXiv build
regenerates its sources from them. The checks verify listing outputs,
bibliography links and LaTeX diagnostics; the bundle check also compiles
the upload archive independently. The bundle is written to
`arxiv/arxiv_source.tar.gz` and is ignored by Git.

The local manuscripts may evolve after an arXiv submission. For the exact
published text, use the versioned arXiv record above; for exact release
files, use the versioned Zenodo archive.

## Optional figures and timings

```bash
make figures
make benchmark-smoke
```

`make figures` regenerates the thesis figures. `make benchmark-smoke`
writes a short timing run to `build/benchmarks/`. To reproduce the full
benchmark protocol, use `python3 benchmarks/benchmark.py`; this overwrites
`benchmarks/results.csv` and `benchmarks/results.md`. Timings depend on the
machine and dependency versions; the recorded values are reference
measurements, not pass/fail thresholds.
