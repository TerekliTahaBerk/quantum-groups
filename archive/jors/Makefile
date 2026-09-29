pdf:
	latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex

check: pdf
	python3 check_submission.py

clean:
	latexmk -c paper.tex
	rm -f paper.bbl paper.run.xml

.PHONY: pdf check clean
