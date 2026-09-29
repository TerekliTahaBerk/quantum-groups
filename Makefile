# Convenience targets. `make check` is the canonical validation command and
# runs exactly what CI runs: `python -m pytest` (tests/ plus doctests).
PYTHON ?= python3

.PHONY: help check test quickstart listings demo figures benchmark-smoke \
        paper historical-article-pdf

help:
	@echo "check                   run tests and doctests (same as CI)"
	@echo "quickstart              run the README quickstart"
	@echo "listings                run the userguide's Listings 1-6 and compare with their expected outputs"
	@echo "demo                    run main.py (writes outputs/V4_combined.png)"
	@echo "figures                 regenerate the thesis figures from package output"
	@echo "benchmark-smoke         quick benchmark run written to build/benchmarks"
	@echo "paper                   build and check the SciPost userguide scipost/paper.pdf (needs pdflatex, bibtex)"
	@echo "historical-article-pdf  build the historical Turkish article thesis/thesis.tex (Tectonic)"

check:
	MPLBACKEND=Agg $(PYTHON) -m pytest

test: check

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

# Builds the earlier Turkish article source (not the userguide and not the
# submitted thesis). Its corrections are listed in thesis/ERRATA.md.
historical-article-pdf: figures
	cd thesis && tectonic thesis.tex
