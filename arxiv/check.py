"""Checks for the arXiv preprint (run by `make -C arxiv check`).

1. arxiv/paper.tex and arxiv/references.bib are exactly what build.py
   generates from scipost/ (so the preprint cannot drift from the userguide,
   whose listings and outputs are checked by scipost/check_submission.py).
2. The LaTeX log shows no undefined references or citations, no unsettled
   cross-references, no LaTeX errors and no overfull boxes; BibTeX gave no
   warnings.
3. Every entry of the rendered bibliography carries a link (DOI or URL).
4. The source bundle for arXiv, if present, compiles on its own with
   pdflatex only (arXiv does not run BibTeX) and gives the same page count.

Exit status 0 means all checks pass.
"""
import pathlib
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile

here = pathlib.Path(__file__).resolve().parent
failures = []

generated = ["paper.tex", "references.bib"]
before = {name: (here / name).read_bytes() for name in generated}
subprocess.run([sys.executable, str(here / "build.py")], check=True, capture_output=True)
for name in generated:
    if (here / name).read_bytes() != before[name]:
        failures.append(f"{name} was out of date with scipost/ (regenerated now; rebuild and rerun)")

log = (here / "paper.log").read_text(encoding="latin-1")
for pattern, what in [(r"undefined", "undefined reference or citation"),
                      (r"Rerun to get", "cross-references not settled"),
                      (r"^! ", "LaTeX error"),
                      (r"^Overfull", "overfull box")]:
    if re.search(pattern, log, re.M):
        failures.append(f"paper.log reports: {what}")
blg = (here / "paper.blg").read_text(encoding="latin-1")
if re.search(r"^Warning--", blg, re.M):
    failures.append("BibTeX warnings in paper.blg")

bbl = (here / "paper.bbl").read_text(encoding="utf-8")
items = re.split(r"\\bibitem", bbl)[1:]
for item in items:
    key = re.match(r"\{([^}]*)\}", item).group(1)
    if "\\doi{" not in item and "\\url{" not in item:
        failures.append(f"reference {key} has no printed DOI or URL")
cited = set()
for group in re.findall(r"\\cite\{([^}]*)\}", (here / "paper.tex").read_text(encoding="utf-8")):
    cited.update(k.strip() for k in group.split(","))
if cited != {re.match(r"\{([^}]*)\}", i).group(1) for i in items}:
    failures.append("cited keys differ from bibliography entries")

bundle = here / "arxiv_source.tar.gz"
if bundle.exists():
    pages = re.search(r"Output written on paper\.pdf \((\d+) pages", log).group(1)
    with tempfile.TemporaryDirectory() as tmp:
        with tarfile.open(bundle) as tar:
            tar.extractall(tmp)
        for _ in range(3):
            run = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "paper.tex"],
                                 cwd=tmp, capture_output=True, text=True)
        tlog = pathlib.Path(tmp, "paper.log").read_text(encoding="latin-1")
        m = re.search(r"Output written on paper\.pdf \((\d+) pages", tlog)
        if run.returncode or not m or m.group(1) != pages:
            failures.append("arxiv_source.tar.gz does not compile to the same PDF on its own")
        elif re.search(r"undefined|^Overfull", tlog, re.M):
            failures.append("arxiv_source.tar.gz compiles with warnings")

if failures:
    print("FAILED:")
    for f in failures:
        print("  -", f)
    sys.exit(1)
print(f"OK ({len(items)} references, all linked)")
