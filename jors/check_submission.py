"""Consistency checks for the JORS manuscript (run from the repository root
or from jors/ via `make -C jors check`).

1. Listing 1 in paper.tex is identical to examples/sample_verification.py.
2. The printed output in paper.tex equals the expected-output file.
3. The rendered paper.pdf contains no [PENDING ...] marker (needs pdftotext).

Exit status 0 means the manuscript is complete in these respects.
"""
import pathlib
import subprocess
import sys

root = pathlib.Path(__file__).resolve().parent.parent
tex = (root / "jors" / "paper.tex").read_text(encoding="utf-8")
failures = []

start = "label={lst:example}, captionpos=b]\n"
listing = tex[tex.index(start) + len(start):tex.index("\\end{lstlisting}", tex.index(start))]
example = (root / "examples" / "sample_verification.py").read_text(encoding="utf-8")
body = example.split('"""', 2)[2].lstrip("\n")
if listing != body:
    failures.append("Listing 1 differs from examples/sample_verification.py")

start = "basicstyle=\\ttfamily\\small\\color{black!80}]\n"
printed = tex[tex.index(start) + len(start):tex.index("\\end{lstlisting}", tex.index(start))]
printed = printed.replace(",\n  (17, 25)", ", (17, 25)")
expected = (root / "examples" / "sample_verification_expected.txt").read_text(encoding="utf-8")
if printed != expected:
    failures.append("printed output differs from sample_verification_expected.txt")

text = subprocess.run(["pdftotext", str(root / "jors" / "paper.pdf"), "-"],
                      capture_output=True, text=True, check=True).stdout
pending = text.count("[PENDING")
if pending:
    failures.append(f"paper.pdf still shows {pending} [PENDING] marker(s)")

for failure in failures:
    print("FAIL:", failure)
print("OK" if not failures else f"{len(failures)} check(s) failed")
sys.exit(1 if failures else 0)
