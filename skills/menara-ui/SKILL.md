---
name: menara-ui
description: Build or edit pages with Menara UI, the plain HTML/CSS admin dashboard + storefront template (classes prefixed mn-, tokens prefixed --mn-). Use when creating admin dashboards, data tables, forms, settings, login pages, landing pages, storefronts, checkout or payment pages in a project that includes css/menara.css, or when the user mentions Menara UI. Covers layout, typography, color, components and what not to do.
---

# Menara UI

Menara UI is a no-build template: `css/tokens.css` (design tokens) + `css/menara.css` (components) + `js/menara.js` (behaviours and the icon sprite). Every page is plain HTML using `mn-` classes. Your job is to compose those classes, not to invent new styling.

## Workflow

1. **Find the closest existing page** in `admin/` or `store/` and copy its structure. It already has the shell, head snippet, skip link and script tag right.
2. **Compose with existing classes only.** Look them up in `references/components.md`. If something is truly missing, add a small rule to your own stylesheet using tokens (`var(--mn-…)`), never raw hex values.
3. **Follow the layout rules** in `references/layout.md` (app shell, grids, breakpoints, tables scroll inside `mn-table-wrap`).
4. **Type and color**: see `references/typography.md` and `references/color.md`. Body text is neutral ink, brand color is for actions and emphasis.
5. **Check `references/dont.md`** before you finish.
6. **Verify**: view the page at 360px wide and in dark mode (`<html data-theme="dark">`). Nothing may scroll sideways. Every icon-only button needs `aria-label`.

## Every page needs

```html
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Page · App</title>
  <script data-mn-theme-init>try{var t=localStorage.getItem('mn-theme');if(t)document.documentElement.setAttribute('data-theme',t)}catch(e){}</script>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;600;700;800&display=swap">
  <link rel="stylesheet" href="css/tokens.css">
  <link rel="stylesheet" href="css/menara.css">
</head>
<body>
  <a class="mn-skip" href="#main">Skip to content</a>
  …
  <script src="js/menara.js" defer></script>
</body>
```

## Icons

`<svg class="mn-icon" aria-hidden="true"><use href="#i-NAME"/></svg>`. The sprite is injected by `menara.js`. Names: home, chart, table, form, upload, download, file, settings, users, user, bell, search, plus, edit, trash, check, x, menu, sun, moon, copy, alert, info, zap, shield, clock, cart, tag, qr, arrow-right, arrow-left, logout, external, filter, eye, lock, mail, wifi, tower, package, receipt, wallet, trend, globe, headset, layers, palette, book, github. Size modifiers: `mn-icon-sm`, `mn-icon-lg`. Never use emoji as icons.

## Behaviours (data attributes)

- `data-mn-theme-toggle` on a button: switches light/dark, remembered.
- `data-mn-sidebar-toggle` on the burger: opens the mobile sidebar.
- `data-mn-modal-open="id"` + `<dialog class="mn-modal" id="id">` + `data-mn-modal-close`.
- `data-mn-tabs` on a wrapper with `role="tablist"`, `role="tab"` (with `aria-controls`) and `role="tabpanel"`.
- `data-mn-copy="text"` or `data-mn-copy="#id"`; optional inner `data-mn-copy-label`.
- `data-mn-check-all="name"` on a header checkbox; `data-mn-check-count="name"`, `data-mn-check-bar="name"` for a bulk bar.
- `data-mn-dismiss` inside an `mn-alert` or `mn-banner`.
- `data-mn-countdown="1800"` shows mm:ss.
- `Menara.toast("Saved")` from JS.
