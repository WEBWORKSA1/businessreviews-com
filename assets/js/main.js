/* BusinessReviews.com — core site behaviour (no dependencies) */
(function () {
  "use strict";
  var d = document, w = window;

  /* ---------- Contact routing (address is never written in page source) ---------- */
  var _k = [116,118,106,53,115,112,104,116,110,71,56,104,122,114,121,118,126,105,108,126];
  function inbox() { return _k.slice().reverse().map(function (c) { return String.fromCharCode(c - 7); }).join(""); }

  /* Optional payment links for donations — paste hosted links here (PayPal.me, Stripe Payment Link, Ko-fi, etc.) */
  var DONATE_LINKS = w.BR_DONATE_LINKS || { stripe: "", paypal: "", kofi: "" };

  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }

  /* ---------- Theme ---------- */
  var root = d.documentElement;
  var saved = store("br-theme");
  if (saved) root.setAttribute("data-theme", saved);
  else if (w.matchMedia && w.matchMedia("(prefers-color-scheme: dark)").matches) root.setAttribute("data-theme", "dark");
  d.addEventListener("click", function (e) {
    var t = e.target.closest("[data-theme-toggle]");
    if (!t) return;
    var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", next); store("br-theme", next);
  });

  /* ---------- Mobile nav ---------- */
  var nav = d.getElementById("nav"), scrim = d.getElementById("scrim"), mb = d.getElementById("menuBtn");
  function closeNav() { if (!nav) return; nav.classList.remove("open"); scrim.classList.remove("show"); mb && mb.setAttribute("aria-expanded", "false"); }
  if (mb) mb.addEventListener("click", function () {
    var open = !nav.classList.contains("open");
    nav.classList.toggle("open", open); scrim.classList.toggle("show", open); mb.setAttribute("aria-expanded", String(open));
  });
  if (scrim) scrim.addEventListener("click", closeNav);
  d.addEventListener("keydown", function (e) { if (e.key === "Escape") { closeNav(); closeModal(); } });

  /* ---------- Mail links: <a data-mail="Subject"> ---------- */
  d.addEventListener("click", function (e) {
    var a = e.target.closest("[data-mail]");
    if (!a) return;
    e.preventDefault();
    var subj = a.getAttribute("data-mail") || "Inquiry from BusinessReviews.com";
    w.location.href = "mailto:" + inbox() + "?subject=" + encodeURIComponent(subj);
  });

  /* ---------- Forms: <form data-form="Lead: Get matched"> ---------- */
  function serialize(form) {
    var fd = new FormData(form), o = {};
    fd.forEach(function (v, k) {
      if (k === "_honey") return;
      if (o[k]) o[k] = o[k] + ", " + v; else o[k] = v;
    });
    return o;
  }
  function status(form, ok, msg) {
    var s = form.querySelector(".form-status");
    if (!s) { s = d.createElement("div"); s.className = "form-status"; s.setAttribute("role", "status"); form.appendChild(s); }
    s.className = "form-status " + (ok ? "ok" : "err"); s.textContent = msg;
  }
  d.addEventListener("submit", function (e) {
    var form = e.target.closest("form[data-form]");
    if (!form) return;
    e.preventDefault();
    if (form.querySelector("[name=_honey]") && form.querySelector("[name=_honey]").value) return;
    if (!form.checkValidity()) { form.reportValidity(); return; }
    var rating = form.querySelector("[name=rating]");
    if (rating && rating.required && !rating.value) { status(form, false, "Choose a star rating before you submit."); return; }
    var data = serialize(form);
    var topic = form.getAttribute("data-form");
    data._subject = "[BusinessReviews.com] " + topic;
    data._template = "table";
    data._captcha = "false";
    data.page = location.href;
    data.submitted_at = new Date().toISOString();
    var btn = form.querySelector("[type=submit]"), label = btn ? btn.textContent : "";
    if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }
    fetch("https://formsubmit.co/ajax/" + inbox(), {
      method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data)
    }).then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, j: j }; }); })
      .then(function (res) {
        if (!res.ok || String(res.j.success) === "false") throw new Error(res.j.message || "send failed");
        status(form, true, form.getAttribute("data-ok") || "Thanks — your submission was received. We reply within 2 business days.");
        form.reset(); resetStars(form); resetSteps(form);
        if (w.gtag) w.gtag("event", "generate_lead", { form: topic });
      })
      .catch(function () {
        status(form, false, "We couldn't send that automatically. Opening your email app so nothing is lost…");
        var body = Object.keys(data).filter(function (k) { return k[0] !== "_"; }).map(function (k) { return k + ": " + data[k]; }).join("\n");
        setTimeout(function () { w.location.href = "mailto:" + inbox() + "?subject=" + encodeURIComponent(data._subject) + "&body=" + encodeURIComponent(body); }, 900);
      })
      .then(function () { if (btn) { btn.disabled = false; btn.textContent = label; } });
  });

  /* ---------- Star rating inputs ---------- */
  var starSvg = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3l-5.9 3.3 1.3-6.6L2.5 9.4l6.6-.8z"/></svg>';
  var words = ["", "Bad", "Poor", "Average", "Great", "Excellent"];
  function paint(box, n) { box.querySelectorAll("button").forEach(function (b, i) { b.classList.toggle("on", i < n); b.setAttribute("aria-pressed", String(i < n && i === n - 1)); }); }
  d.querySelectorAll("[data-rate]").forEach(function (box) {
    var input = d.getElementById(box.getAttribute("data-rate")), cap = box.parentNode.querySelector(".star-caption");
    for (var i = 1; i <= 5; i++) {
      var b = d.createElement("button"); b.type = "button"; b.innerHTML = starSvg; b.setAttribute("aria-label", i + " star" + (i > 1 ? "s" : "") + " — " + words[i]);
      (function (n) {
        b.addEventListener("click", function () { box.dataset.v = n; if (input) input.value = n; paint(box, n); if (cap) cap.textContent = n + " of 5 — " + words[n]; box.dispatchEvent(new CustomEvent("rated", { detail: n })); });
        b.addEventListener("mouseenter", function () { paint(box, n); });
      })(i);
      box.appendChild(b);
    }
    box.addEventListener("mouseleave", function () { paint(box, +box.dataset.v || 0); });
  });
  function resetStars(form) { form.querySelectorAll("[data-rate]").forEach(function (b) { b.dataset.v = 0; paint(b, 0); var c = b.parentNode.querySelector(".star-caption"); if (c) c.textContent = ""; }); }

  /* Hero stars: route to write-review with rating preset */
  var hs = d.getElementById("heroStars");
  if (hs) hs.addEventListener("rated", function (e) {
    var go = d.getElementById("heroGo");
    if (go) { go.href = go.getAttribute("data-base") + "?rating=" + e.detail; go.focus(); }
  });

  /* ---------- Multi-step forms ---------- */
  function initSteps(form) {
    var panes = form.querySelectorAll(".step-pane"); if (!panes.length) return;
    var bar = form.querySelector(".progress span"), cur = 0, lbl = form.querySelector("[data-step-label]");
    function show(i) {
      panes.forEach(function (p, j) { p.classList.toggle("active", j === i); });
      cur = i; if (bar) bar.style.width = ((i + 1) / panes.length * 100) + "%";
      if (lbl) lbl.textContent = "Step " + (i + 1) + " of " + panes.length;
      var f = panes[i].querySelector("input,select,textarea"); if (f && i > 0) f.focus({ preventScroll: true });
    }
    form.addEventListener("click", function (e) {
      if (e.target.closest("[data-next]")) {
        var fields = panes[cur].querySelectorAll("input,select,textarea"), ok = true;
        for (var k = 0; k < fields.length; k++) { if (!fields[k].checkValidity()) { fields[k].reportValidity(); ok = false; break; } }
        var hid = panes[cur].querySelector("input[type=hidden][required]");
        if (ok && hid && !hid.value) { status(form, false, "Choose a star rating to continue."); ok = false; }
        var group = panes[cur].querySelector("[data-require-one]");
        if (!ok) {} else if (group && !group.querySelector("input:checked")) { status(form, false, "Pick at least one option to continue."); ok = false; }
        else { var s = form.querySelector(".form-status"); if (s) s.className = "form-status"; }
        if (ok && cur < panes.length - 1) show(cur + 1);
      }
      if (e.target.closest("[data-prev]") && cur > 0) show(cur - 1);
    });
    form._showStep = show; show(0);
  }
  function resetSteps(form) { if (form._showStep) form._showStep(0); }
  d.querySelectorAll("form").forEach(initSteps);

  /* ---------- Prefill from query string (?business=, ?category=, ?rating=, ?amount=) ---------- */
  var qs = new URLSearchParams(location.search);
  ["business", "category", "amount", "role", "plan", "package"].forEach(function (k) {
    var v = qs.get(k); if (!v) return;
    d.querySelectorAll('[name="' + k + '"]').forEach(function (el) {
      if (el.type === "radio") { if (el.value === v) el.checked = true; }
      else el.value = v;
    });
  });
  if (qs.get("rating")) {
    var r = +qs.get("rating"), box = d.querySelector("[data-rate=reviewRating]");
    if (box && r >= 1 && r <= 5) { var bt = box.querySelectorAll("button")[r - 1]; bt && bt.click(); }
  }

  /* ---------- Donation links ---------- */
  d.querySelectorAll("[data-donate]").forEach(function (a) {
    var url = DONATE_LINKS[a.getAttribute("data-donate")];
    if (url) { a.href = url; a.hidden = false; a.target = "_blank"; a.rel = "noopener"; }
  });
  d.querySelectorAll("[data-amount]").forEach(function (b) {
    b.addEventListener("click", function () {
      var f = d.getElementById("pledgeAmount"); if (f) { f.value = b.getAttribute("data-amount"); f.scrollIntoView({ behavior: "smooth", block: "center" }); f.focus({ preventScroll: true }); }
    });
  });

  /* ---------- Lazy YouTube ---------- */
  d.querySelectorAll(".vid[data-yt]").forEach(function (v) {
    var id = v.getAttribute("data-yt");
    v.innerHTML = '<img loading="lazy" alt="" src="https://i.ytimg.com/vi/' + id + '/hqdefault.jpg"><div class="play"><span><svg width="22" height="22" viewBox="0 0 24 24" fill="#12213A"><path d="M8 5v14l11-7z"/></svg></span></div>';
    v.setAttribute("role", "button"); v.setAttribute("tabindex", "0");
    function play() { v.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" title="' + (v.getAttribute("aria-label") || "Video") + '" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'; }
    v.addEventListener("click", play);
    v.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); play(); } });
  });

  /* ---------- Cookie notice ---------- */
  var ck = d.getElementById("cookie");
  if (ck && !store("br-consent")) ck.classList.add("show");
  d.addEventListener("click", function (e) {
    var c = e.target.closest("[data-consent]"); if (!c) return;
    store("br-consent", c.getAttribute("data-consent")); ck && ck.classList.remove("show");
  });

  /* ---------- Sticky CTA + exit-intent lead modal ---------- */
  var sc = d.getElementById("stickyCta");
  if (sc) w.addEventListener("scroll", function () { sc.classList.toggle("show", w.scrollY > 900); }, { passive: true });
  var modal = d.getElementById("leadModal");
  function openModal() { if (!modal || store("br-modal")) return; modal.classList.add("show"); store("br-modal", String(Date.now())); var f = modal.querySelector("input,select"); f && f.focus(); }
  function closeModal() { modal && modal.classList.remove("show"); }
  w.BR_closeModal = closeModal;
  if (modal) {
    modal.addEventListener("click", function (e) { if (e.target === modal || e.target.closest("[data-close]")) closeModal(); });
    var last = +store("br-modal") || 0; if (last && Date.now() - last > 7 * 864e5) { try { localStorage.removeItem("br-modal"); } catch (e) {} }
    if (w.matchMedia("(pointer:fine)").matches) d.addEventListener("mouseout", function (e) { if (!e.relatedTarget && e.clientY < 8) openModal(); });
  }

  /* ---------- Site search (header + search page) ---------- */
  var idx = null;
  function loadIdx(cb) {
    if (idx) return cb(idx);
    var base = d.documentElement.getAttribute("data-root") || "";
    fetch(base + "search-index.json").then(function (r) { return r.json(); }).then(function (j) { idx = j; cb(j); }).catch(function () { cb([]); });
  }
  function score(item, terms) {
    var hay = (item.t + " " + item.k + " " + item.d).toLowerCase(), s = 0;
    terms.forEach(function (t) { if (item.t.toLowerCase().indexOf(t) > -1) s += 5; if (hay.indexOf(t) > -1) s += 1; else s -= 3; });
    return s;
  }
  var out = d.getElementById("results");
  if (out) {
    var q = (qs.get("q") || "").trim(), qi = d.getElementById("q"); if (qi) qi.value = q;
    if (!q) out.innerHTML = '<p class="muted">Type a business, tool or topic above — for example “CRM”, “payroll”, or “fake reviews”.</p>';
    else loadIdx(function (items) {
      var terms = q.toLowerCase().split(/\s+/).filter(Boolean);
      var hits = items.map(function (it) { return { it: it, s: score(it, terms) }; }).filter(function (h) { return h.s > 0; }).sort(function (a, b) { return b.s - a.s; }).slice(0, 40);
      var base = d.documentElement.getAttribute("data-root") || "";
      if (!hits.length) { out.innerHTML = '<div class="notice"><strong>No matches for “' + q.replace(/</g, "&lt;") + '”.</strong> Try a broader word, browse <a href="' + base + 'categories.html">all categories</a>, or <a href="' + base + 'write-review.html?business=' + encodeURIComponent(q) + '">write the first review of ' + q.replace(/</g, "&lt;") + '</a>.</div>'; return; }
      out.innerHTML = '<p class="muted">' + hits.length + ' result' + (hits.length > 1 ? "s" : "") + ' for “' + q.replace(/</g, "&lt;") + '”</p>' + hits.map(function (h) {
        return '<div class="result"><div class="kicker">' + h.it.y + '</div><a href="' + base + h.it.u + '">' + h.it.t + '</a><p class="muted" style="margin:.3em 0 0">' + h.it.d + '</p></div>';
      }).join("");
    });
  }

  /* ---------- Category filter ---------- */
  var cf = d.getElementById("catFilter");
  if (cf) cf.addEventListener("input", function () {
    var v = cf.value.toLowerCase();
    d.querySelectorAll("[data-cat]").forEach(function (c) { c.hidden = c.getAttribute("data-cat").indexOf(v) === -1; });
  });

  /* ---------- Year ---------- */
  d.querySelectorAll("[data-year]").forEach(function (y) { y.textContent = new Date().getFullYear(); });
})();
