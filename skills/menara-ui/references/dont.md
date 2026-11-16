# Don't

- **Don't invent styling.** No new buttons, cards or badges with one-off CSS. If a class exists, use it.
- **No raw colors** (`#2451c7`, `rgb(…)`) in markup or CSS. Use `var(--mn-…)` tokens so dark mode and rebranding keep working.
- **No emoji as icons.** Use the sprite: `<svg class="mn-icon"><use href="#i-name"/></svg>`.
- **No icon-only buttons without `aria-label`.** No inputs without a `<label>`.
- **No text under 12px.** No all-caps sentences. No brand-colored paragraphs.
- **No horizontal page scroll** at 360px. Wide tables go inside `mn-table-wrap`.
- **No color-only meaning.** Status badges carry a word, charts carry an `aria-label` with numbers.
- **No more than one primary button** per view or form.
- **No gradients, glows or heavy shadows** to "make it pop". Use `--mn-shadow-sm|md|lg` only.
- **No extra frameworks** (Bootstrap, Tailwind) on the same page. They fight the base styles.
- **No new JS libraries** for things `menara.js` already does: theme, drawer, modal, tabs, copy, select-all, countdown, toast.
- **Don't remove** the `data-mn-theme-init` head snippet (dark-mode flash), the skip link, or `aria-current` on the active nav item.
