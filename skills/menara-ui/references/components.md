# Components cheat-sheet

Copy these exactly. Live versions: `docs/components.html`.

## Buttons
`mn-btn` + one of `mn-btn-primary`, `mn-btn-accent`, `mn-btn-outline`, `mn-btn-ghost`, `mn-btn-danger`. Sizes `mn-btn-sm`, `mn-btn-lg`, `mn-btn-block`, `mn-btn-icon` (needs `aria-label`). Text link: `mn-link`.
```html
<button class="mn-btn mn-btn-primary"><svg class="mn-icon" aria-hidden="true"><use href="#i-plus"/></svg>New product</button>
```

## Cards and KPIs
```html
<section class="mn-card">
  <div class="mn-card-head"><div><h2>Title</h2><p>Subtitle</p></div><a class="mn-link" href="#">Action</a></div>
  <div class="mn-card-body">…</div>
  <div class="mn-card-foot"><button class="mn-btn mn-btn-primary">Save</button></div>
</section>
<div class="mn-card mn-kpi"><span class="mn-kpi-icon is-success"><svg class="mn-icon" aria-hidden="true"><use href="#i-wallet"/></svg></span>
  <div><span class="mn-kpi-label">Revenue</span><b class="mn-kpi-value">$2,480</b><span class="mn-kpi-meta"><span class="mn-up">+12%</span> vs yesterday</span></div></div>
```
`mn-kpi-icon` tones: default (primary), `is-success`, `is-warning`, `is-danger`. Trend text: `mn-up`, `mn-down`.

## Forms
`mn-field` > `mn-label` (+ `mn-req` star) + `mn-input` | `mn-select` | `mn-textarea` + `mn-help` or `mn-error`. Invalid: add `is-invalid` and `aria-invalid="true"` with `aria-describedby` pointing at the `mn-error`. Prefix: `mn-input-group` > `span` + `mn-input`. Search: `label.mn-search` > icon + `mn-input`. Two columns: `mn-form-grid`. Toggles: `label.mn-switch > input[type=checkbox]`, `label.mn-check > input`. Upload: `label.mn-file > input[type=file]`.

## Tables
```html
<div class="mn-table-wrap"><table class="mn-table">
  <thead><tr><th class="is-check"><input type="checkbox" data-mn-check-all="ids" aria-label="Select all"></th><th>Order</th><th class="is-right">Amount</th><th>Status</th></tr></thead>
  <tbody><tr><td class="is-check"><input type="checkbox" name="ids" aria-label="Select MN-1"></td>
    <td><span class="mn-cell-title">Name</span><span class="mn-cell-sub">meta</span></td>
    <td class="is-right mn-num">$12.00</td><td><span class="mn-badge mn-badge-success">Paid</span></td></tr></tbody>
</table></div>
```
Around it: `mn-toolbar` (filters with `mn-segment`, search), `mn-bulkbar` (`data-mn-check-bar`), `mn-pagination`. No rows: `mn-empty`.

## Status
Badges `mn-badge` + `mn-badge-success | -warning | -danger | -info | -neutral | -primary | -accent`; `mn-badge-plain` hides the dot. Alerts `mn-alert` + `mn-alert-success | -warning | -danger | -info`. Avatar `mn-avatar`. Toast via `Menara.toast()` (renders `mn-toast`).

## Data viz (CSS only)
Bars: `mn-bars` > `mn-bar[style="--v:.64"]` > `mn-bar-value`, `i`, `mn-bar-label`; highlight one with `is-current`; many bars: `mn-bars-dense`. Meters: `mn-meter-row` > text + `mn-meter[style="--v:.4"] > i` (tones `is-success`, `is-warning`, `is-danger`). Funnel: `mn-funnel` > `mn-funnel-row` (+ `mn-funnel-drop`).

## Navigation and overlays
Tabs: `mn-tabs` + `data-mn-tabs` (ARIA roles) or link tabs `mn-tablist`. Segmented filter `mn-segment` with `aria-current` / `aria-pressed`. Modal `dialog.mn-modal` > `mn-modal-body` + `mn-card-foot`. Dropdown `details.mn-dropdown > summary + mn-menu`. Breadcrumb `mn-crumbs`.

## Storefront
`mn-banner`, `mn-shop-header`, `mn-hero` (+ `mn-hero-chip`, `mn-hero-stats`), `mn-trust`, `mn-ticker` > `mn-ticker-track` > `mn-ticker-item` (+ `mn-ticker-dup` copy for the loop), `mn-section`, `mn-section-head`, `mn-products` > `mn-product` (`mn-product-media`, `mn-product-body`, `mn-price`, `is-soldout`), `mn-compare` (table with `is-best` row), `mn-steps` > `mn-step`, `mn-faq` (`details`), `mn-footer`, `mn-bottom-nav`, `mn-checkout`, `mn-summary` (`is-total`), `mn-qr`, `mn-countdown`, `mn-code`, `mn-success-mark`.

## Pages
Login `mn-auth` (`mn-auth-side`, `mn-auth-main`, `mn-auth-card`). Error `mn-error-page` + `mn-error-code`. Utilities: `mn-num`, `mn-mono`, `mn-muted`, `mn-truncate`, `mn-sr-only`, `mn-skip`, `mn-spacer`.
