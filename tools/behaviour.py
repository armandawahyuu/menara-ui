#!/usr/bin/env python3
"""Behaviour checks for menara.js (dev-only; needs playwright + Chrome). Exit 1 on any failure.

    python3 tools/behaviour.py
"""
import pathlib
import sys

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
fails = []


def check(name, ok):
    print(("ok   " if ok else "FAIL ") + name)
    if not ok:
        fails.append(name)


def url(rel):
    return (ROOT / rel).as_uri()


with sync_playwright() as pw:
    b = pw.chromium.launch(channel="chrome")

    # Theme: toggle persists, reload applies it before scripts run (no flash), icon flips.
    ctx = b.new_context(color_scheme="light")
    p = ctx.new_page()
    p.goto(url("admin/index.html"))
    p.click("[data-mn-theme-toggle]")
    check("theme toggle sets dark", p.evaluate("document.documentElement.dataset.theme") == "dark")
    check("theme button aria-pressed", p.get_attribute("[data-mn-theme-toggle]", "aria-pressed") == "true")
    p.goto(url("store/index.html"), wait_until="commit")
    p.wait_for_selector("body")
    check("saved theme applied on next page before load", p.evaluate("document.documentElement.dataset.theme") == "dark")
    bg = p.evaluate("getComputedStyle(document.body).backgroundColor")
    check("dark background really dark", bg in ("rgb(11, 16, 32)",))
    ctx.close()

    # Mobile drawer: burger opens, Escape closes, focus moves into the sidebar.
    ctx = b.new_context(viewport={"width": 390, "height": 800})
    p = ctx.new_page()
    p.goto(url("admin/index.html"))
    check("burger visible on phone", p.is_visible(".mn-burger"))
    p.click(".mn-burger")
    check("drawer opens", p.evaluate("document.querySelector('.mn-app').classList.contains('is-nav-open')"))
    check("focus moved into sidebar", p.evaluate("!!document.activeElement.closest('.mn-sidebar')"))
    p.keyboard.press("Escape")
    check("Escape closes drawer", not p.evaluate("document.querySelector('.mn-app').classList.contains('is-nav-open')"))
    ctx.close()

    ctx = b.new_context(viewport={"width": 1280, "height": 900})
    p = ctx.new_page()
    p.goto(url("admin/index.html"))
    check("burger hidden on desktop", not p.is_visible(".mn-burger"))

    # Select-all + bulk bar + modal focus return.
    p.goto(url("admin/table.html"))
    p.check("[data-mn-check-all='ids']")
    check("select-all checks every row", p.evaluate("[...document.querySelectorAll('input[name=ids]')].every(i => i.checked)"))
    check("bulk bar shows count", p.is_visible("[data-mn-check-bar='ids']") and p.inner_text("[data-mn-check-count='ids']") == "8")
    p.uncheck("input[name=ids] >> nth=0")
    check("header checkbox indeterminate", p.evaluate("document.querySelector('[data-mn-check-all]').indeterminate"))
    p.click("[data-mn-modal-open='confirm-delete']")
    check("modal opens", p.evaluate("document.getElementById('confirm-delete').open"))
    p.keyboard.press("Escape")
    check("Escape closes modal", not p.evaluate("document.getElementById('confirm-delete').open"))
    check("focus returns to opener", p.evaluate("document.activeElement.matches('[data-mn-modal-open]')"))

    # Tabs: arrow keys move selection and panels.
    p.goto(url("admin/settings.html"))
    p.focus("#t-general")
    p.keyboard.press("ArrowRight")
    check("ArrowRight selects next tab", p.get_attribute("#t-pay", "aria-selected") == "true" and p.is_visible("#p-pay") and not p.is_visible("#p-general"))
    p.keyboard.press("End")
    check("End selects last tab", p.get_attribute("#t-notify", "aria-selected") == "true")
    p.keyboard.press("ArrowRight")
    check("ArrowRight wraps to first", p.get_attribute("#t-general", "aria-selected") == "true")

    # Dropdown closes on Escape; alert dismiss removes it.
    p.goto(url("admin/index.html"))
    p.click(".mn-dropdown summary")
    p.keyboard.press("Escape")
    check("Escape closes account menu", not p.evaluate("document.querySelector('.mn-dropdown').open"))
    n = p.locator(".mn-alert").count()
    p.click(".mn-alert [data-mn-dismiss]")
    check("dismiss removes alert", p.locator(".mn-alert").count() == n - 1)

    # Icons rendered from the injected sprite.
    check("icon sprite injected", p.evaluate("!!document.getElementById('i-home')"))

    # Countdown ticks.
    p.goto(url("store/pay.html"))
    p.wait_for_timeout(1300)
    check("countdown running", p.inner_text("[data-mn-countdown]") in ("29:59", "29:58"))

    # Copy shows feedback.
    ctx2 = b.new_context(permissions=["clipboard-read", "clipboard-write"])
    q = ctx2.new_page()
    q.goto(url("store/success.html"))
    q.click("[data-mn-copy]")
    try:  # clipboard write is async
        q.wait_for_function("document.querySelector('[data-mn-copy-label]').textContent === 'Copied!'", timeout=2000)
        copied = True
    except Exception:
        copied = False
    check("copy shows Copied!", copied)
    check("clipboard holds the code", q.evaluate("navigator.clipboard.readText()") == "K7QX-22LM-90PA")
    ctx2.close()

    # Rebrand: one variable recolors primary buttons, focus ring and chart bars.
    p.goto(url("admin/index.html"))
    p.evaluate("document.documentElement.style.setProperty('--mn-primary', 'rgb(15, 118, 110)')")
    p.wait_for_timeout(400)  # let the 150ms colour transition finish
    check("primary button follows --mn-primary", p.evaluate("getComputedStyle(document.querySelector('.mn-btn-primary')).backgroundColor") == "rgb(15, 118, 110)")
    check("chart bar follows --mn-primary", p.evaluate("getComputedStyle(document.querySelector('.mn-bar:not(.is-current) i')).backgroundColor") == "rgb(15, 118, 110)")

    # No console errors anywhere.
    errs = []
    p.on("pageerror", lambda e: errs.append(str(e)))
    for f in sorted(ROOT.rglob("*.html")):
        if "superpowers" in f.parts or "tools" in f.parts:
            continue
        p.goto(f.as_uri())
    check("no JS errors on any page", not errs)
    ctx.close()
    b.close()

print(f"behaviour: {len(fails)} failure(s)")
sys.exit(1 if fails else 0)
