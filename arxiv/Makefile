# arXiv preprint in the AMS amsart layout, generated from ../scipost/paper.tex.
#   make          regenerate paper.tex and build paper.pdf
#   make check    build and run check.py
#   make bundle   write arxiv_source.tar.gz for upload to arXiv
PYTHON ?= python3

pdf:
	$(PYTHON) build.py
	pdflatex -interaction=nonstopmode -halt-on-error paper.tex
	bibtex paper
	pdflatex -interaction=nonstopmode -halt-on-error paper.tex
	pdflatex -interaction=nonstopmode -halt-on-error paper.tex

check: pdf
	$(PYTHON) check.py

# arXiv does not run BibTeX, so the generated .bbl is included.
bundle: check
	rm -f arxiv_source.tar.gz
	tar czf arxiv_source.tar.gz paper.tex paper.bbl references.bib figures/figure1_workflow.pdf
	$(PYTHON) check.py

clean:
	rm -f paper.aux paper.log paper.out paper.blg paper.toc

.PHONY: pdf check bundle clean
