"""Shared page shells for the Menara UI generator (dev-time only; output is plain HTML)."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
VERSION = "1.0.0"
REPO = "https://github.com/armandawahyuu/menara-ui"

THEME_INIT = ("<script data-mn-theme-init>try{var t=localStorage.getItem('mn-theme');"
              "if(t)document.documentElement.setAttribute('data-theme',t)}catch(e){}</script>")


def icon(name, cls=""):
    return f'<svg class="mn-icon{(" " + cls) if cls else ""}" aria-hidden="true"><use href="#i-{name}"/></svg>'


def head(title, root, desc="Menara UI — free HTML/CSS admin dashboard and storefront template."):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Menara UI</title>
<meta name="description" content="{desc}">
{THEME_INIT}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="{root}css/tokens.css">
<link rel="stylesheet" href="{root}css/menara.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%232451c7'/%3E%3Cpath d='M16 6v4M11 26l5-16 5 16M13 20h6' stroke='white' stroke-width='2.4' fill='none' stroke-linecap='round'/%3E%3C/svg%3E">
</head>"""


def foot(root):
    return f'<script src="{root}js/menara.js" defer></script>\n</body>\n</html>\n'


def theme_button(cls="mn-btn mn-btn-ghost mn-btn-icon"):
    return f'<button type="button" class="{cls}" data-mn-theme-toggle aria-label="Switch to dark mode">{icon("moon")}</button>'


def brand(href, sub="Admin"):
    return (f'<a class="mn-brand" href="{href}"><span class="mn-brand-mark">{icon("tower")}</span>'
            f'<span><b>Menara</b><small>{sub}</small></span></a>')


ADMIN_NAV = [
    ("Overview", [("index.html", "home", "Dashboard"), ("analytics.html", "chart", "Analytics"), ("reports.html", "receipt", "Reports")]),
    ("Store", [("table.html", "table", "Orders", "12"), ("form.html", "package", "Products"), ("import.html", "upload", "Import")]),
    ("Settings", [("users.html", "users", "Users"), ("settings.html", "settings", "Settings")]),
]


def admin(file, title, body, crumbs=None, head_actions=""):
    root = "../"
    nav = []
    for label, links in ADMIN_NAV:
        nav.append(f'<div class="mn-nav-label">{label}</div>')
        for item in links:
            href, ic, text = item[:3]
            count = f'<span class="mn-nav-count">{item[3]}</span>' if len(item) > 3 else ""
            cur = ' aria-current="page"' if href == file else ""
            nav.append(f'<a class="mn-nav-link" href="{href}"{cur}>{icon(ic)}{text}{count}</a>')
    crumb_html = ""
    if crumbs:
        crumb_html = '<nav class="mn-crumbs" aria-label="Breadcrumb">' + " / ".join(
            f'<a href="{h}">{t}</a>' if h else f'<span>{t}</span>' for h, t in crumbs) + "</nav>"
    html = f"""{head(title, root)}
<body>
<a class="mn-skip" href="#main">Skip to content</a>
<div class="mn-app">
  <aside class="mn-sidebar" aria-label="Main navigation">
    {brand("index.html")}
    <nav class="mn-nav">
      {"".join(nav)}
    </nav>
    <div class="mn-sidebar-foot">
      <a class="mn-nav-link" href="../index.html">{icon("layers")}All templates</a>
      <a class="mn-nav-link" href="login.html">{icon("logout")}Sign out</a>
    </div>
  </aside>
  <div class="mn-scrim"></div>
  <div class="mn-main">
    <header class="mn-topbar">
      <button type="button" class="mn-btn mn-btn-outline mn-btn-icon mn-burger" data-mn-sidebar-toggle aria-label="Open menu" aria-expanded="false">{icon("menu")}</button>
      <label class="mn-search" style="width:min(360px,100%)"><span class="mn-sr-only">Search</span>{icon("search")}<input class="mn-input" type="search" placeholder="Search orders, products…"></label>
      <div class="mn-topbar-actions">
        {theme_button()}
        <button type="button" class="mn-btn mn-btn-ghost mn-btn-icon" aria-label="Notifications">{icon("bell")}</button>
        <details class="mn-dropdown">
          <summary class="mn-btn mn-btn-ghost" aria-label="Account menu"><span class="mn-avatar">AR</span></summary>
          <div class="mn-menu">
            <a href="users.html">{icon("user")}Profile</a>
            <a href="settings.html">{icon("settings")}Settings</a>
            <hr>
            <a href="login.html">{icon("logout")}Sign out</a>
          </div>
        </details>
      </div>
    </header>
    <main class="mn-content" id="main">
      <div class="mn-page-head">
        <div>{crumb_html}<h1>{title}</h1></div>
        {f'<div>{head_actions}</div>' if head_actions else ''}
      </div>
{body}
    </main>
  </div>
</div>
{foot(root)}"""
    write(f"admin/{file}", html)


