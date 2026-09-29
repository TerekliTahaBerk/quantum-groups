"""Consistency checks for the SciPost Physics Codebases manuscript
(run from scipost/ via `make check`, or from the repository root).

1. Every code listing in paper.tex is identical to the script it names.
2. Every printed output in paper.tex equals the stored expected output
   (compared with whitespace runs collapsed, because long lines are wrapped
   in the paper).
3. Every script, run afresh against the installed package, reproduces its
   stored expected output exactly.
4. The LaTeX log shows no undefined references/citations and no overfull
   boxes, and the BibTeX run produced no warnings.
5. Every bibliography entry carries a DOI or a URL in a field the SciPost
   style actually prints (SciPost requires all references to be externally
   linked), and the cited keys equal the bibliography keys.
6. Every reference in the rendered bibliography shows a link (doi: or a URL).

Exit status 0 means the manuscript passes these checks.
"""
import pathlib
import re
import subprocess
import sys

here = pathlib.Path(__file__).resolve().parent
root = here.parent
tex = (here / "paper.tex").read_text(encoding="utf-8")
failures = []

# listing label -> (script, expected output)
pairs = {
    "lst:example": ("examples/sample_verification.py",
                    "examples/sample_verification_expected.txt"),
    "lst:coproduct": ("scipost/examples/coproduct_check.py",
                      "scipost/examples/coproduct_check_expected.txt"),
    "lst:typo": ("scipost/examples/transcription_check.py",
                 "scipost/examples/transcription_check_expected.txt"),
    "lst:cg": ("scipost/examples/clebsch_gordan.py",
               "scipost/examples/clebsch_gordan_expected.txt"),
    "lst:graded4": ("scipost/examples/graded_four_factors.py",
                    "scipost/examples/graded_four_factors_expected.txt"),
    "lst:crosscheck": ("scipost/crosscheck/quagroup_crosscheck.py",
                       "scipost/crosscheck/quagroup_crosscheck_expected.txt"),
}


def squash(text):
    return " ".join(text.split())


for label, (script, expected) in pairs.items():
    start = tex.index("label={%s}]\n" % label)
    code_start = tex.index("\n", start) + 1
    code_end = tex.index("\\end{lstlisting}", code_start)
    listing = tex[code_start:code_end]
    body = (root / script).read_text(encoding="utf-8").split('"""', 2)[2].lstrip("\n")
    if listing != body:
        failures.append(f"{label}: listing differs from {script}")
    out_start = tex.index("\\begin{lstlisting}[style=output]\n", code_end)
    out_start = tex.index("\n", out_start) + 1
    printed = tex[out_start:tex.index("\\end{lstlisting}", out_start)]
    stored = (root / expected).read_text(encoding="utf-8")
    if squash(printed) != squash(stored):
        failures.append(f"{label}: printed output differs from {expected}")
    fresh = subprocess.run([sys.executable, str(root / script)], cwd="/",
                           capture_output=True, text=True, check=True).stdout
    if fresh != stored:
        failures.append(f"{label}: fresh run of {script} differs from {expected}")

log = (here / "paper.log").read_text(encoding="latin-1")
for pattern, what in [(r"undefined", "undefined reference or citation"),
                      (r"Rerun to get", "cross-references not settled"),
                      (r"^! ", "LaTeX error")]:
    if re.search(pattern, log, re.M):
        failures.append(f"paper.log reports: {what}")
# The copyright placeholder block is supplied by SciPost and must not be
# modified by authors; it produces an overfull box in the unmodified template
# too, so boxes inside it are ignored. Any other overfull box fails.
lines = tex.splitlines()
marks = [i + 1 for i, line in enumerate(lines) if "BLOCK: Copyright information" in line]
block = range(marks[0], marks[-1] + 1)
for first, last in re.findall(r"Overfull \\hbox .* at lines (\d+)--(\d+)", log):
    if not (int(first) in block and int(last) in block):
        failures.append(f"overfull box at paper.tex lines {first}--{last}")
# Display equations are reported as "Overfull \hbox (...) detected at line N".
for line in re.findall(r"Overfull \\hbox .* detected at line (\d+)", log):
    if int(line) not in block:
        failures.append(f"overfull display at paper.tex line {line}")
blg = (here / "paper.blg").read_text(encoding="latin-1")
if "Warning" in blg or "error" in blg.lower().replace("error message", ""):
    failures.append("paper.blg reports BibTeX warnings or errors")

bib = (here / "references.bib").read_text(encoding="utf-8")
for entry in re.split(r"\n@", bib)[1:]:
    key = entry[entry.index("{") + 1:entry.index(",")]
    # The SciPost style prints `doi` and `note`/`howpublished`/`eprint`, but
    # not `url`, so a link must be in one of the printed fields.
    if not (re.search(r"^\s*doi\s*=", entry, re.M)
            or re.search(r"^\s*(note|howpublished|eprint)\s*=\s*\{[^\n]*\\url\{", entry, re.M)):
        failures.append(f"reference {key} has no printed DOI or URL")
cited = set()
for group in re.findall(r"\\cite\{([^}]*)\}", tex):
    cited.update(k.strip() for k in group.split(","))
keys = set(re.findall(r"^@\w+\{([^,]+),", bib, re.M))
if cited != keys:
    failures.append(f"cited vs bib mismatch: uncited={sorted(keys - cited)}, missing={sorted(cited - keys)}")

text = subprocess.run(["pdftotext", "-layout", str(here / "paper.pdf"), "-"],
                      capture_output=True, text=True, check=True).stdout
refs = text[text.rindex("References"):]
items = re.split(r"\n\s*(?:\d+\s+)?\[(\d+)\]\s", refs)[1:]  # line numbers precede items
numbers = [int(n) for n in items[0::2]]
if numbers != list(range(1, len(keys) + 1)):
    failures.append(f"rendered bibliography numbering is {numbers}")
for number, body in zip(items[0::2], items[1::2]):
    if "doi:" not in body and "http" not in body:
        failures.append(f"rendered reference [{number}] shows no link")

for failure in failures:
    print("FAIL:", failure)
print("OK" if not failures else f"{len(failures)} check(s) failed")
sys.exit(1 if failures else 0)
