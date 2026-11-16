"""Storefront / landing pages for a fictional digital-goods shop."""
from .shell import store, icon

PRODUCTS = [
    # name, big label, small, price, color var, badge, soldout
    ("Streaming Pass", "7", "days", "$3.00", "--mn-series-4", "", False),
    ("Cloud Storage", "100", "GB · 30 days", "$12.00", "--mn-series-1", "Best seller", False),
    ("E-book Bundle: Product Design for Busy Teams", "12", "e-books", "$24.00", "--mn-series-3", "", False),
    ("Cloud Storage", "1", "TB · 30 days", "$79.00", "--mn-series-5", "Best value", False),
    ("Domain .com", "1", "year", "$11.99", "--mn-series-2", "", True),
]


def product_card(p):
    name, big, small, price, color, badge, sold = p
    b = f'<span class="mn-badge mn-badge-accent mn-badge-plain">{badge}</span>' if badge else ""
    status = '<span class="mn-badge mn-badge-neutral">Sold out</span>' if sold else '<span class="mn-badge mn-badge-success">Instant delivery</span>'
    cls = " is-soldout" if sold else ""
    return f"""<a class="mn-product{cls}" href="product.html">{b}
      <div class="mn-product-media" style="background:var({color})"><div><b>{big}</b><small>{small}</small></div></div>
      <div class="mn-product-body"><h3>{name}</h3><span class="mn-price">{price}</span>{status}</div></a>"""


