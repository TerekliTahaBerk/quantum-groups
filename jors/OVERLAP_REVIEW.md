# Overlap review: JOSS draft (`paper/paper.md`) vs JORS metapaper (`jors/paper.tex`)

Checked 27 September 2026 on the texts in this commit. `paper/paper.md` was
not changed.

## Method

Both texts were reduced to lower-case word sequences (JOSS: Markdown body
without front matter; JORS: text extracted from `paper.pdf` up to the
reference list; inline mathematics replaced by a placeholder). Shared
word *n*-grams were counted, and every maximal shared run of at least eight
words was listed and read.

| Measure | Result |
|---|---|
| Length | JOSS ≈ 1,710 words; JORS ≈ 4,700 words |
| Shared 6-grams | 71 of 4,661 JORS 6-grams (1.5 %) |
| Shared 8-grams | 25 of 4,680 (0.5 %) |
| Shared 12-grams | 0 |

A first draft had 1.1 % shared 8-grams and 12 shared 12-grams; the closest
passages (AI-disclosure sentence, related-software capability list, scaling
sentence, scope sentence) were rewritten from scratch, not by synonym
substitution.

## Remaining shared runs (all ≥ 8 words) and assessment

| Shared run | Assessment |
|---|---|
| "the author thanks Prof. Dr. Salih Çelik for supervising the …" | Acknowledgement of the same fact; unavoidable and appropriate. |
| "R-matrix intertwines the opposite of the coproduct used in the text" | Precise statement of the thesis error; rewording would lose precision. Unavoidable factual overlap. |
| "checks the defining relations and generator-level Hopf identities" | Functional description of the same API. Unavoidable. |
| "noncommutative graded algebra … such as the Gauss decomposition of" | Technical reason for a scope limitation. Unavoidable. |
| "R-matrix and verifies the graded Yang–Baxter equation on three [factors]" | Functional description. Unavoidable. |
| "… grows exponentially. In the recorded benchmark (benchmarks/…" | Pointer to the same benchmark file. Acceptable. |
| "links each computational claim to its implementation and [tests]" | Description of `MANUSCRIPT_CODE_MAPPING.md`. Acceptable. |
| "are authored or co-authored by 'Claude' in the Git history" | Factual AI-disclosure statement; deliberately consistent with the JOSS disclosure. |
| "into English and with a mathematical and technical audit" | Factual AI-disclosure statement; must not contradict the JOSS text. |
| "the difference between the two sides of an identity" | Definition of the residual; standard phrasing. |
| "R_check_V1_coproduct and intertwining_residual_V1" | Function names. |
| "is not by itself a proof of inequality" | Precise technical caveat about `sympy.simplify`. Acceptable. |

No paragraph of the JORS text is close to a JOSS paragraph; no shared run
exceeds eleven words.

## Structural comparison

| JOSS draft (JOSS sections) | JORS metapaper (JORS template) |
|---|---|
| Summary (non-specialist) | Abstract with functionality, users, reuse and archive |
| Statement of need | Introduction: failure modes of explicit calculations, approach, provenance, intended users |
| State of the field, **comparison table**, build-vs-contribute argument | Short related-software paragraph without a table; positioning only |
| Software design: six trade-off paragraphs | Implementation and architecture: layered module structure, **Figure 1** workflow, one paragraph per design decision incl. validation and error behaviour, scaling with re-measured timings and memory |
| (tests mentioned in one sentence) | **Quality control**: CI matrix incl. macOS/Windows, **Table 1** evidence map, negative controls, independent re-derivations, **Listing 1** with expected output |
| — | **Availability**: OS, language, system requirements, dependencies (runtime vs optional vs build), contributors, archive/repository/registry fields |
| Research impact statement | **Reuse potential**: seven concrete reuse routes with the APIs to use, explicit boundary of easy vs substantial extension, integration, support |
| AI usage disclosure | Use of generative AI (same facts, independently written; model details pending author confirmation) |

## Material written specifically for JORS

- Figure 1 (original) and Table 1 (evidence map).
- Listing 1 and its expected output, backed by a CI comparison.
- The layered-architecture description, the validation/failure-mode
  paragraph, and re-measured scaling with memory.
- The Availability section in the JORS field format.
- The whole Reuse potential section.

## Consistency between the two texts

Facts that appear in both were checked to agree: coproduct formula, R-matrix
conventions, parities (0,0,1), page 261 of Çelik–Çelik, scope limitations,
AI tools used. The JORS text reports 202 tests (198 + 4 doctests), the
cross-platform CI job and re-measured timings, which postdate the JOSS
draft; the JOSS draft does not contradict them. If the JOSS draft is later
revised, keep these facts consistent.

## Reproducing

From the repository root, after building `jors/paper.pdf`:

```sh
pdftotext jors/paper.pdf /tmp/jors.txt
python3 - <<'PY'
import re
def words(t):
    t = re.sub(r'\$[^$]*\$', ' M ', t); t = re.sub(r'[`*_\\{}\[\]@;]', ' ', t)
    return re.findall(r"[a-z0-9'\-]+", t.lower())
A = words(open('paper/paper.md').read().split('---', 2)[2])
B = words(open('/tmp/jors.txt').read().split('References')[0])
for n in (6, 8, 12):
    ga = {tuple(A[i:i+n]) for i in range(len(A)-n)}
    gb = {tuple(B[i:i+n]) for i in range(len(B)-n)}
    print(n, len(ga & gb), 'of', len(gb))
PY
```
