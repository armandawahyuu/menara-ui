/*!
 * Menara UI v1.0.0 — tiny behaviours, no dependencies.
 * Everything is opt-in through data-mn-* attributes.
 * MIT License · https://github.com/armandawahyuu/menara-ui
 */
(function () {
  'use strict';


  /* Icon sprite (Lucide-style strokes, ISC — https://lucide.dev). Use: <svg class="mn-icon" aria-hidden="true"><use href="#i-name"/></svg> */
  var SPRITE = '<symbol id="i-home" viewBox="0 0 24 24"><path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/><path d="M10 21v-6h4v6"/></symbol><symbol id="i-chart" viewBox="0 0 24 24"><path d="M3 3v18h18"/><path d="M7 15v3"/><path d="M12 10v8"/><path d="M17 6v12"/></symbol><symbol id="i-table" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 10h18M9 10v10"/></symbol><symbol id="i-form" viewBox="0 0 24 24"><rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/></symbol><symbol id="i-upload" viewBox="0 0 24 24"><path d="M12 15V3"/><path d="m7 8 5-5 5 5"/><path d="M4 15v4a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-4"/></symbol><symbol id="i-download" viewBox="0 0 24 24"><path d="M12 3v12"/><path d="m7 10 5 5 5-5"/><path d="M4 15v4a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-4"/></symbol><symbol id="i-file" viewBox="0 0 24 24"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6"/></symbol><symbol id="i-settings" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/></symbol><symbol id="i-users" viewBox="0 0 24 24"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></symbol><symbol id="i-user" viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></symbol><symbol id="i-bell" viewBox="0 0 24 24"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.9 1.9 0 0 0 3.4 0"/></symbol><symbol id="i-search" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></symbol><symbol id="i-plus" viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></symbol><symbol id="i-edit" viewBox="0 0 24 24"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/></symbol><symbol id="i-trash" viewBox="0 0 24 24"><path d="M3 6h18"/><path d="M8 6V4h8v2"/><path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"/></symbol><symbol id="i-check" viewBox="0 0 24 24"><path d="M20 6 9 17l-5-5"/></symbol><symbol id="i-x" viewBox="0 0 24 24"><path d="M18 6 6 18M6 6l12 12"/></symbol><symbol id="i-menu" viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h16"/></symbol><symbol id="i-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></symbol><symbol id="i-moon" viewBox="0 0 24 24"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></symbol><symbol id="i-copy" viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></symbol><symbol id="i-alert" viewBox="0 0 24 24"><path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/></symbol><symbol id="i-info" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></symbol><symbol id="i-zap" viewBox="0 0 24 24"><path d="M13 2 3 14h9l-1 8 10-12h-9z"/></symbol><symbol id="i-shield" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></symbol><symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></symbol><symbol id="i-cart" viewBox="0 0 24 24"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.7 13.4a2 2 0 0 0 2 1.6h9.7a2 2 0 0 0 2-1.6L23 6H6"/></symbol><symbol id="i-tag" viewBox="0 0 24 24"><path d="M20.6 13.4 13.4 20.6a2 2 0 0 1-2.8 0L3 13V3h10l7.6 7.6a2 2 0 0 1 0 2.8z"/><path d="M7.5 7.5h.01"/></symbol><symbol id="i-qr" viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><path d="M14 14h3v3h-3zM20 14v.01M14 20h.01M17 20h4v-3"/></symbol><symbol id="i-arrow-right" viewBox="0 0 24 24"><path d="M5 12h14M13 5l7 7-7 7"/></symbol><symbol id="i-arrow-left" viewBox="0 0 24 24"><path d="M19 12H5M11 19l-7-7 7-7"/></symbol><symbol id="i-logout" viewBox="0 0 24 24"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><path d="m16 17 5-5-5-5M21 12H9"/></symbol><symbol id="i-external" viewBox="0 0 24 24"><path d="M15 3h6v6M10 14 21 3"/><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/></symbol><symbol id="i-filter" viewBox="0 0 24 24"><path d="M22 3H2l8 9.5V19l4 2v-8.5z"/></symbol><symbol id="i-eye" viewBox="0 0 24 24"><path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></symbol><symbol id="i-lock" viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></symbol><symbol id="i-mail" viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></symbol><symbol id="i-wifi" viewBox="0 0 24 24"><path d="M5 12.5a10 10 0 0 1 14 0M8.5 16a5 5 0 0 1 7 0M2 9a15 15 0 0 1 20 0"/><path d="M12 20h.01"/></symbol><symbol id="i-tower" viewBox="0 0 24 24"><path d="M12 2v4"/><path d="M8 22 12 6l4 16"/><path d="M9.5 16h5M10.5 11h3"/><path d="M5 5a9.5 9.5 0 0 0 0 9M19 5a9.5 9.5 0 0 1 0 9"/></symbol><symbol id="i-package" viewBox="0 0 24 24"><path d="M21 8 12 3 3 8v8l9 5 9-5z"/><path d="M3 8l9 5 9-5M12 13v8"/></symbol><symbol id="i-receipt" viewBox="0 0 24 24"><path d="M5 2v20l3-2 2 2 2-2 2 2 2-2 3 2V2l-3 2-2-2-2 2-2-2-2 2z"/><path d="M9 8h6M9 12h6M9 16h4"/></symbol><symbol id="i-wallet" viewBox="0 0 24 24"><path d="M20 7V5a2 2 0 0 0-2-2H5a2 2 0 0 0 0 4h15v14H5a2 2 0 0 1-2-2V5"/><path d="M16 14h.01"/></symbol><symbol id="i-trend" viewBox="0 0 24 24"><path d="m22 7-8.5 8.5-5-5L2 17"/><path d="M16 7h6v6"/></symbol><symbol id="i-globe" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></symbol><symbol id="i-headset" viewBox="0 0 24 24"><path d="M3 14v-2a9 9 0 0 1 18 0v2"/><path d="M21 16a2 2 0 0 1-2 2h-1v-6h3zM3 16a2 2 0 0 0 2 2h1v-6H3z"/><path d="M18 18a4 4 0 0 1-4 4h-2"/></symbol><symbol id="i-layers" viewBox="0 0 24 24"><path d="m12 2 10 5-10 5L2 7z"/><path d="m2 17 10 5 10-5M2 12l10 5 10-5"/></symbol><symbol id="i-palette" viewBox="0 0 24 24"><circle cx="13.5" cy="6.5" r="1"/><circle cx="17.5" cy="10.5" r="1"/><circle cx="8.5" cy="7.5" r="1"/><circle cx="6.5" cy="12.5" r="1"/><path d="M12 2a10 10 0 0 0 0 20c1.1 0 2-.9 2-2 0-.5-.2-1-.5-1.3-.3-.4-.5-.8-.5-1.3 0-1.1.9-2 2-2h2.3A5.6 5.6 0 0 0 22 10c0-4.4-4.5-8-10-8z"/></symbol><symbol id="i-book" viewBox="0 0 24 24"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V2H6.5A2.5 2.5 0 0 0 4 4.5z"/><path d="M4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/></symbol><symbol id="i-github" viewBox="0 0 24 24"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.9a3.4 3.4 0 0 0-.9-2.6c3.1-.3 6.4-1.5 6.4-7A5.4 5.4 0 0 0 20 4.8 5 5 0 0 0 19.9 1S18.7.6 16 2.5a13.4 13.4 0 0 0-7 0C6.3.6 5.1 1 5.1 1A5 5 0 0 0 5 4.8a5.4 5.4 0 0 0-1.5 3.7c0 5.5 3.3 6.7 6.4 7A3.4 3.4 0 0 0 9 18.1V22"/></symbol>';
  (function () {
    var holder = document.createElement('div');
    holder.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">' + SPRITE + '</svg>';
    document.body.insertBefore(holder.firstChild, document.body.firstChild);
  })();

  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) { /* private mode */ } }
  };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };

  /* Theme: <button data-mn-theme-toggle>. Initial theme is set by the inline head snippet (no flash). */
  function currentTheme() {
    var t = document.documentElement.getAttribute('data-theme');
    if (t) return t;
    return window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
  function syncThemeButtons() {
    var dark = currentTheme() === 'dark';
    $$('[data-mn-theme-toggle]').forEach(function (b) {
      b.setAttribute('aria-pressed', String(dark));
      b.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode');
      var use = b.querySelector('use');
      if (use) use.setAttribute('href', use.getAttribute('href').replace(/#i-(sun|moon)$/, dark ? '#i-sun' : '#i-moon'));
    });
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-mn-theme-toggle]');
    if (!b) return;
    var next = currentTheme() === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    store.set('mn-theme', next);
    syncThemeButtons();
  });

  /* Sidebar (mobile): <button data-mn-sidebar-toggle>, closes on scrim click / Escape. */
  function setNav(open) {
    var app = document.querySelector('.mn-app');
    if (!app) return;
    app.classList.toggle('is-nav-open', open);
    $$('[data-mn-sidebar-toggle]').forEach(function (b) { b.setAttribute('aria-expanded', String(open)); });
    if (open) { var first = app.querySelector('.mn-sidebar a'); if (first) first.focus(); }
  }
  document.addEventListener('click', function (e) {
    if (e.target.closest('[data-mn-sidebar-toggle]')) setNav(!document.querySelector('.mn-app.is-nav-open'));
    else if (e.target.classList && e.target.classList.contains('mn-scrim')) setNav(false);
  });

  /* Modal: <button data-mn-modal-open="id">, <dialog id class="mn-modal">, [data-mn-modal-close]. */
  var opener = null;
  document.addEventListener('click', function (e) {
    var o = e.target.closest('[data-mn-modal-open]');
    if (o) {
      var d = document.getElementById(o.getAttribute('data-mn-modal-open'));
      if (d && d.showModal) { opener = o; d.showModal(); }
      return;
    }
    var c = e.target.closest('[data-mn-modal-close]');
    if (c) { var dlg = c.closest('dialog'); if (dlg) dlg.close(); return; }
    if (e.target.tagName === 'DIALOG' && e.target.classList.contains('mn-modal')) e.target.close(); // backdrop click
  });
  $$('dialog.mn-modal').forEach(function (d) {
    d.addEventListener('close', function () { if (opener) { opener.focus(); opener = null; } });
  });

  /* Tabs: <div class="mn-tabs" data-mn-tabs> with role=tablist/tab/tabpanel and aria-controls. Arrow keys move. */
  $$('[data-mn-tabs]').forEach(function (root) {
    var tabs = $$('[role="tab"]', root);
    function select(tab, focus) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
        var panel = document.getElementById(t.getAttribute('aria-controls'));
        if (panel) panel.hidden = !on;
      });
      if (focus) tab.focus();
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { select(t); });
      t.addEventListener('keydown', function (e) {
        var n = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
        if (e.key === 'Home') n = -i; else if (e.key === 'End') n = tabs.length - 1 - i;
        if (n === undefined) return;
        e.preventDefault();
        select(tabs[(i + n + tabs.length) % tabs.length], true);
      });
    });
    select(tabs.filter(function (t) { return t.getAttribute('aria-selected') === 'true'; })[0] || tabs[0]);
  });

  /* Copy: <button data-mn-copy="text"> or data-mn-copy="#selector" (copies its text). */
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-mn-copy]');
    if (!b) return;
    var v = b.getAttribute('data-mn-copy');
    if (v.charAt(0) === '#') { var el = document.querySelector(v); v = el ? el.textContent.trim() : ''; }
    var done = function () {
      var label = b.querySelector('[data-mn-copy-label]') || b;
      var old = label.textContent;
      if (label === b && b.querySelector('svg')) { toast('Copied to clipboard'); return; }
      label.textContent = 'Copied!';
      setTimeout(function () { label.textContent = old; }, 1600);
    };
    if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(v).then(done, function () { fallbackCopy(v); done(); });
    else { fallbackCopy(v); done(); }
  });
  function fallbackCopy(text) {
    var t = document.createElement('textarea');
    t.value = text; t.setAttribute('readonly', ''); t.style.position = 'fixed'; t.style.opacity = '0';
    document.body.appendChild(t); t.select();
    try { document.execCommand('copy'); } catch (e) { /* ignore */ }
    document.body.removeChild(t);
  }

  /* Toast helper, also exposed as window.Menara.toast(message). */
  function toast(msg) {
    var el = document.createElement('div');
    el.className = 'mn-toast'; el.setAttribute('role', 'status');
    el.textContent = msg;
    document.body.appendChild(el);
    setTimeout(function () { el.remove(); }, 2600);
  }

  /* Select all: <input type=checkbox data-mn-check-all="ids[]"> toggles inputs with that name;
     an element [data-mn-check-count="ids[]"] shows how many are checked and [data-mn-check-bar="ids[]"] is shown when > 0. */
  function syncChecks(name) {
    var boxes = $$('input[type="checkbox"][name="' + name + '"]');
    var n = boxes.filter(function (b) { return b.checked; }).length;
    $$('[data-mn-check-all="' + name + '"]').forEach(function (all) {
      all.checked = n > 0 && n === boxes.length;
      all.indeterminate = n > 0 && n < boxes.length;
    });
    $$('[data-mn-check-count="' + name + '"]').forEach(function (el) { el.textContent = n; });
    $$('[data-mn-check-bar="' + name + '"]').forEach(function (el) { el.hidden = n === 0; });
  }
  document.addEventListener('change', function (e) {
    var t = e.target;
    if (t.hasAttribute && t.hasAttribute('data-mn-check-all')) {
      var name = t.getAttribute('data-mn-check-all');
      $$('input[type="checkbox"][name="' + name + '"]').forEach(function (b) { b.checked = t.checked; });
      syncChecks(name);
    } else if (t.type === 'checkbox' && t.name && document.querySelector('[data-mn-check-all="' + t.name + '"]')) {
      syncChecks(t.name);
    }
  });

  /* Dismiss: <button data-mn-dismiss> removes its closest .mn-alert / .mn-banner. */
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-mn-dismiss]');
    if (!b) return;
    var box = b.closest('.mn-alert, .mn-banner, [data-mn-dismissible]');
    if (box) box.remove();
  });

  /* Countdown: <span data-mn-countdown="1800"> → mm:ss, then "Expired". */
  $$('[data-mn-countdown]').forEach(function (el) {
    var end = Date.now() + parseInt(el.getAttribute('data-mn-countdown'), 10) * 1000;
    (function tick() {
      var s = Math.max(0, Math.round((end - Date.now()) / 1000));
      el.textContent = s ? String(Math.floor(s / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0') : 'Expired';
      if (s) setTimeout(tick, 1000);
    })();
  });

  /* Escape closes the mobile sidebar and open dropdowns. */
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    if (document.querySelector('.mn-app.is-nav-open')) setNav(false);
    $$('details.mn-dropdown[open]').forEach(function (d) { d.open = false; d.querySelector('summary').focus(); });
  });
  /* Click outside closes dropdowns. */
  document.addEventListener('click', function (e) {
    $$('details.mn-dropdown[open]').forEach(function (d) { if (!d.contains(e.target)) d.open = false; });
  });

  syncThemeButtons();
  window.Menara = { toast: toast };
})();
