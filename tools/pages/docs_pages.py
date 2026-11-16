"""Gallery (root index.html) and the docs site."""
from .shell import doc, head, foot, icon, theme_button, brand, snippet, write, REPO, VERSION


def demo(html_code, note=""):
    n = f'<p class="mn-help" style="margin-bottom:var(--mn-space-2)">{note}</p>' if note else ""
    return f'{n}<div class="mn-demo">{html_code}</div>{snippet(html_code)}'


SHELL = """<body>
<div class="mn-app">
  <aside class="mn-sidebar">
    <a class="mn-brand" href="#">…</a>
    <nav class="mn-nav">
      <div class="mn-nav-label">Overview</div>
      <a class="mn-nav-link" href="#" aria-current="page"><svg class="mn-icon"><use href="#i-home"/></svg>Dashboard</a>
    </nav>
  </aside>
  <div class="mn-scrim"></div>
  <div class="mn-main">
    <header class="mn-topbar">
      <button class="mn-btn mn-btn-outline mn-btn-icon mn-burger" data-mn-sidebar-toggle aria-label="Open menu"><svg class="mn-icon"><use href="#i-menu"/></svg></button>
      <div class="mn-topbar-actions"><button class="mn-btn mn-btn-ghost mn-btn-icon" data-mn-theme-toggle aria-label="Toggle theme"><svg class="mn-icon"><use href="#i-moon"/></svg></button></div>
    </header>
    <main class="mn-content" id="main">
      <div class="mn-page-head"><div><h1>Page title</h1></div></div>
      <!-- your content -->
    </main>
  </div>
</div>
<script src="js/menara.js" defer></script>
</body>"""

HEAD = """<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>My app</title>
  <!-- 1. Apply the saved theme before paint (prevents a light flash in dark mode) -->
  <script data-mn-theme-init>try{var t=localStorage.getItem('mn-theme');if(t)document.documentElement.setAttribute('data-theme',t)}catch(e){}</script>
  <!-- 2. Font (optional: falls back to system-ui) -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;600;700;800&display=swap">
  <!-- 3. Menara UI -->
  <link rel="stylesheet" href="css/tokens.css">
  <link rel="stylesheet" href="css/menara.css">
</head>"""


