#!/usr/bin/env python3
"""Menara UI repo checker (stdlib only). Exit 0 = clean, 1 = problems (one line each)."""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".superpowers", "tools", "superpowers"}
TEXT = {".html", ".css", ".js", ".md", ".svg", ".json", ".txt"}

FORBIDDEN = [
    (re.compile(r"(?<!\d)(?:08|628|\+628)\d{8,}(?!\d)"), "phone number"),
]
# Private words that must never ship (e.g. a client's brand). One per line, not committed.
_local = pathlib.Path(__file__).with_name("forbidden.local.txt")
if _local.exists():
    for w in _local.read_text().split("\n"):
        if w.strip() and not w.startswith("#"):
            FORBIDDEN.append((re.compile(re.escape(w.strip()).replace("\\ ", r"\s?"), re.I), "private word"))
ALLOWED_EXTERNAL = ("https://fonts.googleapis.com", "https://fonts.gstatic.com", "https://github.com/armandawahyuu/menara-ui",
                    "https://armandawahyuu.github.io/menara-ui", "https://lucide.dev", "https://fonts.google.com", "https://opensource.org")

problems = []


def files():
    for p in ROOT.rglob("*"):
        if p.is_file() and not (set(p.relative_to(ROOT).parts) & SKIP_DIRS) and p.suffix in TEXT:
            yield p


def rel(p):
    return p.relative_to(ROOT).as_posix()


for f in files():
    text = f.read_text(encoding="utf-8", errors="replace")
    for rx, label in FORBIDDEN:
        m = rx.search(text)
        if m:
            problems.append(f"{rel(f)}: forbidden {label}: {m.group(0)!r}")

    if f.suffix == ".html":
        if '<html lang="en"' not in text:
            problems.append(f"{rel(f)}: missing <html lang=\"en\">")
        if 'name="viewport"' not in text:
            problems.append(f"{rel(f)}: missing viewport meta")
        if not re.search(r"<title>[^<]+</title>", text):
            problems.append(f"{rel(f)}: missing <title>")
        if "data-mn-theme-init" not in text:
            problems.append(f"{rel(f)}: missing theme-init snippet")
        for m in re.finditer(r'<script\s+src="([^"]+)"', text):
            if not m.group(1).endswith("js/menara.js"):
                problems.append(f"{rel(f)}: external/extra script {m.group(1)}")
        for m in re.finditer(r'(?:href|src)="([^"#][^"]*)"', text):
            url = m.group(1)
            if url.startswith(("mailto:", "tel:", "data:", "javascript:")):
                continue
            if url.startswith("http"):
                if not url.startswith(ALLOWED_EXTERNAL):
                    problems.append(f"{rel(f)}: external link {url}")
                continue
            if url.startswith("/"):
                problems.append(f"{rel(f)}: absolute path {url}")
                continue
            target = (f.parent / url.split("#")[0].split("?")[0]).resolve()
            if not target.exists():
                problems.append(f"{rel(f)}: broken link {url}")

css = ROOT / "css" / "menara.css"
if css.exists():
    body = re.sub(r"/\*.*?\*/", "", css.read_text(), flags=re.S)
    for m in re.finditer(r"#[0-9a-fA-F]{3,8}\b|\brgba?\(\s*\d", body):
        problems.append(f"css/menara.css: color literal {m.group(0)} (use tokens)")
        break

# Skill docs may only name classes, tokens and data-attributes that really exist.
if css.exists():
    known = "".join(p.read_text() for p in (css, ROOT / "css" / "tokens.css", ROOT / "js" / "menara.js") if p.exists())
    pages_html = "".join(p.read_text() for p in ROOT.rglob("*.html") if not (set(p.relative_to(ROOT).parts) & SKIP_DIRS))
    names = (set(re.findall(r"\.(mn-[a-z0-9-]+)", known)) | set(re.findall(r"--(mn-[a-z0-9-]+)", known))
             | set(re.findall(r"data-(mn-[a-z0-9-]+)", known + pages_html)) | set(re.findall(r"'(mn-[a-z0-9-]+)'", known)))
    for md in (ROOT / "skills").rglob("*.md"):
        for c in sorted(set(re.findall(r"(?<![\w-])-{0,2}(?:data-)?(mn-[a-z0-9-]+)", md.read_text()))):
            if c not in names and not c.endswith("-"):  # "--mn-sidebar-*" style wildcards
                problems.append(f"{rel(md)}: unknown class/token {c}")

for line in problems:
    print(line)
print(f"check: {len(problems)} problem(s)")
sys.exit(1 if problems else 0)