def build():
    ticker_items = [("Maya", "Cloud Storage 100 GB", "2 min ago"), ("Budi", "Streaming Pass", "5 min ago"), ("Sofia", "E-book Bundle", "9 min ago"),
                    ("Chen", "Cloud Storage 1 TB", "14 min ago"), ("Aisha", "Streaming Pass", "20 min ago"), ("Liam", "Domain .com", "31 min ago")]
    one = "".join(f'<span class="mn-ticker-item"><i></i><b>{n}</b> bought {p} · <span class="mn-muted">{t}</span></span>' for n, p, t in ticker_items)

    store("index.html", "Store", f"""
<section class="mn-hero">
  <span class="mn-hero-chip">{icon("zap", "mn-icon-sm")}Instant delivery</span>
  <h1>Digital goods, delivered in seconds.</h1>
  <p>Storage, streaming passes, e-books and domains. Pay once, get your code right away, any time of day.</p>
  <div class="mn-row"><a class="mn-btn mn-btn-accent mn-btn-lg" href="#products">Browse products {icon("arrow-right")}</a><a class="mn-btn mn-btn-outline mn-btn-lg" href="lookup.html">Track an order</a></div>
  <div class="mn-hero-stats"><div><b>12,400+</b>orders</div><div><b>24/7</b>always open</div><div><b>&lt; 1 min</b>delivery</div></div>
</section>

<div class="mn-trust">
  <div><span class="mn-kpi-icon">{icon("qr")}</span><div><b>Pay by QR or card</b><span>All major wallets and banks</span></div></div>
  <div><span class="mn-kpi-icon is-warning">{icon("zap")}</span><div><b>Instant code</b><span>Shown the moment you pay</span></div></div>
  <div><span class="mn-kpi-icon is-success">{icon("shield")}</span><div><b>Secure checkout</b><span>No account needed</span></div></div>
  <div><span class="mn-kpi-icon">{icon("headset")}</span><div><b>Real support</b><span>Replies within an hour</span></div></div>
</div>

<div class="mn-ticker" aria-label="Recent purchases"><div class="mn-ticker-track">{one}<span class="mn-ticker-dup" aria-hidden="true">{one}</span></div></div>

<section class="mn-section" id="products">
  <div class="mn-section-head"><h2>Products</h2><span class="mn-spacer"></span><div class="mn-segment" role="group" aria-label="Filter"><button type="button" aria-pressed="true">All</button><button type="button" aria-pressed="false">Storage</button><button type="button" aria-pressed="false">Media</button></div></div>
  <div class="mn-products">{"".join(product_card(p) for p in PRODUCTS)}</div>
</section>

<section class="mn-section">
  <div class="mn-section-head"><h2>Compare plans</h2><p>Same instant delivery, pick the size that fits.</p></div>
  <div class="mn-card"><div class="mn-table-wrap"><table class="mn-table mn-compare">
    <thead><tr><th>Plan</th><th class="is-right">Size</th><th class="is-right">Days</th><th class="is-right">Price</th><th class="is-right">Per GB</th></tr></thead>
    <tbody>
      <tr><td><b>Cloud 100</b></td><td class="is-right mn-num">100 GB</td><td class="is-right mn-num">30</td><td class="is-right mn-num">$12.00</td><td class="is-right mn-num">$0.120</td></tr>
      <tr class="is-best"><td><b>Cloud 1 TB</b> <span class="mn-badge mn-badge-accent mn-badge-plain">Best value</span></td><td class="is-right mn-num">1,000 GB</td><td class="is-right mn-num">30</td><td class="is-right mn-num">$79.00</td><td class="is-right mn-num"><b>$0.079</b></td></tr>
      <tr><td><b>Cloud 2 TB</b></td><td class="is-right mn-num">2,000 GB</td><td class="is-right mn-num">30</td><td class="is-right mn-num">$169.00</td><td class="is-right mn-num">$0.085</td></tr>
    </tbody></table></div></div>
</section>

<section class="mn-section">
  <div class="mn-section-head"><h2>How it works</h2></div>
  <div class="mn-steps">
    <div class="mn-step"><h3>Pick a product</h3><p>Choose a plan and enter your email to receive the receipt.</p></div>
    <div class="mn-step"><h3>Pay in one scan</h3><p>Scan the QR code with any wallet or banking app, or pay by card.</p></div>
    <div class="mn-step"><h3>Get your code</h3><p>Your code appears instantly and is also sent to your inbox.</p></div>
  </div>
</section>

<section class="mn-section" id="faq">
  <div class="mn-section-head"><h2>Questions</h2></div>
  <div class="mn-faq">
    <details open><summary>How fast will I get my code?</summary><p>Right after payment is confirmed, usually within a few seconds. Keep the page open, it updates by itself.</p></details>
    <details><summary>I paid but closed the page. What now?</summary><p>Open “My order”, enter your order number, and your code will be there. We also email it to you.</p></details>
    <details><summary>Can I get a refund?</summary><p>Unused codes can be refunded within 7 days. Contact support with your order number.</p></details>
  </div>
</section>""")

    store("product.html", "Cloud Storage 100 GB", f"""
<nav class="mn-crumbs" aria-label="Breadcrumb" style="margin-top:var(--mn-space-5)"><a href="index.html">Store</a> / <span>Cloud Storage 100 GB</span></nav>
<div class="mn-checkout">
  <section class="mn-card">
    <div class="mn-product-media" style="background:var(--mn-series-1);border-radius:var(--mn-radius-lg) var(--mn-radius-lg) 0 0;aspect-ratio:16/7"><div><b>100</b><small>GB · 30 days</small></div></div>
    <div class="mn-card-body">
      <div class="mn-row" style="margin-bottom:var(--mn-space-2)"><span class="mn-badge mn-badge-success">In stock · 128 left</span><span class="mn-badge mn-badge-accent mn-badge-plain">Best seller</span></div>
      <h1 style="font-size:var(--mn-text-2xl)">Cloud Storage 100 GB</h1>
      <p class="mn-price" style="margin:var(--mn-space-2) 0 var(--mn-space-4)">$12.00</p>
      <p class="mn-muted">Private cloud storage for 30 days. Activate with the code you receive, works on phone, tablet and desktop.</p>
      <ul style="margin-top:var(--mn-space-4);padding-left:var(--mn-space-5);display:grid;gap:var(--mn-space-1)">
        <li>100 GB, encrypted at rest</li><li>Active for 30 days from activation</li><li>Code delivered instantly</li>
      </ul>
    </div>
  </section>
  <form class="mn-card" action="pay.html" style="align-self:start">
    <div class="mn-card-head"><div><h2>Checkout</h2><p>No account needed</p></div></div>
    <div class="mn-card-body">
      <div class="mn-field"><label class="mn-label" for="email">Email <span class="mn-req" aria-hidden="true">*</span></label><input class="mn-input" id="email" type="email" autocomplete="email" placeholder="you@example.com" required aria-describedby="email-help"><p class="mn-help" id="email-help"><b>Use an email you can open.</b> Your receipt and code are sent here.</p></div>
      <div class="mn-field"><label class="mn-label" for="qty">Quantity</label><select class="mn-select" id="qty"><option>1</option><option>2</option><option>3</option></select></div>
      <div class="mn-summary"><div><span>Subtotal</span><span class="mn-num">$12.00</span></div><div><span>Service fee</span><span class="mn-num">$0.36</span></div><div class="is-total"><span>Total</span><span class="mn-num">$12.36</span></div></div>
    </div>
    <div class="mn-card-foot"><button class="mn-btn mn-btn-primary mn-btn-lg mn-btn-block">{icon("qr")}Pay with QR</button></div>
  </form>
</div>""", active="index.html#products")

    qr_cells = "".join(
        f'<rect x="{x}" y="{y}" width="1" height="1"/>' for y in range(25) for x in range(25)
        if ((x * 7 + y * 13 + x * y) % 5 < 2) and not ((x < 8 and y < 8) or (x > 16 and y < 8) or (x < 8 and y > 16)))
    finder = "".join(f'<rect x="{x}" y="{y}" width="7" height="7" fill="none" stroke="currentColor" stroke-width="1"/><rect x="{x + 2}" y="{y + 2}" width="3" height="3"/>' for x, y in [(0.5, 0.5), (17.5, 0.5), (0.5, 17.5)])
    store("pay.html", "Waiting for payment", f"""
<div class="mn-checkout" style="max-width:860px;margin-inline:auto">
  <section class="mn-card" style="text-align:center">
    <div class="mn-card-head"><div style="text-align:left"><h2>Scan to pay</h2><p>Order MN-24082 · Cloud Storage 100 GB</p></div><span class="mn-badge mn-badge-warning">Waiting</span></div>
    <div class="mn-card-body">
      <div class="mn-qr" role="img" aria-label="Payment QR code (demo placeholder)"><svg viewBox="0 0 25 25" fill="currentColor" shape-rendering="crispEdges">{finder}{qr_cells}</svg></div>
      <p class="mn-muted" style="margin-top:var(--mn-space-4)">Pay before the timer ends</p>
      <div class="mn-countdown" data-mn-countdown="1800">30:00</div>
    </div>
    <div class="mn-card-foot" style="justify-content:center"><a class="mn-btn mn-btn-outline" href="success.html">{icon("clock")}I’ve paid, check status</a></div>
  </section>
  <section class="mn-card" style="align-self:start">
    <div class="mn-card-head"><div><h2>Summary</h2></div></div>
    <div class="mn-card-body">
      <div class="mn-summary"><div><span>Product</span><span>Cloud Storage 100 GB</span></div><div><span>Order</span><span class="mn-mono">MN-24082</span></div><div><span>Email</span><span>you@example.com</span></div><div class="is-total"><span>Total</span><span class="mn-num">$12.36</span></div></div>
      <div class="mn-alert mn-alert-info" style="margin-top:var(--mn-space-5)">{icon("info")}<div>This page updates by itself after you pay. You can also close it and use <a href="lookup.html">My order</a> later.</div></div>
    </div>
  </section>
</div>""", banner=False)

    store("success.html", "Payment received", f"""
<section class="mn-card" style="max-width:560px;margin:var(--mn-space-7) auto;text-align:center">
  <div class="mn-card-body" style="padding:var(--mn-space-7) var(--mn-space-5)">
    <div class="mn-success-mark">{icon("check")}</div>
    <h1 style="font-size:var(--mn-text-2xl)">Payment received</h1>
    <p class="mn-muted" style="margin:var(--mn-space-2) 0 var(--mn-space-5)">Here is your activation code. We also sent it to you@example.com.</p>
    <div class="mn-code"><b id="code">K7QX-22LM-90PA</b><button type="button" class="mn-btn mn-btn-primary" data-mn-copy="#code">{icon("copy")}<span data-mn-copy-label>Copy code</span></button></div>
    <div class="mn-summary" style="text-align:left;margin-top:var(--mn-space-6)"><div><span>Product</span><span>Cloud Storage 100 GB</span></div><div><span>Order</span><span class="mn-mono">MN-24082</span></div><div><span>Paid</span><span class="mn-num">$12.36</span></div></div>
  </div>
  <div class="mn-card-foot" style="justify-content:center"><a class="mn-btn mn-btn-outline" href="index.html">Buy again</a><a class="mn-btn mn-btn-ghost" href="lookup.html">Find another order</a></div>
</section>""", banner=False)

    store("lookup.html", "Track an order", f"""
<section class="mn-card" style="max-width:520px;margin:var(--mn-space-7) auto">
  <div class="mn-card-head"><span class="mn-kpi-icon">{icon("receipt")}</span><div><h2>Track an order</h2><p>See the status and your code again</p></div></div>
  <form class="mn-card-body" action="success.html">
    <div class="mn-field"><label class="mn-label" for="order">Order number</label><input class="mn-input mn-mono" id="order" placeholder="MN-24082" autocapitalize="characters" required><p class="mn-help">It’s in your receipt email and at the top of the payment page.</p></div>
    <button class="mn-btn mn-btn-primary mn-btn-block mn-btn-lg">{icon("search")}Find my order</button>
  </form>
</section>""", active="lookup.html")