def build():
    # ---------------- Gallery ----------------
    admin_pages = [("admin/index.html", "home", "Dashboard", "KPIs, CSS bar chart, recent orders, stock meters"),
                   ("admin/table.html", "table", "Data table", "Filters, select-all, bulk delete, pagination, empty state"),
                   ("admin/form.html", "form", "Form", "Inputs, validation, switches, radio, file upload"),
                   ("admin/import.html", "upload", "Import", "Paste-to-import with a preview table"),
                   ("admin/reports.html", "receipt", "Reports", "Period switcher, profit summary, per-product table"),
                   ("admin/analytics.html", "chart", "Analytics", "Funnel, daily and hourly charts, sources"),
                   ("admin/settings.html", "settings", "Settings", "Accessible tabs with keyboard support"),
                   ("admin/users.html", "users", "Users", "Team table and invite form"),
                   ("admin/login.html", "lock", "Sign in", "Split-screen login"),
                   ("admin/404.html", "alert", "404", "Friendly not-found page")]
    store_pages = [("store/index.html", "home", "Storefront", "Hero, trust strip, products, ticker, compare, FAQ"),
                   ("store/product.html", "tag", "Product + checkout", "Details with order summary"),
                   ("store/pay.html", "qr", "Waiting for payment", "QR, live countdown, status"),
                   ("store/success.html", "check", "Success", "Code reveal with copy button"),
                   ("store/lookup.html", "search", "Order lookup", "Find an order again")]

    def cards(items):
        return "".join(f'<a href="{h}">{icon(i, "mn-icon-lg")}<b>{t}</b><span>{d}</span></a>' for h, i, t, d in items)

    write("index.html", f"""{head("Free HTML admin dashboard + storefront template", "")}
<body>
<a class="mn-skip" href="#main">Skip to content</a>
<header class="mn-shop-header">
  <div class="mn-container">
    {brand("index.html", "UI kit v" + VERSION)}
    <nav aria-label="Site"><a href="docs/index.html">Docs</a><a href="docs/components.html">Components</a><a href="{REPO}">GitHub</a></nav>
    {theme_button()}
  </div>
</header>
<main id="main" class="mn-container">
  <section class="mn-hero">
    <span class="mn-hero-chip">{icon("zap", "mn-icon-sm")}No build step · MIT</span>
    <h1>Menara UI</h1>
    <p>A free admin dashboard and storefront template in plain HTML and CSS. Light and dark, rebrandable from one variable, and it ships with an AI skill so coding agents stay on-style.</p>
    <div class="mn-row"><a class="mn-btn mn-btn-accent mn-btn-lg" href="docs/index.html">Get started {icon("arrow-right")}</a><a class="mn-btn mn-btn-outline mn-btn-lg" href="{REPO}">{icon("github")}View on GitHub</a></div>
    <div class="mn-hero-stats"><div><b>15</b>pages</div><div><b>0</b>dependencies</div><div><b>1</b>small script</div></div>
  </section>

  <section class="mn-card" style="margin-bottom:var(--mn-space-7)">
    <div class="mn-card-head"><span class="mn-kpi-icon">{icon("palette")}</span><div><h2>Try your brand color</h2><p>Changes <code>--mn-primary</code> live. Open any template after to see it there too.</p></div></div>
    <div class="mn-card-body mn-row" style="gap:var(--mn-space-4)">
      <label class="mn-row"><input type="color" id="brand" value="#2451c7" aria-label="Primary color" style="width:52px;height:44px;border:1px solid var(--mn-line);border-radius:var(--mn-radius-sm);background:none;padding:2px"> <span class="mn-label" style="margin:0">Primary</span></label>
      <div class="mn-row">{"".join(f'<button type="button" class="mn-btn mn-btn-outline mn-btn-sm" data-color="{c}"><i style="width:14px;height:14px;border-radius:50%;background:{c};display:inline-block"></i>{n}</button>' for c, n in [("#2451c7", "Menara"), ("#0f766e", "Teal"), ("#7c3aed", "Violet"), ("#be123c", "Rose"), ("#c2410c", "Orange")])}</div>
      <button type="button" class="mn-btn mn-btn-ghost mn-btn-sm" id="brand-reset">Reset</button>
      <span class="mn-spacer"></span>
      <button type="button" class="mn-btn mn-btn-primary">Primary</button><span class="mn-badge mn-badge-primary">Badge</span><label class="mn-switch"><input type="checkbox" checked> Switch</label>
    </div>
  </section>

  <section class="mn-section"><div class="mn-section-head"><h2>Admin</h2><p>Sidebar app shell, collapses to a drawer on phones.</p></div><div class="mn-gallery">{cards(admin_pages)}</div></section>
  <section class="mn-section"><div class="mn-section-head"><h2>Storefront &amp; landing</h2><p>Mobile-first shop with a bottom nav on phones.</p></div><div class="mn-gallery">{cards(store_pages)}</div></section>
  <section class="mn-section"><div class="mn-section-head"><h2>Docs</h2></div><div class="mn-gallery">
    <a href="docs/index.html">{icon("book", "mn-icon-lg")}<b>Getting started</b><span>Install in two minutes</span></a>
    <a href="docs/theming.html">{icon("palette", "mn-icon-lg")}<b>Theming</b><span>Tokens, dark mode, rebranding</span></a>
    <a href="docs/components.html">{icon("layers", "mn-icon-lg")}<b>Components</b><span>Live examples with copyable code</span></a>
    <a href="docs/layout.html">{icon("table", "mn-icon-lg")}<b>Layout</b><span>App shell, grids, breakpoints</span></a>
    <a href="docs/accessibility.html">{icon("eye", "mn-icon-lg")}<b>Accessibility</b><span>What’s built in and what’s on you</span></a>
  </div></section>
</main>
<footer class="mn-footer"><div class="mn-container"><span>Menara UI v{VERSION} · MIT License</span><span>Font: Rubik (OFL) · Icons: Lucide-style (ISC)</span></div></footer>
<script>
(function () {{
  var root = document.documentElement, input = document.getElementById('brand');
  var VARS = ['--mn-primary', '--mn-primary-hover', '--mn-primary-text', '--mn-brand-surface', '--mn-primary-soft'];
  function apply(c) {{
    VARS.slice(0, 4).forEach(function (v) {{ root.style.setProperty(v, c); }});
    root.style.setProperty('--mn-primary-soft', 'color-mix(in srgb, ' + c + ' 14%, var(--mn-surface))');
    input.value = c;
    try {{ localStorage.setItem('mn-brand', c); }} catch (e) {{}}
  }}
  input.addEventListener('input', function () {{ apply(input.value); }});
  document.querySelectorAll('[data-color]').forEach(function (b) {{ b.addEventListener('click', function () {{ apply(b.getAttribute('data-color')); }}); }});
  document.getElementById('brand-reset').addEventListener('click', function () {{
    VARS.forEach(function (v) {{ root.style.removeProperty(v); }});
    input.value = '#2451c7'; try {{ localStorage.removeItem('mn-brand'); }} catch (e) {{}}
  }});
  try {{ var saved = localStorage.getItem('mn-brand'); if (saved) apply(saved); }} catch (e) {{}}
}})();
</script>
{foot("")}""")

    # ---------------- Getting started ----------------
    doc("index.html", "Getting started", f"""
<h1>Getting started</h1>
<p>Menara UI is plain HTML, CSS and a small script. There is nothing to install or build. Copy the files, link them, and start from the page closest to what you need.</p>
<h2>1. Get the files</h2>
{snippet("git clone " + REPO + ".git")}
<p>Or download the ZIP from GitHub. Open <code>index.html</code> in your browser to see every template.</p>
<h2>2. Copy three files into your project</h2>
<ul><li><code>css/tokens.css</code>: colors, type, spacing (edit this to rebrand)</li><li><code>css/menara.css</code>: all components</li><li><code>js/menara.js</code>: theme toggle, mobile sidebar, modal, tabs, copy, select-all, countdown, and the icon sprite</li></ul>
<h2>3. Add them to your page</h2>
{snippet(HEAD)}
<p>Load the script at the end of <code>&lt;body&gt;</code> with <code>defer</code>:</p>
{snippet('<script src="js/menara.js" defer></script>')}
<h2>4. Start from a template</h2>
<p>Copy the closest page from <code>admin/</code> or <code>store/</code> and replace the dummy data. Every page uses only <code>mn-</code> classes, so it works the same in Laravel Blade, Django templates, Rails, Express views or static HTML.</p>
<h2>Using it with a framework</h2>
<ul><li><b>Laravel:</b> put the folders in <code>public/</code> and use <code>asset('css/menara.css')</code>. Move the sidebar into a Blade layout.</li><li><b>Django / Flask:</b> put them in <code>static/</code> and the shell in <code>base.html</code>.</li><li><b>React / Vue:</b> import the two CSS files once. Keep the class names and skip <code>menara.js</code> if your framework handles the behaviour (you still need an icon solution).</li></ul>
<h2>Using it with an AI agent</h2>
<p>Copy <code>skills/menara-ui/</code> into your project’s <code>.claude/skills/</code> folder (or your agent’s skills folder). The skill teaches the layout, type, color and component rules so new pages stay consistent.</p>
<h2>Translating</h2>
<p>All text lives in the HTML. Change <code>lang="en"</code> on <code>&lt;html&gt;</code> and translate the copy. The only strings in <code>menara.js</code> are the theme button labels, “Copied!”, “Copied to clipboard” and “Expired”.</p>
<h2>Editing the templates in this repo</h2>
<p>The HTML pages are generated by <code>tools/build.py</code> so the sidebar and headers stay identical everywhere. If you contribute, edit <code>tools/pages/</code>, then run <code>python3 tools/build.py &amp;&amp; python3 tools/check.py</code>. If you only use the template, ignore this and edit the HTML directly.</p>""")

    # ---------------- Theming ----------------
    def sw(v, n):
        return f'<div class="mn-swatch"><i style="background:var({v})"></i><div><b>{n}</b><code>{v}</code></div></div>'
    doc("theming.html", "Theming", f"""
<h1>Theming</h1>
<p>Every color, size and shadow is a CSS custom property in <code>css/tokens.css</code>. Components never use raw colors, so changing a token changes the whole UI.</p>
<h2>Rebrand in a few lines</h2>
<p>Override the brand tokens after <code>tokens.css</code>:</p>
{snippet(""":root {
  --mn-primary: #0f766e;        /* buttons, links, focus, active nav, charts */
  --mn-primary-hover: #0b5f59;
  --mn-primary-soft: #e6f4f2;   /* tinted backgrounds */
  --mn-primary-text: #0f766e;   /* primary used as text on light surfaces */
  --mn-accent: #ffc83d;         /* highlights, current bar, badges */
}
:root[data-theme="dark"] {
  --mn-primary: #2dd4bf;
  --mn-primary-text: #5eead4;
  --mn-brand-surface: #134e4a;  /* store header + hero in dark mode */
}""")}
<p>Dark values also live under <code>@media (prefers-color-scheme: dark)</code> in <code>tokens.css</code>. Change both blocks, or delete the media block if you only want an explicit toggle. Try colors live on the <a href="../index.html">gallery page</a>, and check contrast: text on <code>--mn-primary</code> uses <code>--mn-primary-ink</code>.</p>
<h2>Palette</h2>
<div class="mn-swatches">{sw("--mn-primary", "Primary")}{sw("--mn-accent", "Accent")}{sw("--mn-navy", "Navy")}{sw("--mn-ink", "Ink")}{sw("--mn-muted", "Muted")}{sw("--mn-line", "Line")}{sw("--mn-surface", "Surface")}{sw("--mn-bg", "Background")}{sw("--mn-success", "Success")}{sw("--mn-warning", "Warning")}{sw("--mn-danger", "Danger")}{sw("--mn-info", "Info")}</div>
<h2>Dark mode</h2>
<p>Dark mode follows the operating system by default. A <code>data-mn-theme-toggle</code> button switches it and remembers the choice in <code>localStorage</code> (key <code>mn-theme</code>). To force a theme, set the attribute yourself:</p>
{snippet('<html lang="en" data-theme="dark">')}
<p>Keep the small <code>data-mn-theme-init</code> script in <code>&lt;head&gt;</code>. It applies the saved theme before the first paint, so dark-mode users never see a white flash.</p>
<h2>Typography</h2>
<p>Rubik from Google Fonts, falling back to the system font. Sizes run from <code>--mn-text-xs</code> (12px, the minimum) to <code>--mn-text-3xl</code> (40px). Body text is neutral ink, not brand blue. Use <code>.mn-num</code> for tabular numbers in tables and KPIs.</p>
<h2>Spacing, radius, shadows</h2>
<p>A 4px grid: <code>--mn-space-1</code> (4px) to <code>--mn-space-8</code> (48px). Radius <code>--mn-radius-sm|md|lg|pill</code>. Shadows <code>--mn-shadow-sm|md|lg</code>.</p>""")

    # ---------------- Components ----------------
    i = icon
    sections = [
        ("Buttons", f'<div class="mn-row"><button class="mn-btn mn-btn-primary">{i("plus")}Primary</button><button class="mn-btn mn-btn-accent">Accent</button><button class="mn-btn mn-btn-outline">Outline</button><button class="mn-btn mn-btn-ghost">Ghost</button><button class="mn-btn mn-btn-danger">{i("trash")}Delete</button><button class="mn-btn mn-btn-outline mn-btn-icon" aria-label="Settings">{i("settings")}</button><button class="mn-btn mn-btn-primary mn-btn-sm">Small</button><button class="mn-btn mn-btn-primary" disabled>Disabled</button></div>',
         "Sizes: <code>mn-btn-sm</code>, <code>mn-btn-lg</code>, <code>mn-btn-block</code>, <code>mn-btn-icon</code> (always add <code>aria-label</code>)."),
        ("Form fields", '<div class="mn-form-grid"><div class="mn-field"><label class="mn-label" for="d-email">Email <span class="mn-req" aria-hidden="true">*</span></label><input class="mn-input" id="d-email" type="email" placeholder="you@example.com"><p class="mn-help">We never share it.</p></div><div class="mn-field"><label class="mn-label" for="d-slug">Slug</label><input class="mn-input is-invalid" id="d-slug" value="Bad Slug" aria-invalid="true" aria-describedby="d-slug-e"><p class="mn-error" id="d-slug-e">Lowercase letters and dashes only.</p></div><div class="mn-field"><label class="mn-label" for="d-sel">Select</label><select class="mn-select" id="d-sel"><option>Option A</option><option>Option B</option></select></div><div class="mn-field"><label class="mn-label" for="d-price">With prefix</label><div class="mn-input-group"><span>$</span><input class="mn-input" id="d-price" value="12.00"></div></div></div>', ""),
        ("Switch, checkbox, radio", '<div class="mn-row" style="gap:var(--mn-space-5)"><label class="mn-switch"><input type="checkbox" checked> Show in store</label><label class="mn-check"><input type="checkbox" checked> Remember me</label><label class="mn-check"><input type="radio" name="d-r" checked> Instant</label><label class="mn-check"><input type="radio" name="d-r"> Manual</label></div>', ""),
        ("Badges", '<div class="mn-row"><span class="mn-badge mn-badge-success">Paid</span><span class="mn-badge mn-badge-warning">Pending</span><span class="mn-badge mn-badge-danger">Failed</span><span class="mn-badge mn-badge-info">Sent</span><span class="mn-badge mn-badge-neutral">Expired</span><span class="mn-badge mn-badge-primary">New</span><span class="mn-badge mn-badge-accent mn-badge-plain">Best value</span></div>', ""),
        ("Alerts", f'<div class="mn-stack" style="gap:var(--mn-space-3)"><div class="mn-alert mn-alert-success" role="status">{i("check")}<div><b>Saved</b>Your changes are live.</div></div><div class="mn-alert mn-alert-warning">{i("alert")}<div><b>Stock is low</b>4 codes left.</div><button type="button" class="mn-btn mn-btn-ghost mn-btn-sm mn-btn-icon" data-mn-dismiss aria-label="Dismiss">{i("x")}</button></div><div class="mn-alert mn-alert-danger" role="alert">{i("alert")}<div><b>Payment failed</b>Try another method.</div></div></div>', "<code>data-mn-dismiss</code> removes the alert."),
        ("Card + KPI", f'<div class="mn-grid mn-grid-2"><div class="mn-card mn-kpi"><span class="mn-kpi-icon">{i("wallet")}</span><div><span class="mn-kpi-label">Revenue</span><b class="mn-kpi-value">$2,480</b><span class="mn-kpi-meta"><span class="mn-up">+12%</span> vs yesterday</span></div></div><section class="mn-card"><div class="mn-card-head"><div><h3>Card title</h3><p>Subtitle</p></div><a class="mn-link" href="#">Action</a></div><div class="mn-card-body">Body content.</div></section></div>', ""),
        ("Bar chart (CSS)", '<div class="mn-bars" role="img" aria-label="Orders: Mon 42, Tue 58, Wed 96"><div class="mn-bar" style="--v:.44"><span class="mn-bar-value">42</span><i></i><span class="mn-bar-label">Mon</span></div><div class="mn-bar" style="--v:.6"><span class="mn-bar-value">58</span><i></i><span class="mn-bar-label">Tue</span></div><div class="mn-bar is-current" style="--v:1"><span class="mn-bar-value">96</span><i></i><span class="mn-bar-label">Wed</span></div></div>', "Set each bar’s height with <code>--v</code> from 0 to 1. Always give the chart an <code>aria-label</code> with the numbers."),
        ("Meters", '<div class="mn-card"><div class="mn-meter-row"><span>Storage</span><b>86%</b><div class="mn-meter is-success" style="--v:.86"><i></i></div></div><div class="mn-meter-row"><span>Seats</span><b>12%</b><div class="mn-meter is-warning" style="--v:.12"><i></i></div></div></div>', ""),
        ("Table", '<div class="mn-card"><div class="mn-table-wrap"><table class="mn-table"><thead><tr><th class="is-check"><input type="checkbox" data-mn-check-all="d-ids" aria-label="Select all"></th><th>Order</th><th class="is-right">Amount</th><th>Status</th></tr></thead><tbody><tr><td class="is-check"><input type="checkbox" name="d-ids" aria-label="Select MN-1"></td><td>MN-1</td><td class="is-right mn-num">$12.00</td><td><span class="mn-badge mn-badge-success">Paid</span></td></tr><tr><td class="is-check"><input type="checkbox" name="d-ids" aria-label="Select MN-2"></td><td>MN-2</td><td class="is-right mn-num">$9.50</td><td><span class="mn-badge mn-badge-warning">Pending</span></td></tr></tbody></table></div></div>', "<code>data-mn-check-all=\"name\"</code> toggles every checkbox with that name. Add <code>data-mn-check-count</code> / <code>data-mn-check-bar</code> for a bulk-action bar."),
        ("Tabs", '<div class="mn-card mn-tabs" data-mn-tabs><div role="tablist" aria-label="Demo tabs"><button type="button" role="tab" id="dt1" aria-controls="dp1" aria-selected="true">One</button><button type="button" role="tab" id="dt2" aria-controls="dp2" aria-selected="false">Two</button></div><div role="tabpanel" id="dp1" aria-labelledby="dt1" class="mn-card-body">First panel. Use arrow keys to switch.</div><div role="tabpanel" id="dp2" aria-labelledby="dt2" class="mn-card-body" hidden>Second panel.</div></div>', ""),
        ("Segmented filter", '<div class="mn-segment" role="group" aria-label="Period"><a href="#" aria-current="page">Today</a><a href="#">7 days</a><a href="#">30 days</a></div>', ""),
        ("Modal", '<button type="button" class="mn-btn mn-btn-outline" data-mn-modal-open="demo-modal">Open modal</button><dialog class="mn-modal" id="demo-modal" aria-labelledby="dm-t"><div class="mn-modal-body"><h2 id="dm-t">Delete product?</h2><p>This can’t be undone.</p></div><div class="mn-card-foot"><button type="button" class="mn-btn mn-btn-outline" data-mn-modal-close>Cancel</button><button type="button" class="mn-btn mn-btn-danger" data-mn-modal-close>Delete</button></div></dialog>', "Native <code>&lt;dialog&gt;</code>: Escape and the backdrop close it, focus returns to the button."),
        ("Copy to clipboard", '<div class="mn-code"><b id="d-code">K7QX-22LM</b><button type="button" class="mn-btn mn-btn-primary" data-mn-copy="#d-code"><span data-mn-copy-label>Copy</span></button></div>', ""),
        ("Empty state", f'<div class="mn-empty">{i("search")}<b>No results</b>Try another filter.</div>', ""),
        ("Icons", '<div class="mn-row">' + "".join(f'<span title="i-{n}" style="display:inline-grid;place-items:center;width:44px;height:44px;border:1px solid var(--mn-line);border-radius:var(--mn-radius-sm)">{i(n)}</span>' for n in ["home", "chart", "table", "form", "upload", "download", "settings", "users", "bell", "search", "plus", "edit", "trash", "check", "x", "copy", "alert", "info", "zap", "shield", "clock", "cart", "tag", "qr", "wallet", "receipt", "package", "lock", "mail", "eye", "tower"]) + '</div>',
         "Use <code>&lt;svg class=\"mn-icon\" aria-hidden=\"true\"&gt;&lt;use href=\"#i-name\"/&gt;&lt;/svg&gt;</code>. The sprite is injected by <code>menara.js</code>. Hover an icon to see its name."),
    ]
    body = "".join(f'<h2 id="c{n}">{t}</h2>' + demo(code, note) for n, (t, code, note) in enumerate(sections))
    toc = "".join(f'<a class="mn-badge mn-badge-neutral mn-badge-plain" href="#c{n}">{t}</a>' for n, (t, _, _) in enumerate(sections))
    doc("components.html", "Components", f"""
<h1>Components</h1>
<p>Live examples. Copy the snippet under each one. Everything uses classes from <code>css/menara.css</code> and colors from <code>css/tokens.css</code>.</p>
<div class="mn-row" style="margin-bottom:var(--mn-space-5)">{toc}</div>
{body}""")

    # ---------------- Layout ----------------
    doc("layout.html", "Layout", f"""
<h1>Layout</h1>
<h2>Admin shell</h2>
<p>A fixed dark sidebar (256px) and a sticky topbar. Below 1024px the sidebar becomes a drawer opened by the burger button. Escape or the dimmed backdrop closes it.</p>
{snippet(SHELL)}
<h2>Page header</h2>
<p><code>.mn-page-head</code>: breadcrumb and <code>h1</code> on the left, actions on the right. Actions wrap under the title on phones.</p>
<h2>Grids</h2>
<ul><li><code>mn-grid mn-grid-4</code>: KPI row. 4 → 2 columns below 1100px.</li><li><code>mn-grid mn-grid-main</code>: main column + side column (about 62/38). Stacks below 1100px.</li><li><code>mn-grid-2</code>, <code>mn-grid-3</code>: even columns.</li><li><code>mn-stack</code>: vertical rhythm inside a column.</li></ul>
<h2>Storefront</h2>
<p><code>&lt;body class="mn-shop"&gt;</code> + <code>.mn-shop-header</code> + <code>&lt;main class="mn-container"&gt;</code> (max 1120px). <code>.mn-bottom-nav</code> shows on phones only. Keep it to four items.</p>
<h2>Breakpoints</h2>
<ul><li>360px: smallest supported width. Nothing scrolls sideways.</li><li>560px: topbar search hides.</li><li>640px: forms become one column. KPIs get smaller.</li><li>900px: store top nav ↔ bottom nav.</li><li>1024px: admin sidebar ↔ drawer.</li><li>1100px: multi-column grids collapse.</li></ul>
<h2>Rules</h2>
<ul><li>Tables scroll inside <code>.mn-table-wrap</code>, never the page.</li><li>Use cards for summaries and tables for lists people scan or sort.</li><li>One primary button per view.</li><li>Long names get <code>.mn-cell-title</code> (truncates) or wrap. Numbers get <code>.mn-num</code> and right alignment.</li></ul>""")

    # ---------------- Accessibility ----------------
    doc("accessibility.html", "Accessibility", """
<h1>Accessibility</h1>
<h2>Built in</h2>
<ul>
<li>Text contrast of at least 4.5:1 in light and dark themes. Muted text is tuned for both.</li>
<li>Visible focus rings on every interactive element (<code>:focus-visible</code>).</li>
<li>Touch targets of at least 44px for buttons, nav links, inputs and switches.</li>
<li>A skip link (<code>.mn-skip</code>) on every template.</li>
<li>Tabs follow the ARIA pattern: arrow keys, Home and End.</li>
<li>The modal uses native <code>&lt;dialog&gt;</code>: Escape closes it and focus returns to the opener.</li>
<li>The mobile sidebar closes with Escape. The theme button exposes <code>aria-pressed</code>.</li>
<li><code>prefers-reduced-motion</code> turns off animations, including the ticker.</li>
<li>No text smaller than 12px.</li>
</ul>
<h2>Your part</h2>
<ul>
<li>Give icon-only buttons an <code>aria-label</code>.</li>
<li>Label every input with <code>&lt;label for&gt;</code>. Point errors at the field with <code>aria-describedby</code> and add <code>aria-invalid="true"</code>.</li>
<li>Give charts an <code>aria-label</code> with the actual numbers.</li>
<li>Don’t rely on color alone: status badges also carry words.</li>
<li>Check contrast again if you change brand colors.</li>
</ul>""")
