# Convenience targets. `make check` is the canonical validation command and
# runs exactly what CI runs: `python -m pytest` (tests/ plus doctests).
PYTHON ?= python3
INARA_IMAGE ?= openjournals/inara:latest

.PHONY: help check test quickstart demo figures benchmark-smoke \
        joss-pdf historical-article-pdf

help:
	@echo "check                   run tests and doctests (same as CI)"
	@echo "quickstart              run the README quickstart"
	@echo "demo                    run main.py (writes outputs/V4_combined.png)"
	@echo "figures                 regenerate the thesis figures from package output"
	@echo "benchmark-smoke         quick benchmark run written to build/benchmarks"
	@echo "joss-pdf                build paper/paper.pdf with the JOSS Inara image (Docker)"
	@echo "historical-article-pdf  build the historical Turkish article thesis/thesis.tex (Tectonic)"

check:
	MPLBACKEND=Agg $(PYTHON) -m pytest

test: check

quickstart:
	$(PYTHON) examples/quickstart.py

demo:
	$(PYTHON) main.py

figures:
	$(PYTHON) thesis/figures/generate_figures.py

benchmark-smoke:
	$(PYTHON) benchmarks/benchmark.py --repeats 1 --max-n 4 --out-dir build/benchmarks

joss-pdf:
	docker run --rm -v "$(CURDIR)/paper:/data" -u "$$(id -u):$$(id -g)" \
		$(INARA_IMAGE) -o pdf paper.md

# Builds the earlier Turkish article source (not the JOSS paper and not the
# submitted thesis). Its corrections are listed in thesis/ERRATA.md.
historical-article-pdf: figures
	cd thesis && tectonic thesis.tex
