# Release, PyPI and Zenodo steps for version 1.1.0

Prepared 27 September 2026. **Nothing on this page has been executed.**
Every step below is irreversible or outward-facing (a tag, a GitHub
Release, a PyPI upload, a Zenodo DOI) and needs the author's explicit
decision. The JORS manuscript describes version **1.1.0**; the archive DOI,
PyPI release, Git tag, GitHub Release, `CITATION.cff`, `CHANGELOG.md` and the
Availability section of `jors/paper.tex` must all name that same version.

## 0. Before releasing

1. Review the full diff since `v1.0.0` (`git diff v1.0.0 origin/main`) and
   merge the branch carrying the JORS package into `main` once CI is green.
2. Decide what to do with the unmerged commit `33ae33c` on branch
   `claude/determined-maxwell-7u3h0j` (JOSS wording, `paper.bib` DOI for de
   Graaf 2001, removal of the v1.0.0 DOI from the 1.1.0 `CITATION.cff`).
   Its `CITATION.cff` change is required before releasing (step 2 below
   makes the same change if the branch is not merged).
3. Confirm in the Zenodo account (Settings → GitHub) that the toggle for
   `TerekliTahaBerk/quantum-groups` is still **on**; otherwise no DOI is
   minted for the release.

## 1. Configure PyPI Trusted Publishing (once)

The project name `quantum-group` returned HTTP 404 from both
`https://pypi.org/pypi/quantum-group/json` and the TestPyPI equivalent on
27 September 2026, i.e. no project of that name (or its normalized forms
`quantum_group`, `quantum.group`) exists. PyPI can still refuse a name at
first upload (e.g. prohibited or too similar to an existing one); only the
upload settles this.

1. Sign in to <https://pypi.org> (two-factor authentication is mandatory).
2. *Your account → Publishing → Add a new pending publisher → GitHub*:
   - PyPI project name: `quantum-group`
   - Owner: `TerekliTahaBerk`
   - Repository name: `quantum-groups`
   - Workflow name: `publish.yml`
   - Environment name: `pypi`
3. On GitHub: *Settings → Environments → New environment* `pypi`.
   Recommended: add yourself as a required reviewer, so that every upload
   waits for a manual approval.

No API token is created or stored anywhere.

## 2. Prepare the release commit

```sh
git switch main && git pull
# CHANGELOG.md: "## [1.1.0] - Unreleased" -> "## [1.1.0] - YYYY-MM-DD";
#   delete the "Prepared on main; not yet tagged ..." paragraph; update the
#   [1.1.0] compare link to .../compare/v1.0.0...v1.1.0
# CITATION.cff: add  date-released: "YYYY-MM-DD"; remove the v1.0.0 DOI
#   from identifiers (it does not archive 1.1.0)
python -m pytest                       # must pass
python -m build && python -m twine check --strict dist/*
git commit -am "Release 1.1.0"
git push origin main                   # wait for CI to pass on this commit
```

## 3. Tag and publish the GitHub Release

```sh
git tag -a v1.1.0 -m "quantum-group 1.1.0"
git push origin v1.1.0
```

Then on GitHub: *Releases → Draft a new release*, choose tag `v1.1.0`,
title `v1.1.0`, paste the 1.1.0 section of `CHANGELOG.md`, **Publish**.
Publishing the release triggers:

- Zenodo, which mints a new **version DOI** for the tagged code;
- `.github/workflows/publish.yml`, which rebuilds sdist and wheel, checks
  that the tag equals `v` + the `pyproject.toml` version, and uploads to PyPI
  (after the environment approval, if configured).

Never move or delete `v1.0.0` or its release; DOI 10.5281/zenodo.22997681
must keep pointing at the code it archives.

## 4. Verify, then record the identifiers

```sh
python -m venv /tmp/qg-check && . /tmp/qg-check/bin/activate
cd /tmp && python -m pip install quantum-group==1.1.0
python -c "import quantum_group; print(quantum_group.__version__)"   # 1.1.0
curl -sO https://raw.githubusercontent.com/TerekliTahaBerk/quantum-groups/v1.1.0/examples/sample_verification.py
curl -sO https://raw.githubusercontent.com/TerekliTahaBerk/quantum-groups/v1.1.0/examples/sample_verification_expected.txt
python sample_verification.py | diff - sample_verification_expected.txt && echo OK
```

Download the Zenodo archive and confirm it is the tagged code:

```sh
git archive --format=tar --prefix=x/ v1.1.0 | tar -x -C /tmp/from-git
# unzip the Zenodo file into /tmp/from-zenodo, then
diff -r /tmp/from-git/x /tmp/from-zenodo/<extracted-folder>
```

Then record the results (a documentation-only commit after the release):

- `CITATION.cff`: add the v1.1.0 version DOI under `identifiers`.
- `README.md` (Citation section): cite the v1.1.0 DOI; keep the note that
  10.5281/zenodo.22997681 archives v1.0.0.
- `jors/paper.tex`: fill *Persistent identifier*, *Date published* (archive
  and repository) and the PyPI identifier; remove the corresponding
  `\pending{}` markers; rebuild `jors/paper.pdf` (`latexmk -pdf paper.tex`).
- `jors/PREFLIGHT.md`: record the exact install command, the version it
  installed and the date.
- `jors/COVER_LETTER.md`: fill the DOI and PyPI lines.

If JORS review later leads to code changes, make a further release
(1.1.1 or 1.2.0) and give JORS that version's DOI; do not pair a new version
with the 1.1.0 DOI.
