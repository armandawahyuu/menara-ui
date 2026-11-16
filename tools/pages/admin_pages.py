"""Admin pages. Dummy data for a fictional digital-goods shop."""
from .shell import admin, head, foot, icon, theme_button, write, brand

ORDERS = [
    ("MN-24081", "Maya Putri", "maya@example.com", "Cloud Storage 100 GB", "$12.00", "success", "Paid", "2 min ago"),
    ("MN-24080", "Alexandria Montgomery-Washington", "alexandria.montgomery-washington@example-company.com", "Design Asset Pack — Ultimate Bundle (icons, mockups, fonts, 3D scenes)", "$149.00", "warning", "Pending", "8 min ago"),
    ("MN-24079", "Budi Santoso", "budi@example.com", "Streaming Pass · 30 days", "$9.50", "success", "Paid", "21 min ago"),
    ("MN-24078", "Chen Wei", "chen.wei@example.com", "E-book Bundle: Product Design", "$24.00", "danger", "Failed", "1 h ago"),
    ("MN-24077", "Sofia Rossi", "sofia@example.com", "Domain .com · 1 year", "$11.99", "neutral", "Expired", "2 h ago"),
    ("MN-24076", "Northwind Holdings", "billing@example.org", "Enterprise license · 500 seats", "$12,480,000.00", "info", "Invoice sent", "Yesterday"),
    ("MN-24075", "Liam O'Brien", "liam@example.com", "Cloud Storage 1 TB", "$79.00", "success", "Paid", "Yesterday"),
    ("MN-24074", "Aisha Rahman", "aisha@example.com", "Streaming Pass · 7 days", "$3.00", "success", "Paid", "2 days ago"),
]


def badge(tone, text):
    return f'<span class="mn-badge mn-badge-{tone}">{text}</span>'


def kpi(ic, tone, label, value, meta):
    t = f" is-{tone}" if tone else ""
    return (f'<div class="mn-card mn-kpi"><span class="mn-kpi-icon{t}">{icon(ic)}</span><div>'
            f'<span class="mn-kpi-label">{label}</span><b class="mn-kpi-value">{value}</b>'
            f'<span class="mn-kpi-meta">{meta}</span></div></div>')


def bars(values, labels, current=-1, dense=False, show=True):
    """current: index of the highlighted bar (-1 = last, None = none)."""
    top = max(values) or 1
    hi = None if current is None else current % len(values)
    out = []
    for i, (v, l) in enumerate(zip(values, labels)):
        cur = " is-current" if i == hi else ""
        val = f'<span class="mn-bar-value">{v}</span>' if show else ""
        out.append(f'<div class="mn-bar{cur}" style="--v:{v / top:.2f}" title="{l}: {v}">{val}<i></i><span class="mn-bar-label">{l}</span></div>')
    return f'<div class="mn-bars{" mn-bars-dense" if dense else ""}" role="img" aria-label="Bar chart: {", ".join(f"{l} {v}" for v, l in zip(values, labels))}">{"".join(out)}</div>'


def orders_table(rows, check=False, limit=None):
    head_check = '<th class="is-check"><input type="checkbox" class="mn-check" data-mn-check-all="ids" aria-label="Select all orders"></th>' if check else ""
    body = []
    for r in rows[:limit]:
        oid, name, mail, product, amount, tone, status, when = r
        c = f'<td class="is-check"><input type="checkbox" name="ids" value="{oid}" aria-label="Select {oid}"></td>' if check else ""
        body.append(f"""<tr>{c}
          <td class="is-nowrap"><b class="mn-mono">{oid}</b><span class="mn-cell-sub">{when}</span></td>
          <td><span class="mn-cell-title">{name}</span><span class="mn-cell-sub mn-truncate" style="max-width:28ch">{mail}</span></td>
          <td><span class="mn-cell-title" title="{product}">{product}</span></td>
          <td class="is-right is-nowrap mn-num"><b>{amount}</b></td>
          <td>{badge(tone, status)}</td>
          {'<td class="is-right"><button type="button" class="mn-btn mn-btn-ghost mn-btn-sm mn-btn-icon" aria-label="Edit ' + oid + '">' + icon("edit") + '</button></td>' if check else ''}
        </tr>""")
    return f"""<div class="mn-table-wrap"><table class="mn-table">
      <thead><tr>{head_check}<th>Order</th><th>Customer</th><th>Product</th><th class="is-right">Amount</th><th>Status</th>{'<th class="is-right"><span class="mn-sr-only">Actions</span></th>' if check else ''}</tr></thead>
      <tbody>{"".join(body)}</tbody></table></div>"""