SHOP_NAV = [("index.html", "home", "Home"), ("index.html#products", "tag", "Products"), ("lookup.html", "receipt", "My order"), ("index.html#faq", "headset", "Help")]


def store(file, title, body, active="index.html", banner=True):
    root = "../"
    top_nav = "".join(f'<a href="{h}">{t}</a>' for h, _, t in SHOP_NAV)
    bottom = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{icon(i)}{t}</a>' for h, i, t in SHOP_NAV)
    ban = (f'<div class="mn-banner" role="note">{icon("zap", "mn-icon-sm")}<span>Weekend deal: 10% off all bundles until Sunday.</span>'
           f'<button type="button" class="mn-btn mn-btn-ghost mn-btn-sm mn-btn-icon" data-mn-dismiss aria-label="Dismiss">{icon("x")}</button></div>') if banner else ""
    html = f"""{head(title, root)}
<body class="mn-shop">
<a class="mn-skip" href="#main">Skip to content</a>
{ban}
<header class="mn-shop-header">
  <div class="mn-container">
    {brand("index.html", "Digital store")}
    <nav aria-label="Store">{top_nav}</nav>
    {theme_button("mn-btn mn-btn-ghost mn-btn-icon")}
  </div>
</header>
<main id="main" class="mn-container">
{body}
</main>
<footer class="mn-footer">
  <div class="mn-container">
    <span>© 2026 Menara Store · Built with <a href="../index.html">Menara UI</a></span>
    <span><a href="lookup.html">Track an order</a> · <a href="index.html#faq">Help</a></span>
  </div>
</footer>
<nav class="mn-bottom-nav" aria-label="Store shortcuts">{bottom}</nav>
{foot(root)}"""
    write(f"store/{file}", html)


DOCS_NAV = [("index.html", "Getting started"), ("theming.html", "Theming"), ("components.html", "Components"),
            ("layout.html", "Layout"), ("accessibility.html", "Accessibility")]


def doc(file, title, body):
    root = "../"
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == file else ""}>{t}</a>' for h, t in DOCS_NAV)
    html = f"""{head(title, root)}
<body>
<a class="mn-skip" href="#main">Skip to content</a>
<header class="mn-shop-header">
  <div class="mn-container">
    {brand("../index.html", "Docs")}
    <nav aria-label="Site"><a href="../index.html">Templates</a><a href="index.html">Docs</a><a href="{REPO}">GitHub</a></nav>
    {theme_button()}
  </div>
</header>
<div class="mn-container mn-doc">
  <nav class="mn-doc-nav" aria-label="Documentation">{nav}</nav>
  <main id="main" class="mn-prose">
{body}
  </main>
</div>
{foot(root)}"""
    write(f"docs/{file}", html)


def snippet(code):
    import html as h
    esc = h.escape(code.strip())
    return (f'<div class="mn-snippet"><pre><code>{esc}</code></pre>'
            f'<button type="button" class="mn-btn mn-btn-outline mn-btn-sm" data-mn-copy="{h.escape(code.strip(), quote=True)}">'
            f'<span data-mn-copy-label>Copy</span></button></div>')


def write(rel, html):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html, encoding="utf-8")
