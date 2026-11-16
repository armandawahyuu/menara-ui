# Typography

- **Font:** Rubik (Google Fonts, OFL) via `--mn-font`, falling back to `system-ui`. Monospace via `--mn-mono` for codes, IDs and API keys (`mn-mono`).
- **Scale:** `--mn-text-xs` 12px (the minimum, for meta and table headers), `--mn-text-sm` 13.5px (tables, labels, nav), `--mn-text-md` 15px (body), `--mn-text-lg` 17px, `--mn-text-xl` 21px (section titles), `--mn-text-2xl` 28px (page titles, KPI values), `--mn-text-3xl` 40px (hero, error codes).
- **Weights:** 400 body, 500 nav and labels, 600 buttons, table heads and card titles, 700 page titles and KPI values, 800 hero only.
- **Line height:** `--mn-leading` 1.55 for body. Headings 1.2.
- **Numbers:** add `mn-num` (tabular figures) to every amount, count and percentage in tables and KPIs so columns align.
- **Color of text:** body and headings use `--mn-ink`. Secondary text uses `--mn-muted` (`mn-muted`). Links and primary emphasis use `--mn-primary-text`. Don't make paragraphs or headings brand-blue.
- **Case:** sentence case for buttons, titles and labels ("Save product", not "SAVE PRODUCT"). Uppercase only for small table headers and nav section labels, which the CSS already handles.
- **Writing:** short, specific labels. A button says what happens ("Delete 3 orders"). Errors say what to do ("Use lowercase letters and dashes only").
