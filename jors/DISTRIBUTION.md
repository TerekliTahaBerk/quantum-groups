# Distribution of version 1.1.0

**Updated 28 September 2026: the author reversed the earlier "no release"
decision.** `v1.1.0` is now a published GitHub Release, target `main`,
commit `103d5384e70e8b0b746b296a0bdbd2d156ba8dde` (`103d538`) — the same
commit this file called the JORS submission software snapshot before this
update (previously `892dfae`; package source trees are identical between
the two, only documentation changed, see `PREFLIGHT.md` §1). The historical
`v1.0.0` tag and release stay untouched. A stray `v1.0.1` tag on the same
commit (from a first, misnamed release attempt) should be deleted. Version
1.1.0 is distributed from the `v1.1.0` release commit through:

| Channel | Mechanism | Why |
|---|---|---|
| PyPI `quantum-group==1.1.0` | `.github/workflows/publish.yml`, started by hand with the snapshot SHA; Trusted Publishing (OIDC), no stored token; waits for approval of the `pypi` environment | JORS: "easy to install and supports versioning", which for Python means a package registry |
| Zenodo software deposit | Manual upload of `git archive` of the snapshot commit (no GitHub integration involved) | JORS: the described version must be in a repository that provides a persistent identifier for that version; see `PREFLIGHT.md` §4 |
| GitHub | The repository and the snapshot commit URL | Development, issues, support |

**Update, 28 September 2026: sections A, B, C and D are all complete.**
PyPI and Zenodo publication (steps 7 and 9–11) have both been carried out
and independently verified; only step 12 (download-and-diff the published
Zenodo archive) and step 14 (set `date-released`/`CHANGELOG.md` to the PyPI
date) remain as author follow-ups. Each numbered step below says who does
it; steps already done are marked inline.

## Frozen snapshot

| Field | Value |
|---|---|
| Snapshot commit | `103d5384e70e8b0b746b296a0bdbd2d156ba8dde` (short `103d538`), 2026-09-28T14:13:05+03:00, branch `main` — **= the `v1.1.0` GitHub Release commit** |
| Package version | 1.1.0 |
| Package source trees | `quantum_group/` `804d66f83a1d`, `tests/` `a2a4fdc80bf4`, `pyproject.toml` `b17aa2bbc012` — identical to the earlier `892dfae` snapshot; only `jors/` and `paper/` documentation changed since (Codex-attribution correction) |
| Tests | 202 passed (198 + 4 doctests) |
| Python | 3.10, 3.11, 3.12, 3.13 |
| Tested OS | Linux, macOS, Windows (CI; all 9 jobs green on `103d538`) |
| Dependencies | SymPy ≥ 1.10, NetworkX ≥ 2.6, Matplotlib ≥ 3.5 |
| Archive file | `git archive --format=zip --prefix=quantum-group-1.1.0/ 103d538…` → `quantum-group-1.1.0.zip`, 236 files, 13,011,364 bytes, SHA-256 `47433ae4feef57f81daf2c219fd4051dd60a04435aed38a5ba8b3a5b77cd5c1d` (git 2.43.0; other git versions may produce a different zip checksum but identical contents — verify contents with step 12). This is also exactly what GitHub's own "Source code (zip)" asset on the `v1.1.0` Release contains, modulo GitHub's own zip wrapper differences — prefer `git archive` for a reproducible, documented hash. |

Steps 5–6 below are therefore done: the reserved DOI does **not** need to be
inside the snapshot (the Zenodo record carries it); after publication it is
added to `CITATION.cff` on `main` in a documentation-only commit.

## A. Author, once (can be done in parallel)

1. **PyPI pending publisher** — <https://pypi.org> → *Account → Publishing →
   Add a new pending publisher → GitHub*:
   project `quantum-group`, owner `TerekliTahaBerk`, repository
   `quantum-groups`, workflow `publish.yml`, environment `pypi`.
2. **GitHub environment** — repository *Settings → Environments → New
   environment* `pypi`; add yourself as *required reviewer*.
