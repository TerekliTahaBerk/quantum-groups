"""MkDocs hook: reuse repository files in the documentation site.

The README, the changelog and the example scripts stay the single source of
their text. A page pulls them in with an HTML comment, which GitHub hides
when the page is read in the repository:

    <!-- include: README.md#Scope and limitations -->   one "## " section
    <!-- include: CHANGELOG.md -->                      a whole file
    <!-- include-code: examples/quickstart.py -->       a fenced code block

Relative links in a page or an included file are resolved against the
directory of the file they were written in. Links to other documentation
pages stay relative; links to anything else in the repository (source,
manuscripts, audit, ...) become GitHub URLs, so they work on the site too.
"""

from __future__ import annotations

import posixpath
import re
from pathlib import Path

REPO_URL = "https://github.com/TerekliTahaBerk/quantum-groups"
BRANCH = "main"
ROOT = Path(__file__).resolve().parents[2]
DOCS = "docs"

INCLUDE = re.compile(r"^<!-- include(-code)?: (\S+?)(?:#(.+?))? -->[ \t]*$", re.M)
LINK = re.compile(r"(\]\()([^)\s]+)(\))")
FENCE = re.compile(r"^(```|~~~)")


def _section(text: str, heading: str, path: str) -> str:
    lines = text.splitlines()
    try:
        start = lines.index(f"## {heading}")
    except ValueError:
        raise ValueError(f"{path}: no section '## {heading}'") from None
    end = next(
        (i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")),
        len(lines),
    )
    return "\n".join(lines[start + 1 : end]).strip("\n")


def _demote_headings(text: str) -> str:
    """Drop a top-level title and keep included headings below the page's."""
    out, in_fence = [], False
    for line in text.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
        elif not in_fence and line.startswith("# "):
            continue
        out.append(line)
    return "\n".join(out)


def _rewrite_links(text: str, page_dir: str, src_file: str | None = None) -> str:
    """Resolve the links of ``text`` for a page living in ``page_dir``.

    ``src_file`` is the included file the text comes from, or ``None`` for
    the page's own text. Paths are repository-relative POSIX paths.
    """
    src_dir = posixpath.dirname(src_file) if src_file else page_dir

    def fix(match: re.Match[str]) -> str:
        target = match.group(2)
        if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("/"):
            return match.group(0)
        path, _, anchor = target.partition("#")
        if not path:
            if src_file is None:
                return match.group(0)
            # An in-page anchor of an included file points into that file.
            path = posixpath.basename(src_file)
        repo_path = posixpath.normpath(posixpath.join(src_dir, path))
        suffix = f"#{anchor}" if anchor else ""
        site_page = repo_path.startswith(DOCS + "/") and repo_path.endswith(".md")
        if site_page and (ROOT / repo_path).is_file() and not repo_path.endswith("README.md"):
            rel = posixpath.relpath(repo_path, page_dir)
            return f"{match.group(1)}{rel}{suffix}{match.group(3)}"
        if repo_path == "docs":
            rel = posixpath.relpath(DOCS + "/index.md", page_dir)
            return f"{match.group(1)}{rel}{match.group(3)}"
        kind = "tree" if (ROOT / repo_path).is_dir() else "blob"
        url = f"{REPO_URL}/{kind}/{BRANCH}/{repo_path}"
        return f"{match.group(1)}{url}{suffix}{match.group(3)}"

    out, in_fence = [], False
    for line in text.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
        out.append(line if in_fence else LINK.sub(fix, line))
    return "\n".join(out)


def on_page_markdown(markdown, page, config, files):
    page_dir = posixpath.dirname(posixpath.join(DOCS, page.file.src_uri))

    def include(match: re.Match[str]) -> str:
        is_code, path, heading = match.group(1), match.group(2), match.group(3)
        text = (ROOT / path).read_text(encoding="utf-8")
        if is_code:
            lang = {".py": "python", ".g": "gap"}.get(Path(path).suffix, "text")
            return f"```{lang} title=\"{path}\"\n{text.rstrip()}\n```"
        if heading:
            text = _section(text, heading, path)
        return _rewrite_links(_demote_headings(text), page_dir, path)

    # Rewrite the page's own links before inserting included text, so that
    # each link is resolved against the file it was written in.
    pieces, last = [], 0
    for match in INCLUDE.finditer(markdown):
        pieces.append(_rewrite_links(markdown[last : match.start()], page_dir))
        pieces.append(include(match))
        last = match.end()
    pieces.append(_rewrite_links(markdown[last:], page_dir))
    return "".join(pieces)
