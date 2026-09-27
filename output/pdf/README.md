# Local manuscript reading copy

`quantum-group-review.pdf` was rendered from `paper/paper.md` and
`paper/paper.bib` with Pandoc 3.9, citeproc and XeLaTeX. It is **not** the
official JOSS/Inara output. All three pages were rendered to images and
visually checked. The footer identifies the preview on every page.

From the repository root, with XeLaTeX on PATH:

```sh
pandoc paper/paper.md --from markdown --citeproc \
  --bibliography paper/paper.bib --pdf-engine=xelatex \
  --include-in-header=paper/review-header.tex \
  -V geometry:margin=22mm -V papersize=a4 \
  -V mainfont='Times New Roman' -V monofont=Menlo -V fontsize=10pt \
  -M author='Taha Berk Terekli' -o output/pdf/quantum-group-review.pdf
```

The fonts are local preview choices. Journal-specific author affiliation and
ORCID metadata remain in the manuscript YAML for the official JOSS build.
