# JOSS paper and release notes (maintainer)

This directory holds the JOSS submission (`paper.md`, `paper.bib`) and the
pre-submission checklist (`PREFLIGHT.md`).

## Zenodo archiving: manual steps

These steps are done in the GitHub and Zenodo web interfaces; no code in this
repository can perform them.

1. **Connect GitHub to Zenodo.** Sign in at <https://zenodo.org> with the
   GitHub account that owns the repository. Open *Account → GitHub* and switch
   `TerekliTahaBerk/quantum-groups` **On**. If the repository is not listed,
   use *Sync now*.
2. **Complete the citation metadata first.** Zenodo builds the record from
   `CITATION.cff` when there is no `.zenodo.json`. Before releasing, add
   `date-released: YYYY-MM-DD` and check authors, ORCID, license and
   version (`1.0.0`).
3. **Create a GitHub Release.** Pushing a tag alone does **not** trigger
   Zenodo. After the `v1.0.0` tag is on GitHub, open *Releases → Draft a new
   release*, select `v1.0.0` and publish it. Zenodo then archives the
   release and mints a DOI within a few minutes.
4. **Record the DOI.** Zenodo issues two DOIs:
   - a **version DOI** (this exact release), which is the one JOSS asks for;
   - a **concept DOI** (always resolves to the latest version), which suits
     a README badge.

   Add the DOI to `CITATION.cff` (`doi:` or `identifiers:`) and a badge to
   `README.md`.
5. **JOSS timing.** JOSS asks for the archive DOI and the release version at
   the *end* of review, when the paper is accepted. If review leads to code
   changes, make a new release (e.g. `v1.0.1`) and give JOSS that version's
   DOI.
