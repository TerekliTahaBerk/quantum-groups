# Releasing quantum-group

Current released version: **1.1.1** (29 September 2026).
The paper is published as [arXiv:2610.07867](https://arxiv.org/abs/2610.07867),
DOI [10.48550/arXiv.2610.07867](https://doi.org/10.48550/arXiv.2610.07867).
A paper revision and a software release have separate identifiers.
Documentation updates alone do not republish the existing PyPI version.

## Prepare a software release

1. Choose a new version following the existing Semantic Versioning policy.
   Update `pyproject.toml`, `quantum_group.__version__`, `CITATION.cff`
   (`version`, `date-released`), the changelog and the release description
   in `.zenodo.json`. Update installation examples and software citations
   to match. Preserve identifiers for previously published versions.
2. Run `make check`, `make quickstart`, `make listings`, `make paper` and
   `make -C arxiv check`. Validate `CITATION.cff` with `cffconvert --validate`.
   Build distributions with `python -m build` and check them with
   `python -m twine check --strict dist/*` in a clean output directory.
3. Push the release commit and verify that every job of the `tests`
   workflow passes. Record its full 40-character SHA.

## Publish to PyPI

The maintainer runs **Actions → publish → Run workflow**, setting `ref`
to the verified SHA and `expected_version` to the new version. Approve
the `pypi` environment when prompted. The workflow builds and validates
distributions, tests the installed wheel and uses Trusted Publishing.
Check the resulting version on [PyPI](https://pypi.org/project/quantum-group/).
Never reuse a published version number for different files.

## Create the GitHub release and Zenodo archive

Create tag `vX.Y.Z` on the same verified commit and publish a GitHub release
with the corresponding changelog entry. The configured Zenodo integration
archives it as a new software version. Verify the deposited files, version,
author/ORCID, license and paper relationship before recording the new DOI.
Existing archives remain available for reproducibility.

After the DOI is registered, update the software DOI in `CITATION.cff`,
`CITATION.bib`, the README and manuscript software references. Rebuild both
manuscript layouts if their references change. Keep the arXiv paper DOI
as `preferred-citation`; `.zenodo.json` links the software to that paper
using `isDocumentedBy`.

## Update the arXiv paper

Edit the manuscript in `scipost/`, then run `make paper` and
`make -C arxiv bundle`. Upload `arxiv/arxiv_source.tar.gz` as a replacement
for **2610.07867**. The existing record has primary category **math.QA** and
cross-list **cs.MS**. Do not create a new arXiv record for a revision.
After publication, check the version and update any version-specific links
and reproduction instructions. The unversioned arXiv DOI remains the paper
identifier.

The earlier Zenodo preprint
[10.5281/zenodo.23040093](https://doi.org/10.5281/zenodo.23040093) is a
separate manuscript archive. It is not the software DOI.

## Existing archives

| Resource | Identifier |
| --- | --- |
| Software 1.1.1 | [10.5281/zenodo.23039671](https://doi.org/10.5281/zenodo.23039671) |
| Software 1.1.0 | [10.5281/zenodo.23015576](https://doi.org/10.5281/zenodo.23015576) |
| Software 1.0.0 | [10.5281/zenodo.22997681](https://doi.org/10.5281/zenodo.22997681) |
| Paper | [10.48550/arXiv.2610.07867](https://doi.org/10.48550/arXiv.2610.07867) |
