# Convenience targets. `make check` is the canonical validation command and
# runs exactly what CI runs: `python -m pytest` (tests/ plus doctests).
PYTHON ?= python3

.PHONY: help check test lint coverage docs docs-serve quickstart listings demo \
        figures benchmark-smoke paper

help:
	@echo "check                   run tests and doctests (same as CI)"
	@echo "lint                    run ruff and mypy (needs .[dev])"
	@echo "coverage                run tests with coverage; fails below the configured threshold (needs .[dev])"
	@echo "docs                    build the documentation site into site/ (needs .[docs])"
	@echo "docs-serve              serve the documentation site locally with live reload (needs .[docs])"
	@echo "quickstart              run the README quickstart"
	@echo "listings                run the userguide's Listings 1-6 and compare with their expected outputs"
	@echo "demo                    run main.py (writes outputs/V4_combined.png)"
	@echo "figures                 regenerate the thesis figures from package output"
	@echo "benchmark-smoke         quick benchmark run written to build/benchmarks"
	@echo "paper                   build and check the SciPost userguide scipost/paper.pdf (needs pdflatex, bibtex)"

check:
	MPLBACKEND=Agg $(PYTHON) -m pytest

test: check

lint:
	$(PYTHON) -m ruff check .
	$(PYTHON) -m mypy

coverage:
	MPLBACKEND=Agg $(PYTHON) -m pytest --cov --cov-report=term

docs:
	NO_MKDOCS_2_WARNING=1 $(PYTHON) -m mkdocs build --strict

docs-serve:
	NO_MKDOCS_2_WARNING=1 $(PYTHON) -m mkdocs serve

quickstart:
	$(PYTHON) examples/quickstart.py

# Each script is run and its output compared with the stored expected output.
LISTINGS = examples/sample_verification.py \
           scipost/examples/coproduct_check.py \
           scipost/examples/transcription_check.py \
           scipost/examples/clebsch_gordan.py \
           scipost/examples/graded_four_factors.py \
           scipost/crosscheck/quagroup_crosscheck.py

listings:
	@set -e; for s in $(LISTINGS); do \
		$(PYTHON) $$s | diff - $${s%.py}_expected.txt; echo "ok  $$s"; \
	done

demo:
	$(PYTHON) main.py

figures:
	$(PYTHON) thesis/figures/generate_figures.py

benchmark-smoke:
	$(PYTHON) benchmarks/benchmark.py --repeats 1 --max-n 4 --out-dir build/benchmarks

paper:
	$(MAKE) -C scipost check
