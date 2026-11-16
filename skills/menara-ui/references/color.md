# Color

All colors are tokens in `css/tokens.css`. Never write a hex value in component markup or CSS: use `var(--mn-…)`.

## Roles

| Token | Role |
|---|---|
| `--mn-primary` | primary buttons, focus ring, active states, chart bars, switches |
| `--mn-primary-hover` | hover of primary buttons |
| `--mn-primary-ink` | text and icons on top of `--mn-primary` |
| `--mn-primary-soft` | tinted backgrounds (selected row, soft badge, info chips) |
| `--mn-primary-text` | primary used as text on light surfaces (links) |
| `--mn-accent` / `--mn-accent-ink` | yellow highlight: current chart bar, best-value badge, store CTA, active-nav marker |
| `--mn-brand-surface` / `--mn-brand-surface-ink` | big brand areas: store header and hero (stays deep in dark mode) |
| `--mn-ink`, `--mn-muted`, `--mn-subtle` | text: main, secondary, placeholder |
| `--mn-bg`, `--mn-surface`, `--mn-surface-2` | page background, cards, table heads and subtle fills |
| `--mn-line`, `--mn-line-strong` | borders: cards and dividers, inputs |
| `--mn-success`, `--mn-warning`, `--mn-danger`, `--mn-info` (+ `-soft`) | status only: badges, alerts, meters |
| `--mn-series-1` … `--mn-series-5` | chart series |
| `--mn-sidebar-*` | the dark admin sidebar |

## Rules

- **Status colors mean status.** Green = paid or done, amber = waiting or low, red = failed, danger or destructive, info blue = neutral notice. Don't use them for decoration.
- **Never rely on color alone.** Badges carry a word, charts carry an `aria-label` with numbers.
- **Contrast:** text ≥ 4.5:1 in both themes. The tokens are tuned for that. If you rebrand `--mn-primary`, recheck white text on it and `--mn-primary-text` on white.
- **Dark mode is automatic** through tokens. Test it with `<html data-theme="dark">`. If you add custom CSS, use tokens so it follows.
- **Rebranding:** override `--mn-primary`, `--mn-primary-hover`, `--mn-primary-soft`, `--mn-primary-text` (and dark-mode values, including `--mn-brand-surface`) after `tokens.css`.
- Keep to one brand color plus the accent. No gradients on buttons or text.