3. **Zenodo draft with a reserved DOI** — preferred: open the existing
   v1.0.0 record (<https://doi.org/10.5281/zenodo.22997681>) and choose
   *New version*; this creates a draft under the same concept DOI without
   involving GitHub (remove the v1.0.0 files from the draft). Alternative:
   *New upload* with resource type *Software*. In either case reserve the
   DOI (*Get a DOI now!* / *Reserve DOI*) and do **not** publish yet. Send
   the reserved DOI back. The `isNewVersionOf` relation in
   `zenodo-metadata.json` is only needed for the alternative route.
4. ~~**Merge** the branch carrying this package into `main`~~ — **done**
   (PR #8, 28 Sep 2026); `main` now carries the JORS package and the
   Codex-attribution correction, and the `v1.1.0` GitHub Release exists.

## B. Freeze the snapshot (Claude or author)

5. *(Done differently: snapshot frozen as above without the DOI.)* Put
   the DOI into `CITATION.cff` (`identifiers`) and the README citation
   section after publication; commit on `main`. The package source
   (`quantum_group/`, `pyproject.toml`) must be unchanged from the reviewed
   state. Wait for CI to pass on this commit on all jobs (Python 3.10–3.13,
   minimum dependencies, wheel, Linux/macOS/Windows).
6. Record that commit as the snapshot: full SHA, date
   (`git show -s --format=%cI <SHA>`), in `jors/PREFLIGHT.md`.

## C. Publish to PyPI (author approval required) — **done, 28 Sep 2026**

7. *Actions → publish → Run workflow* on `main`, inputs
   `ref = <full snapshot SHA>`, `expected_version = 1.1.0`.
   The build job refuses to continue unless the SHA is a full 40-character
   SHA and `pyproject.toml` says 1.1.0; it builds, runs
   `twine check --strict`, installs the wheel in a clean environment, runs
   both examples and diffs the sample output. Then approve the `pypi`
   environment to upload. The job summary artifact `dist` contains
   `dist-provenance.txt` (commit, version, SHA-256 of both files).
8. Verify from a clean environment and record the output in
   `jors/PREFLIGHT.md`:

   ```sh
   python -m venv /tmp/qg && cd /tmp
   /tmp/qg/bin/python -m pip install quantum-group==1.1.0
   /tmp/qg/bin/python -c "import quantum_group; print(quantum_group.__version__)"
   curl -sO https://raw.githubusercontent.com/TerekliTahaBerk/quantum-groups/<SHA>/examples/sample_verification.py
   curl -sO https://raw.githubusercontent.com/TerekliTahaBerk/quantum-groups/<SHA>/examples/sample_verification_expected.txt
   /tmp/qg/bin/python sample_verification.py | diff - sample_verification_expected.txt && echo OK
   ```

   **Done and recorded** (`jors/PREFLIGHT.md`): install succeeds,
   `__version__ == 1.1.0`, sample output matches byte for byte.

PyPI versions are immutable. If package code changes after this, it needs a
new version number; manuscript-only edits do not.

## D. Archive on Zenodo (author approval required) — **done, 28 Sep 2026**

9. Create the archive from the exact snapshot commit (`jors/` is excluded
   by `.gitattributes` because it holds submission paperwork, not software):

   ```sh
   git archive --format=zip --prefix=quantum-group-1.1.0/ <SHA> > quantum-group-1.1.0.zip
   sha256sum quantum-group-1.1.0.zip
   ```

10. Upload the zip to the Zenodo draft of step 3 and fill the metadata from
    `jors/zenodo-metadata.json` (title, creator with ORCID and affiliation,
    description, version `1.1.0`, licence MIT, keywords, related
    identifiers: the repository and the snapshot commit URL
    `https://github.com/TerekliTahaBerk/quantum-groups/tree/<SHA>`).
11. **Publish** the deposit (irreversible; needs the author's approval).
    **Done:** published as DOI
    [10.5281/zenodo.23015576](https://doi.org/10.5281/zenodo.23015576).
12. Download the published zip and verify (**not yet done** — recommended
    before submission, not strictly blocking since the upload was made
    directly from the recorded archive):

    ```sh
    sha256sum downloaded.zip        # equals the value from step 9
    mkdir a b && unzip -q downloaded.zip -d a && git archive <SHA> | tar -x -C b
    diff -r a/quantum-group-1.1.0 b && echo IDENTICAL
    ```

## E. Complete the manuscript (Claude or author) — **done, 28 Sep 2026**

13. Fill `jors/submission-facts.tex`: `\SnapshotSHA`, `\SnapshotDate`,
    `\ArchiveDOI`, `\ArchiveDate`, `\PyPIIdentifier` (and the author
    declarations). Run `make -C jors check`; it must print `OK`.
    **Done:** all fields filled, `make -C jors check` prints `OK`.
14. Set `date-released` in `CITATION.cff` and the date in `CHANGELOG.md` to
    the PyPI publication date. **Done:** both set to 2026-09-28.

## Guard rails

- Never attach the v1.0.0 DOI (10.5281/zenodo.22997681) to 1.1.0.
- Never archive a moving branch; always the recorded SHA (`103d538`, = the
  `v1.1.0` tag).
- A stray `v1.0.1` tag was suspected (same commit as `v1.1.0`, from a first,
  misnamed release attempt); re-checked 28 Sep 2026 via `git ls-remote
  --tags origin` — it does not exist on the remote. Nothing to delete.
- PyPI's `workflow_dispatch` `ref` input should still be the full 40-character
  commit SHA, not the tag name, per the workflow's own validation.
