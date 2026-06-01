.PHONY: test figures pdf demo all

test:
	python3 -m pytest tests/ -q

figures:
	python3 thesis/figures/generate_figures.py

pdf: figures
	tectonic thesis/thesis.tex
	mv thesis/thesis.pdf "thesis/Quantum Grup Yapılarının Python Ortamında Modellenmesi.pdf"

demo:
	python3 main.py

all: test pdf demo
