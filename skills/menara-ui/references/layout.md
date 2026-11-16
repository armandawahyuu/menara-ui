# Layout

## Admin shell

```
.mn-app
├── aside.mn-sidebar          fixed, dark, 256px (--mn-sidebar-w)
│   ├── a.mn-brand > .mn-brand-mark + b + small
│   ├── nav.mn-nav > .mn-nav-label, a.mn-nav-link[aria-current="page"] (+ .mn-nav-count)
│   └── .mn-sidebar-foot
├── .mn-scrim                 backdrop for the mobile drawer
└── .mn-main
    ├── header.mn-topbar      sticky, 64px: burger (.mn-burger), .mn-search, .mn-topbar-actions
    └── main.mn-content#main  max 1240px
        ├── .mn-page-head     (.mn-crumbs + h1) left, actions right
        └── content
```

- Below 1024px the sidebar is a drawer. The burger (`mn-btn mn-btn-outline mn-btn-icon mn-burger` + `data-mn-sidebar-toggle`) opens it.
- Mark the current nav link with `aria-current="page"`.
- Group nav links under `.mn-nav-label` headings. Keep at most about 10 links.

## Grids

| Class | Use | Collapses |
|---|---|---|
| `mn-grid mn-grid-4` | KPI row | 2 columns below 1100px |
| `mn-grid mn-grid-main` | main column + side column | 1 column below 1100px |
| `mn-grid mn-grid-3` | even thirds | 1 column below 1100px |
| `mn-grid mn-grid-2` | halves | 1 column below 640px |
| `mn-stack` | vertical spacing inside a column | — |
| `mn-row` | inline cluster that wraps | — |
| `mn-form-grid` | 2-column form fields | 1 column below 640px |

## Storefront

`<body class="mn-shop">` → `.mn-banner` (optional) → `header.mn-shop-header > .mn-container` → `main.mn-container` → `footer.mn-footer` → `nav.mn-bottom-nav` (phones only, exactly 4 links). Sections: `.mn-section` with `.mn-section-head`. Checkout pages use `.mn-checkout` (2 columns, stacks below 860px).

## Rules

- 360px is the smallest width. Nothing may scroll sideways. Wide tables scroll inside `.mn-table-wrap`.
- Cards (`mn-card`) for summaries, tables (`mn-table`) for lists people scan or sort.
- One primary action per view (`mn-btn-primary`). Secondary actions are `mn-btn-outline` or `mn-btn-ghost`.
- Numbers right-aligned in tables (`is-right`) with `mn-num`.
- Long names: `mn-cell-title` (truncates with ellipsis) or let them wrap. Never let them push the layout wider.
- Spacing comes from tokens (`--mn-space-1` … `--mn-space-8`, 4px grid).
