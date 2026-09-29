# SciPost Physics Codebases submission (run from scipost/ or `make -C scipost`).
pdf:
	pdflatex -interaction=nonstopmode -halt-on-error paper.tex
	bibtex paper
	pdflatex -interaction=nonstopmode -halt-on-error paper.tex
	pdflatex -interaction=nonstopmode -halt-on-error paper.tex

check: pdf
	python3 check_submission.py

# Source bundle of the SciPost-format manuscript (TeX, class, bst, generated
# .bbl, figure), e.g. for SciPost's production stage. The arXiv preprint in
# the amsart layout is built separately in ../arxiv/.
source: pdf
	rm -f scipost_source.tar.gz
	tar czf scipost_source.tar.gz paper.tex paper.bbl SciPost.cls SciPost_bibstyle.bst references.bib figures/figure1_workflow.pdf

clean:
	rm -f paper.aux paper.log paper.out paper.toc paper.blg

.PHONY: pdf check source clean
