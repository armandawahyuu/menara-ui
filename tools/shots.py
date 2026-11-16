#!/usr/bin/env python3
"""Screenshot every page at 360px and 1280px in light and dark, and fail on horizontal overflow.

Dev-only. Needs `pip install playwright` and Google Chrome (uses channel="chrome").
    python3 tools/shots.py            # all pages → tools/out/
    python3 tools/shots.py admin/index.html store/index.html
"""
import pathlib
import sys

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "tools" / "out"
SKIP = {"docs/superpowers"}


def pages(args):
    if args:
        return [ROOT / a for a in args]
    return sorted(p for p in ROOT.rglob("*.html")
                  if not any(s in p.relative_to(ROOT).as_posix() for s in SKIP) and "tools" not in p.parts)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    failures = 0
    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel="chrome")
        for theme in ("light", "dark"):
            for width in (360, 1280):
                ctx = browser.new_context(viewport={"width": width, "height": 900}, device_scale_factor=1,
                                          color_scheme=theme, reduced_motion="reduce")
                page = ctx.new_page()
                errors = []
                page.on("pageerror", lambda e: errors.append(str(e)))
                for f in pages(sys.argv[1:]):
                    rel = f.relative_to(ROOT).as_posix()
                    errors.clear()
                    page.goto(f.as_uri())
                    page.wait_for_timeout(250)
                    over = page.evaluate("""() => {
                        const w = document.documentElement.clientWidth;
                        const bad = [...document.querySelectorAll('body *')].filter(el => {
                          const r = el.getBoundingClientRect();
                          if (!r.width || getComputedStyle(el).position === 'fixed') return false;
                          let p = el.parentElement;  // ignore content inside horizontal scrollers
                          while (p) { const o = getComputedStyle(p).overflowX; if (o === 'auto' || o === 'scroll' || o === 'hidden') return false; p = p.parentElement; }
                          return r.right > w + 1;
                        }).slice(0, 3).map(el => el.tagName.toLowerCase() + '.' + [...el.classList].join('.'));
                        return {scroll: document.documentElement.scrollWidth > w, bad};
                    }""")
                    name = rel.replace("/", "__").replace(".html", "")
                    page.screenshot(path=str(OUT / f"{name}-{width}-{theme}.png"), full_page=True)
                    ok = not over["scroll"] and not over["bad"] and not errors
                    failures += not ok
                    status = "ok" if ok else f"FAIL overflow={over['scroll']} {over['bad']} js={errors}"
                    print(f"{rel:28} {width:>4} {theme:5} {status}")
                ctx.close()
        browser.close()
    print(f"shots: {failures} failure(s)")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
