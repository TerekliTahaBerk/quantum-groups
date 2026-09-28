# JOSS paper and release notes (maintainer)

- `paper.md`, `paper.bib` — the JOSS manuscript (the only active manuscript).
- `PREFLIGHT.md` — current verification record and JOSS gate assessment.
- `REVIEW_CHANGES.md` — factual summary of changes since v1.0.0.
- `review-header.tex` — header for the optional plain-Pandoc reading copy.

## Building the paper

With Docker, the official JOSS toolchain (the `openjournals/inara` image
used by the editorial bot) builds `paper/paper.pdf`:

```sh
make joss-pdf
```

Generated PDFs are not committed (`paper/paper.pdf` is ignored), so a stale
copy cannot be mistaken for the current source. A plain Pandoc reading copy,
not JOSS typesetting, can be made with Pandoc ≥ 3 and XeLaTeX:

```sh
mkdir -p build && pandoc paper/paper.md --citeproc --bibliography paper/paper.bib \
  --pdf-engine=xelatex --include-in-header=paper/review-header.tex \
  -V geometry:margin=22mm -M author='Taha Berk Terekli' -o build/paper-preview.pdf
```

## Releases and Zenodo archiving

Zenodo's GitHub integration was used for `v1.0.0`: publishing that GitHub
release produced the version DOI
[10.5281/zenodo.22997681](https://doi.org/10.5281/zenodo.22997681)
(recorded by the author in commit `855cade`). That archive contains the code
at tag `v1.0.0` (commit `8dcfe99`) only. Before releasing, confirm in the
Zenodo account that the repository toggle is still on.

`main` carries version **1.1.0** (see `../CHANGELOG.md`), which has not been
released. To release it, after reviewing the diff since `v1.0.0`:

1. In `../CHANGELOG.md` replace "Unreleased" in the `[1.1.0]` heading with
   the release date; in `../CITATION.cff` add `date-released: YYYY-MM-DD`.
   Commit and wait for CI to pass on that commit.
2. Create an annotated tag `v1.1.0` on that commit and push it
   (`git tag -a v1.1.0 -m "v1.1.0" && git push origin v1.1.0`).
3. On GitHub, *Releases → Draft a new release*, select `v1.1.0`, paste the
   1.1.0 changelog section, and publish. (A tag alone does not trigger
   Zenodo.)
4. Zenodo mints a new version DOI within minutes. Add it to
   `CITATION.cff` under `identifiers` as the archive of that version (do not
   list the v1.0.0 DOI there, since the file describes the current version),
   and cite it in `README.md`. Note the concept DOI shown on the Zenodo
   record, which always resolves to the latest version.
5. Never move or delete the `v1.0.0` tag or release; its DOI must keep
   pointing at the code it archived.

JOSS asks for the archive DOI and version at the *end* of review. If review
leads to code changes, make a further release and give JOSS that version's
DOI.
