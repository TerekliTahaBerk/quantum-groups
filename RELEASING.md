# Releasing

Checklist for a release of `quantum-group`, written for 1.1.1. Every step
names who does it: **maintainer** steps need the maintainer's GitHub, PyPI or
Zenodo login.

## 0. Before tagging (repository)

1. Version in `pyproject.toml`, `CITATION.cff` (`version`, `date-released`),
   the `CHANGELOG.md` heading and the release paragraph of `.zenodo.json`
   agree. If the release happens on a later day than the changelog date,
   change `date-released` and the changelog date first.
2. Locally: `make check` (tests and doctests), `make listings`,
   `make paper`, `make -C arxiv check`. All must pass.
3. The commit is pushed to `main` and every job of the `tests` workflow is
   green on it.

## 1. PyPI (maintainer)

GitHub → *Actions* → *publish* → *Run workflow*, with `ref` = the full
40-character SHA from step 0.3 and `expected_version` = `1.1.1`. Approve the
`pypi` environment when asked. The workflow builds, checks and test-installs
the wheel before uploading; afterwards <https://pypi.org/project/quantum-group/1.1.1/>
exists. (The trusted publisher was registered for 1.1.0 and is reused.)

## 2. GitHub Release → Zenodo (maintainer)

GitHub → *Releases* → *Draft a new release*: tag `v1.1.1` (create it on
publish), target = the same SHA, title `v1.1.1`, notes = the 1.1.1 section of
`CHANGELOG.md`. *Publish release*.

Zenodo's GitHub integration (already enabled for this repository, as for
1.1.0) then deposits the source archive as a **new version** of the existing
record, with the metadata of `.zenodo.json`. Wait a few minutes and open
<https://zenodo.org/records/23015576>: the *Versions* box lists v1.1.1 with
its own DOI. Check title, creator/ORCID, description, keywords, license and
that the file is about 3 MB.

Published Zenodo records cannot be deleted, and 1.1.0's DOI is cited, so
1.1.0 is **not** removed: it stays as the earlier version, and v1.1.1 becomes
the latest version under the same concept record. If 1.1.0's own metadata
should be improved, use *Edit* on that record (metadata only, no new files).

## 3. After the DOI exists (repository)

Send the new DOI to whoever maintains the manuscript, then in one commit on
`main`:

- `scipost/references.bib`, entry `quantumgroup111`: set
  `howpublished = {Zenodo}`, add `doi = {…}`, and keep only `Version 1.1.1`
  in `note` (drop the release URL); rebuild with `make paper` and
  `make -C arxiv bundle`;
- `CITATION.cff`: add the 1.1.1 DOI under `identifiers`;
- `README.md`, *Citation*: add the 1.1.1 DOI.

## 4. Preprint

- arXiv: upload `arxiv/arxiv_source.tar.gz` (from `make -C arxiv bundle`),
  primary category **math.QA** (the endorsement requested is for math.QA),
  cross-lists math-ph and cs.MS; comments: "21 pages, 1 figure. Code:
  https://github.com/TerekliTahaBerk/quantum-groups".
- Zenodo (optional, no endorsement needed): *New upload*, resource type
  *Publication → Preprint*, file `arxiv/paper.pdf`, license CC BY 4.0,
  related work of type *Documents* pointing to the software's 1.1.1 DOI.
