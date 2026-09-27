# Cover letter (for the *Comments for the Editor* field)

> **STATUS: NOT SUBMITTABLE.** Do not paste this letter until every item in
> `SUBMISSION_CHECKLIST.md` marked HARD BLOCKER or AUTHOR CONFIRMATION
> REQUIRED is resolved, every `[bracketed]` field below is filled, and the
> declaration on consideration elsewhere has been re-checked on the day of
> submission. If a JOSS submission (or any other submission of this software
> paper) exists at that moment, **JORS submission is blocked** until that
> process has ended or been withdrawn.

---

Dear Editor,

I submit the manuscript **"quantum-group: Exact SymPy Verification of
Explicit U_q(sl_2) and GL_q(2|1) Matrix Identities"** for consideration as
a **Software Metapaper** in the *Journal of Open Research Software*.

**The software and its purpose.** `quantum-group` is a Python package for
verifying explicit matrix identities from the theory of quantum groups: the
defining relations and Hopf identities of U_q(sl_2) on finite-dimensional
modules, tensor products and Clebsch–Gordan vectors, the Yang–Baxter, braid,
Hecke and coproduct-intertwining identities of the fundamental R-matrix, and
the graded Yang–Baxter equation for the GL_q(2|1) R-matrix of Çelik and
Çelik (Rep. Math. Phys. 88, 2021). Every identity is returned as an exact
SymPy residual matrix, so that a failed check shows which entries, and hence
which convention, disagree.

**Why it is a substantive research-software contribution.** Published
quantum-group matrices are easy to misuse because the results depend on
basis order, tensor placement, the coproduct and graded sign rules; several
of these errors pass the usual Yang–Baxter test. The package fixes these
conventions in documented functions, provides both a historical and a
coproduct-compatible R-matrix API for reproducibility, encodes the Koszul
sign rule once for all tensor placements, and backs this with 202 automated
tests, including negative controls that require known wrong conventions to
fail. It was used to find a real convention error in the author's own
thesis. The paper claims no new mathematical results; the contribution is
the software and its verification method.

**Relation to existing software.** GAP's QuaGroup and SageMath are far
broader systems for quantized enveloping algebras of semisimple Lie
algebras. `quantum-group` does not replace them: it is a small, inspectable
verification layer for concrete matrix calculations in a given text's
conventions, including a graded example outside QuaGroup's documented scope.

**Availability.**
- Licence: MIT.
- Repository: https://github.com/TerekliTahaBerk/quantum-groups
- Version described: 1.1.0; archived at Zenodo, DOI **[v1.1.0 version DOI]**.
- Installation: `python -m pip install quantum-group` (PyPI, **[confirm
  published]**); also installable directly from GitHub.
- Quality control: `python -m pytest` runs 198 test cases and 4 doctests;
  continuous integration covers Python 3.10–3.13, the oldest supported
  dependency versions, wheel installation, and Linux, macOS and Windows
  **[re-check CI on the release commit]**. A sample script with its
  expected output is included in the paper and the repository.

**Reuse potential.** The residual and graded-embedding functions accept
arbitrary SymPy matrices and parity lists, so researchers can check R-matrix
transcriptions, determine which coproduct an R-matrix intertwines, turn
literature identities into regression tests, and apply the graded placement
machinery to other super vector spaces. The paper states where extensions
would require substantial new software.

**Prior publication and related manuscripts.** This manuscript has not been
published elsewhere, and it is not under consideration by any other journal
**[confirm on the day of submission]**. For transparency: (i) the software
was developed during my undergraduate thesis at Yıldız Technical University
(June 2026, in Turkish), which is cited in the manuscript; (ii) the public
repository also contains a separate draft software paper prepared for the
*Journal of Open Source Software* (`paper/paper.md`). That draft has **not
been submitted** to JOSS or any other venue **[confirm]**, and it will not be
submitted while this manuscript is under consideration at JORS
**[author's decision; confirm]**. The two
texts share facts about the same software but were written separately; the
JORS manuscript is organized around architecture, quality control,
availability and reuse.

**Competing interests.** **[After confirmation, e.g.: "The author has no
competing interests to declare."]**

**Funding.** **[After confirmation: funder and grant number, or "This work
received no specific funding."]**

**Use of generative AI.** In accordance with the Ubiquity Press policy, the
manuscript contains a section describing the use of generative AI tools
(Claude Code by Anthropic **[model/version]**, and Codex by OpenAI
**[model/version]**) in preparing the software release, its tests and
documentation, and in drafting this manuscript and its submission
materials. The tools are not authors. I reviewed and validated all
AI-assisted output and take full responsibility for the software and the
manuscript.

**Suggested reviewers.** **[Five names with institutional e-mail addresses,
chosen from POTENTIAL_REVIEWERS.md and verified on official pages.]** None
of them is at my institution, and none has collaborated with me or with my
thesis supervisor on this work **[confirm]**.

**Article processing charge.** **[Choose one: "I confirm that the APC will
be paid on acceptance." / "I request a waiver/discount because ..." / omit
until decided.]**

Thank you for considering this submission.

Yours sincerely,

Taha Berk Terekli
**[Current affiliation]**
ORCID: 0009-0004-8266-1116
terekli@tahaberk.com