def build():
    # ---------- Dashboard ----------
    days = [42, 58, 51, 77, 64, 88, 96]
    admin("index.html", "Dashboard", f"""
      <div class="mn-grid mn-grid-4" style="margin-bottom:var(--mn-space-5)">
        {kpi("wallet", "", "Revenue today", "$2,480.50", '<span class="mn-up">+12.4%</span> vs yesterday')}
        {kpi("receipt", "success", "Orders", "184", '<span class="mn-up">+8</span> since 9:00')}
        {kpi("trend", "warning", "Net profit (month)", "$18,920", "Margin 31%")}
        {kpi("package", "danger", "Low stock", "3 products", "Restock soon")}
      </div>
      <div class="mn-grid mn-grid-main">
        <div class="mn-stack">
          <section class="mn-card">
            <div class="mn-card-head"><div><h2>Sales, last 7 days</h2><p>Orders per day · today highlighted</p></div><a class="mn-link" href="analytics.html">Analytics {icon("arrow-right", "mn-icon-sm")}</a></div>
            <div class="mn-card-body">{bars(days, ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Today"])}</div>
          </section>
          <section class="mn-card">
            <div class="mn-card-head"><div><h2>Recent orders</h2><p>Latest 5 transactions</p></div><a class="mn-btn mn-btn-outline mn-btn-sm" href="table.html">View all</a></div>
            {orders_table(ORDERS, limit=5)}
          </section>
        </div>
        <div class="mn-stack">
          <section class="mn-card">
            <div class="mn-card-head"><div><h2>Stock</h2><p>Codes / licenses left</p></div><a class="mn-link" href="import.html">Import</a></div>
            <div class="mn-meter-row"><span>Cloud Storage 100 GB</span><b class="mn-num">128</b><div class="mn-meter is-success" style="--v:.86"><i></i></div></div>
            <div class="mn-meter-row"><span>Streaming Pass · 30 days</span><b class="mn-num">41</b><div class="mn-meter is-success" style="--v:.55"><i></i></div></div>
            <div class="mn-meter-row"><span>Design Asset Pack</span><b class="mn-num">4</b><div class="mn-meter is-warning" style="--v:.12"><i></i></div></div>
            <div class="mn-meter-row"><span>Domain .com · 1 year</span><b class="mn-num">0</b><div class="mn-meter is-danger" style="--v:.02"><i></i></div></div>
          </section>
          <div class="mn-alert mn-alert-warning" role="status">{icon("alert")}<div><b>Domain .com is out of stock</b><p>It shows as “Sold out” in the store. <a href="import.html">Import new codes</a>.</p></div><button type="button" class="mn-btn mn-btn-ghost mn-btn-sm mn-btn-icon" data-mn-dismiss aria-label="Dismiss">{icon("x")}</button></div>
          <section class="mn-card">
            <div class="mn-card-head"><div><h2>Top products</h2><p>This month</p></div></div>
            <div class="mn-meter-row"><span>Cloud Storage 100 GB</span><span class="mn-num mn-muted">412 sold</span><div class="mn-meter" style="--v:1"><i></i></div></div>
            <div class="mn-meter-row"><span>Streaming Pass · 30 days</span><span class="mn-num mn-muted">288 sold</span><div class="mn-meter" style="--v:.7"><i></i></div></div>
            <div class="mn-meter-row"><span>E-book Bundle</span><span class="mn-num mn-muted">96 sold</span><div class="mn-meter" style="--v:.23"><i></i></div></div>
          </section>
        </div>
      </div>""", head_actions=f'<a class="mn-btn mn-btn-outline" href="reports.html">{icon("download")}Export</a><a class="mn-btn mn-btn-primary" href="form.html">{icon("plus")}New product</a>')

    # ---------- Orders table ----------
    admin("table.html", "Orders", f"""
      <section class="mn-card">
        <div class="mn-toolbar">
          <div class="mn-segment" role="group" aria-label="Filter by status">
            <a href="#" aria-current="page">All</a><a href="#">Paid</a><a href="#">Pending</a><a href="#">Failed</a>
          </div>
          <label class="mn-search"><span class="mn-sr-only">Search orders</span>{icon("search")}<input class="mn-input" type="search" placeholder="Order, customer, product"></label>
        </div>
        <div class="mn-bulkbar" data-mn-check-bar="ids" hidden><span><b data-mn-check-count="ids">0</b> selected</span><span class="mn-spacer"></span><button type="button" class="mn-btn mn-btn-danger mn-btn-sm" data-mn-modal-open="confirm-delete">{icon("trash")}Delete selected</button></div>
        {orders_table(ORDERS, check=True)}
        <div class="mn-pagination"><span>Showing 1–8 of 1,284</span><nav aria-label="Pagination"><a href="#" aria-label="Previous page">{icon("arrow-left", "mn-icon-sm")}</a><span aria-current="page">1</span><a href="#">2</a><a href="#">3</a><a href="#" aria-label="Next page">{icon("arrow-right", "mn-icon-sm")}</a></nav></div>
      </section>
      <section class="mn-card" style="margin-top:var(--mn-space-5)">
        <div class="mn-card-head"><div><h2>Empty state</h2><p>What a table shows when a filter has no results</p></div></div>
        <div class="mn-empty">{icon("search")}<b>No refunds yet</b>Refunded orders will appear here.<br><a class="mn-btn mn-btn-outline" href="#">Clear filters</a></div>
      </section>
      <dialog class="mn-modal" id="confirm-delete" aria-labelledby="confirm-title">
        <div class="mn-modal-body"><h2 id="confirm-title">Delete selected orders?</h2><p>This removes them from the list. This can’t be undone.</p></div>
        <div class="mn-card-foot"><button type="button" class="mn-btn mn-btn-outline" data-mn-modal-close>Cancel</button><button type="button" class="mn-btn mn-btn-danger" data-mn-modal-close>{icon("trash")}Delete</button></div>
      </dialog>""", crumbs=[("index.html", "Dashboard"), (None, "Store")],
          head_actions=f'<a class="mn-btn mn-btn-outline" href="reports.html">{icon("download")}CSV</a>')

    # ---------- Product form ----------
    admin("form.html", "New product", f"""
      <form class="mn-grid mn-grid-main" onsubmit="event.preventDefault();Menara.toast('Saved (demo)')" novalidate>
        <section class="mn-card">
          <div class="mn-card-head"><div><h2>Product details</h2><p>What buyers see in the store</p></div></div>
          <div class="mn-card-body">
            <div class="mn-field"><label class="mn-label" for="name">Name <span class="mn-req" aria-hidden="true">*</span></label><input class="mn-input" id="name" value="Cloud Storage 100 GB" required></div>
            <div class="mn-form-grid">
              <div class="mn-field"><label class="mn-label" for="price">Price</label><div class="mn-input-group"><span>$</span><input class="mn-input mn-num" id="price" inputmode="decimal" value="12.00"></div></div>
              <div class="mn-field"><label class="mn-label" for="cost">Cost <span class="mn-muted">(optional)</span></label><div class="mn-input-group"><span>$</span><input class="mn-input mn-num" id="cost" inputmode="decimal" value="7.50"></div><p class="mn-help">Used to calculate profit in reports.</p></div>
              <div class="mn-field"><label class="mn-label" for="cat">Category</label><select class="mn-select" id="cat"><option>Storage</option><option>Streaming</option><option>Design</option><option>Books</option></select></div>
              <div class="mn-field"><label class="mn-label" for="slug">URL slug</label><input class="mn-input is-invalid" id="slug" value="cloud storage" aria-invalid="true" aria-describedby="slug-err"><p class="mn-error" id="slug-err">Use lowercase letters, numbers and dashes only.</p></div>
            </div>
            <div class="mn-field"><label class="mn-label" for="desc">Description</label><textarea class="mn-textarea" id="desc">100 GB of private cloud storage for 30 days. Instant activation code.</textarea></div>
            <label class="mn-file"><input type="file" accept="image/*">{icon("upload", "mn-icon-lg")}<b>Upload a cover image</b><span>PNG or JPG, up to 2 MB</span></label>
          </div>
        </section>
        <div class="mn-stack">
          <section class="mn-card">
            <div class="mn-card-head"><div><h2>Visibility</h2></div></div>
            <div class="mn-card-body">
              <label class="mn-switch"><input type="checkbox" checked> Show in store</label><br>
              <label class="mn-switch"><input type="checkbox"> Mark as “Best seller”</label>
              <fieldset style="border:0;padding:0;margin-top:var(--mn-space-3)"><legend class="mn-label">Delivery</legend>
                <label class="mn-check"><input type="radio" name="delivery" checked> Instant code</label><br>
                <label class="mn-check"><input type="radio" name="delivery"> Manual by admin</label>
              </fieldset>
            </div>
          </section>
          <div class="mn-alert mn-alert-info">{icon("info")}<div>Prices are shown with tax included. Change the currency in <a href="settings.html">Settings</a>.</div></div>
        </div>
        <div class="mn-card mn-card-foot" style="grid-column:1/-1;border-radius:var(--mn-radius-lg)"><a class="mn-btn mn-btn-ghost" href="index.html">Cancel</a><button class="mn-btn mn-btn-primary">{icon("check")}Save product</button></div>
      </form>""", crumbs=[("index.html", "Dashboard"), (None, "Products")])

    # ---------- Import ----------
    admin("import.html", "Import codes", f"""
      <div class="mn-grid mn-grid-2">
        <section class="mn-card">
          <div class="mn-card-head"><div><h2>Paste codes</h2><p>One per line, or paste a table from a spreadsheet</p></div></div>
          <div class="mn-card-body">
            <div class="mn-field"><label class="mn-label" for="prod">Product</label><select class="mn-select" id="prod"><option>Design Asset Pack</option><option>Cloud Storage 100 GB</option></select></div>
            <div class="mn-field"><label class="mn-label" for="codes">Codes</label><textarea class="mn-textarea mn-mono" id="codes" rows="8">K7QX-22LM-90PA
B8RT-41NW-77ZE
K7QX-22LM-90PA
H2CV-63DS-15KO</textarea></div>
          </div>
          <div class="mn-card-foot"><button type="button" class="mn-btn mn-btn-outline">{icon("eye")}Preview</button><button type="button" class="mn-btn mn-btn-primary" onclick="Menara.toast('Imported 3 codes (demo)')">{icon("upload")}Import 3 codes</button></div>
        </section>
        <section class="mn-card">
          <div class="mn-card-head"><div><h2>Preview</h2><p>Checked before anything is saved</p></div><span class="mn-badge mn-badge-success">3 new</span></div>
          <div class="mn-table-wrap"><table class="mn-table">
            <thead><tr><th>#</th><th>Code</th><th>Result</th></tr></thead>
            <tbody>
              <tr><td>1</td><td class="mn-mono">K7QX-22LM-90PA</td><td>{badge("success", "New")}</td></tr>
              <tr><td>2</td><td class="mn-mono">B8RT-41NW-77ZE</td><td>{badge("success", "New")}</td></tr>
              <tr><td>3</td><td class="mn-mono">K7QX-22LM-90PA</td><td>{badge("warning", "Duplicate in paste")}</td></tr>
              <tr><td>4</td><td class="mn-mono">H2CV-63DS-15KO</td><td>{badge("success", "New")}</td></tr>
            </tbody></table></div>
          <div class="mn-card-body"><div class="mn-alert mn-alert-warning">{icon("alert")}<div><b>1 duplicate skipped</b>Codes already in this paste or in another product are never imported twice.</div></div></div>
        </section>
      </div>""", crumbs=[("index.html", "Dashboard"), (None, "Store")])

    # ---------- Reports ----------
    admin("reports.html", "Reports", f"""
      <section class="mn-card" style="margin-bottom:var(--mn-space-5)"><div class="mn-toolbar" style="border:0">
        <div class="mn-segment" role="group" aria-label="Period"><a href="#">Today</a><a href="#">7 days</a><a href="#" aria-current="page">This month</a><a href="#">Last month</a></div>
        <span class="mn-spacer"></span><a class="mn-btn mn-btn-outline" href="#">{icon("download")}Export CSV</a></div></section>
      <div class="mn-grid mn-grid-4" style="margin-bottom:var(--mn-space-5)">
        {kpi("wallet", "", "Gross sales", "$61,040", "1,284 orders")}
        {kpi("tag", "warning", "Cost of goods", "$42,120", "69% of sales")}
        {kpi("trend", "success", "Net profit", "$18,920", "Avg $14.74 / order")}
        {kpi("receipt", "danger", "Refunds", "$212", "6 orders")}
      </div>
      <section class="mn-card">
        <div class="mn-card-head"><div><h2>By product</h2><p>This month</p></div></div>
        <div class="mn-table-wrap"><table class="mn-table">
          <thead><tr><th>Product</th><th class="is-right">Sold</th><th class="is-right">Sales</th><th class="is-right">Profit</th><th class="is-right">Margin</th></tr></thead>
          <tbody>
            <tr><td>Cloud Storage 100 GB</td><td class="is-right mn-num">412</td><td class="is-right mn-num">$4,944</td><td class="is-right mn-num mn-up">$1,854</td><td class="is-right mn-num">37%</td></tr>
            <tr><td>Streaming Pass · 30 days</td><td class="is-right mn-num">288</td><td class="is-right mn-num">$2,736</td><td class="is-right mn-num mn-up">$864</td><td class="is-right mn-num">32%</td></tr>
            <tr><td>Enterprise license · 500 seats</td><td class="is-right mn-num">1</td><td class="is-right mn-num">$12,480,000</td><td class="is-right mn-num mn-up">$3,744,000</td><td class="is-right mn-num">30%</td></tr>
            <tr><td>Domain .com · 1 year</td><td class="is-right mn-num">96</td><td class="is-right mn-num">$1,151</td><td class="is-right mn-num mn-down">−$12</td><td class="is-right mn-num">−1%</td></tr>
          </tbody></table></div>
      </section>""", crumbs=[("index.html", "Dashboard"), (None, "Overview")])

    # ---------- Analytics ----------
    month = [12, 18, 15, 22, 30, 26, 19, 24, 28, 35, 31, 27, 33, 41, 38, 29, 36, 44, 40, 47, 52, 49, 45, 58, 61, 55, 63, 70, 66, 72]
    hours = [2, 1, 1, 0, 0, 1, 3, 6, 9, 12, 14, 13, 15, 16, 14, 13, 15, 18, 22, 26, 31, 28, 17, 8]
    admin("analytics.html", "Analytics", f"""
      <div class="mn-grid mn-grid-4" style="margin-bottom:var(--mn-space-5)">
        {kpi("users", "", "Visitors", "8,412", "unique per day")}
        {kpi("eye", "", "Page views", "21,980", "2.6 per visitor")}
        {kpi("cart", "success", "Purchases", "1,284", "this month")}
        {kpi("trend", "warning", "Conversion", "15.3%", "visitors who bought")}
      </div>
      <div class="mn-grid mn-grid-main">
        <div class="mn-stack">
          <section class="mn-card"><div class="mn-card-head"><div><h2>Visitors per day</h2><p>Last 30 days</p></div></div>
            <div class="mn-card-body">{bars(month, [str(i) if i % 5 == 0 else "" for i in range(1, 31)], dense=True, show=False)}</div></section>
          <section class="mn-card"><div class="mn-card-head"><div><h2>Busy hours</h2><p>Page views per hour · peak highlighted</p></div></div>
            <div class="mn-card-body">{bars(hours, [f"{h:02d}" if h % 3 == 0 else "" for h in range(24)], current=hours.index(max(hours)), dense=True, show=False)}</div></section>
          <section class="mn-card"><div class="mn-card-head"><div><h2>Purchase funnel</h2><p>Where visitors drop off</p></div></div>
            <div class="mn-card-body mn-funnel">
              <div class="mn-funnel-row"><div><b>Visited store</b><span class="mn-num">8,412</span></div><div class="mn-meter" style="--v:1"><i></i></div></div>
              <div class="mn-funnel-row"><div><b>Opened a product</b><span class="mn-num">4,630 · 55%</span></div><div class="mn-meter" style="--v:.55"><i></i></div><span class="mn-funnel-drop">45% left at this step</span></div>
              <div class="mn-funnel-row"><div><b>Started checkout</b><span class="mn-num">1,902 · 23%</span></div><div class="mn-meter is-warning" style="--v:.23"><i></i></div><span class="mn-funnel-drop">59% left at this step</span></div>
              <div class="mn-funnel-row"><div><b>Paid</b><span class="mn-num">1,284 · 15%</span></div><div class="mn-meter is-success" style="--v:.15"><i></i></div></div>
            </div></section>
        </div>
        <div class="mn-stack">
          <section class="mn-card"><div class="mn-card-head"><div><h2>Traffic sources</h2><p>Tag links with <code>?ref=</code></p></div></div>
            <div class="mn-meter-row"><b>Social</b><span class="mn-num">46%</span><div class="mn-meter" style="--v:.46"><i></i></div></div>
            <div class="mn-meter-row"><b>Direct</b><span class="mn-num">28%</span><div class="mn-meter" style="--v:.28"><i></i></div></div>
            <div class="mn-meter-row"><b>Search</b><span class="mn-num">17%</span><div class="mn-meter" style="--v:.17"><i></i></div></div>
            <div class="mn-meter-row"><b>Other sites</b><span class="mn-num">9%</span><div class="mn-meter" style="--v:.09"><i></i></div></div></section>
          <section class="mn-card"><div class="mn-card-head"><div><h2>Devices</h2></div></div>
            <div class="mn-meter-row"><b>Phone</b><span class="mn-num">81%</span><div class="mn-meter" style="--v:.81"><i></i></div></div>
            <div class="mn-meter-row"><b>Desktop</b><span class="mn-num">16%</span><div class="mn-meter" style="--v:.16"><i></i></div></div>
            <div class="mn-meter-row"><b>Tablet</b><span class="mn-num">3%</span><div class="mn-meter" style="--v:.03"><i></i></div></div></section>
        </div>
      </div>""", crumbs=[("index.html", "Dashboard"), (None, "Overview")],
          head_actions='<div class="mn-segment" role="group" aria-label="Period"><a href="#">Today</a><a href="#" aria-current="page">30 days</a><a href="#">This month</a></div>')

    # ---------- Settings (tabs) ----------
    admin("settings.html", "Settings", f"""
      <section class="mn-card mn-tabs" data-mn-tabs>
        <div role="tablist" aria-label="Settings sections">
          <button type="button" role="tab" id="t-general" aria-controls="p-general" aria-selected="true">{icon("settings", "mn-icon-sm")}General</button>
          <button type="button" role="tab" id="t-pay" aria-controls="p-pay" aria-selected="false">{icon("wallet", "mn-icon-sm")}Payments</button>
          <button type="button" role="tab" id="t-notify" aria-controls="p-notify" aria-selected="false">{icon("bell", "mn-icon-sm")}Notifications</button>
        </div>
        <div role="tabpanel" id="p-general" aria-labelledby="t-general" class="mn-card-body">
          <div class="mn-form-grid">
            <div class="mn-field"><label class="mn-label" for="sname">Store name</label><input class="mn-input" id="sname" value="Menara Store"></div>
            <div class="mn-field"><label class="mn-label" for="cur">Currency</label><select class="mn-select" id="cur"><option>USD ($)</option><option>EUR (€)</option><option>IDR (Rp)</option></select></div>
            <div class="mn-field"><label class="mn-label" for="mail">Support email</label><input class="mn-input" id="mail" type="email" value="support@example.com"></div>
            <div class="mn-field"><label class="mn-label" for="tz">Time zone</label><select class="mn-select" id="tz"><option>UTC+07:00 Jakarta</option><option>UTC+00:00 London</option></select></div>
          </div>
          <label class="mn-switch"><input type="checkbox" checked> Show announcement banner in store</label>
        </div>
        <div role="tabpanel" id="p-pay" aria-labelledby="t-pay" class="mn-card-body" hidden>
          <div class="mn-alert mn-alert-success" style="margin-bottom:var(--mn-space-4)">{icon("check")}<div><b>Connected</b>Test transaction created successfully.</div></div>
          <div class="mn-field"><label class="mn-label" for="key">API key</label><input class="mn-input mn-mono" id="key" type="password" placeholder="Saved ••••4f2a · leave empty to keep"><p class="mn-help">Stored encrypted. Never shown again after saving.</p></div>
          <label class="mn-switch"><input type="checkbox"> Sandbox mode</label>
        </div>
        <div role="tabpanel" id="p-notify" aria-labelledby="t-notify" class="mn-card-body" hidden>
          <label class="mn-switch"><input type="checkbox" checked> Email me on every sale</label><br>
          <label class="mn-switch"><input type="checkbox" checked> Low stock alerts</label><br>
          <label class="mn-switch"><input type="checkbox"> Daily summary at 21:00</label>
        </div>
        <div class="mn-card-foot"><button type="button" class="mn-btn mn-btn-outline">{icon("zap")}Send test</button><button type="button" class="mn-btn mn-btn-primary" onclick="Menara.toast('Settings saved (demo)')">{icon("check")}Save</button></div>
      </section>""")

    # ---------- Users ----------
    users = [("AR", "Ari Rahman", "ari@example.com", "Owner", "primary", "Active now"),
             ("NK", "Nadia Kusuma", "nadia@example.com", "Admin", "info", "2 h ago"),
             ("JM", "Jonas Müller", "jonas@example.com", "Support", "neutral", "Yesterday")]
    rows = "".join(f"""<tr><td><div class="mn-row" style="flex-wrap:nowrap"><span class="mn-avatar">{i}</span><div style="min-width:0"><span class="mn-cell-title">{n}</span><span class="mn-cell-sub">{m}</span></div></div></td>
      <td>{badge(t, r)}</td><td class="mn-muted is-nowrap">{s}</td>
      <td class="is-right"><button type="button" class="mn-btn mn-btn-ghost mn-btn-sm mn-btn-icon" aria-label="Edit {n}">{icon("edit")}</button></td></tr>""" for i, n, m, r, t, s in users)
    admin("users.html", "Users", f"""
      <div class="mn-grid mn-grid-main">
        <section class="mn-card"><div class="mn-card-head"><div><h2>Team</h2><p>People who can sign in to this dashboard</p></div></div>
          <div class="mn-table-wrap"><table class="mn-table"><thead><tr><th>Name</th><th>Role</th><th>Last seen</th><th class="is-right"><span class="mn-sr-only">Actions</span></th></tr></thead><tbody>{rows}</tbody></table></div></section>
        <form class="mn-card" onsubmit="event.preventDefault();Menara.toast('Invite sent (demo)')">
          <div class="mn-card-head"><div><h2>Invite someone</h2><p>They get an email with a sign-in link</p></div></div>
          <div class="mn-card-body">
            <div class="mn-field"><label class="mn-label" for="iname">Name</label><input class="mn-input" id="iname" autocomplete="off"></div>
            <div class="mn-field"><label class="mn-label" for="imail">Email</label><input class="mn-input" id="imail" type="email" autocomplete="off"></div>
            <div class="mn-field"><label class="mn-label" for="irole">Role</label><select class="mn-select" id="irole"><option>Admin</option><option>Support</option></select></div>
          </div>
          <div class="mn-card-foot"><button class="mn-btn mn-btn-primary">{icon("mail")}Send invite</button></div>
        </form>
      </div>""", crumbs=[("index.html", "Dashboard"), (None, "Settings")])

    # ---------- 404 ----------
    admin("404.html", "Page not found", f"""
      <div class="mn-error-page"><div><div class="mn-error-code">404</div><h2 style="margin:var(--mn-space-3) 0 var(--mn-space-2)">We can’t find that page</h2>
      <p class="mn-muted">It may have moved, or the link is mistyped.</p>
      <div class="mn-row" style="justify-content:center;margin-top:var(--mn-space-5)"><a class="mn-btn mn-btn-primary" href="index.html">{icon("home")}Back to dashboard</a><a class="mn-btn mn-btn-outline" href="../store/index.html">Visit store</a></div></div></div>""")

    # ---------- Login (no shell) ----------
    write("admin/login.html", f"""{head("Sign in", "../")}
<body>
<main class="mn-auth" id="main">
  <section class="mn-auth-side" aria-hidden="true">
    <span class="mn-brand" style="height:auto;padding:0;border:0">{'<span class="mn-brand-mark">' + icon("tower") + '</span><span><b>Menara</b><small>Admin</small></span>'}</span>
    <div><h2>Run your store from one calm place.</h2><p>Orders, stock, payments and reports, made readable on any screen.</p></div>
    <span style="font-size:var(--mn-text-xs);opacity:.7">© 2026 Menara</span>
  </section>
  <div class="mn-auth-main">
    <form class="mn-auth-card" action="index.html">
      <div class="mn-row" style="justify-content:space-between;margin-bottom:var(--mn-space-7)">{brand("../index.html").replace('class="mn-brand"', 'class="mn-brand" style="height:auto;padding:0;border:0;color:var(--mn-ink)"')}{theme_button()}</div>
      <h1>Welcome back</h1><p class="mn-muted" style="margin-bottom:var(--mn-space-6)">Sign in to manage your store.</p>
      <div class="mn-field"><label class="mn-label" for="u">Username or email</label><input class="mn-input" id="u" autocomplete="username" required></div>
      <div class="mn-field"><label class="mn-label" for="p">Password</label><input class="mn-input" id="p" type="password" autocomplete="current-password" required></div>
      <div class="mn-row" style="justify-content:space-between;margin-bottom:var(--mn-space-5)"><label class="mn-check"><input type="checkbox"> Remember me</label><a href="#" class="mn-link">Forgot password?</a></div>
      <button class="mn-btn mn-btn-primary mn-btn-lg mn-btn-block">Sign in</button>
      <p class="mn-help" style="text-align:center;margin-top:var(--mn-space-5)">Demo only: any input goes to the dashboard.</p>
    </form>
  </div>
</main>
{foot("../")}""")
