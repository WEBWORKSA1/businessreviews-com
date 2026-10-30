/* BusinessReviews.com — free interactive tools */
(function () {
  "use strict";
  var d = document;
  function $(id) { return d.getElementById(id); }
  function val(id) { var e = $(id); return e ? e.value.trim() : ""; }
  function num(id) { var v = parseFloat(val(id)); return isNaN(v) ? 0 : v; }
  function copyBtn(btnId, outId) {
    var b = $(btnId); if (!b) return;
    b.addEventListener("click", function () {
      var t = $(outId).textContent;
      (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).then(function () { b.textContent = "Copied"; setTimeout(function () { b.textContent = "Copy text"; }, 1500); })
        .catch(function () { var r = d.createRange(); r.selectNodeContents($(outId)); var s = getSelection(); s.removeAllRanges(); s.addRange(r); });
    });
  }

  /* 1. Review response writer */
  var RR = {
    praise: {
      warm: ["Thank you so much, {name}! Reading this made our team's day.", "We're thrilled you enjoyed {thing}."],
      pro: ["Thank you for the review, {name}.", "We appreciate you taking the time to share your experience with {thing}."],
      brief: ["Thanks, {name}!", "Glad {thing} worked well for you."]
    },
    open: {
      service: "the service you received", product: "the product", price: "our pricing", wait: "the wait time", billing: "the billing process", staff: "your interaction with our team", other: "your experience"
    }
  };
  function respond() {
    var name = val("rrName") || "there", biz = val("rrBiz") || "our team", stars = +val("rrStars") || 5, issue = val("rrIssue"), tone = val("rrTone"), sign = val("rrSign") || "The " + biz + " team", detail = val("rrDetail");
    var thing = RR.open[issue] || "your experience", out = [];
    if (stars >= 4) {
      var p = RR.praise[tone] || RR.praise.pro;
      out.push(p[0].replace("{name}", name), p[1].replace("{thing}", thing === "your experience" ? "your visit" : thing) + (detail ? " It's great to hear that " + detail + "." : ""));
      if (stars === 4) out.push("If there's one thing we could have done to make it five stars, we'd genuinely like to know — just reply here or reach out directly.");
      out.push(tone === "brief" ? "See you again soon." : "We look forward to working with you again.");
    } else {
      out.push((tone === "warm" ? "Hi " + name + ", thank you for telling us about this — we're sorry " : name + ", thank you for your feedback. We're sorry ") + thing + " fell short of what you expected" + (detail ? ", especially " + detail : "") + ".");
      out.push(stars <= 2 ? "That isn't the standard we hold ourselves to, and we want to put it right." : "We take comments like yours seriously and are looking into what happened.");
      out.push("Please contact us directly with your order or account details so a manager can review this personally and follow up within one business day.");
      if (tone !== "brief") out.push("We appreciate the chance to make this right.");
    }
    out.push("— " + sign);
    $("rrOut").textContent = out.join(" ").replace(/\s+—/, "\n\n—");
  }
  if ($("rrForm")) { $("rrForm").addEventListener("input", respond); $("rrForm").addEventListener("submit", function (e) { e.preventDefault(); respond(); }); respond(); copyBtn("rrCopy", "rrOut"); }

  /* 2. Review request builder */
  function request() {
    var ch = val("rqChannel"), biz = val("rqBiz") || "our business", cust = val("rqCust") || "there", link = val("rqLink") || "[your review link]", what = val("rqWhat") || "your recent visit", txt;
    if (ch === "sms") txt = "Hi " + cust + ", thanks for choosing " + biz + "! Would you share a quick, honest review of " + what + "? It takes about a minute: " + link + "  Reply STOP to opt out.";
    else txt = "Subject: How did we do, " + cust + "?\n\nHi " + cust + ",\n\nThank you for choosing " + biz + ". We'd value your honest feedback on " + what + " — good or bad, it helps other customers decide and helps us improve.\n\nLeave a review (about 60 seconds): " + link + "\n\nWe don't offer rewards for reviews, and we read every one.\n\nThank you,\n" + biz;
    $("rqOut").textContent = txt;
  }
  if ($("rqForm")) { $("rqForm").addEventListener("input", request); request(); copyBtn("rqCopy", "rqOut"); }

  /* 3. Rating goal calculator */
  function goal() {
    var avg = num("rgAvg"), n = Math.round(num("rgCount")), target = num("rgTarget"), res = $("rgOut");
    if (!n || avg <= 0 || target <= 0) { res.innerHTML = "<p>Enter your current average, review count and target.</p>"; return; }
    if (target > 5 || avg > 5) { res.innerHTML = "<p>Ratings run from 1 to 5.</p>"; return; }
    if (avg >= target) { res.innerHTML = '<div class="big-num">0</div><p>You already meet a ' + target.toFixed(1) + '★ average. Keep the pace with steady review requests.</p>'; return; }
    if (target >= 5) { res.innerHTML = "<p>A perfect 5.0 can only be reached if every past review was 5★. Pick a target below 5.0 — research shows purchase likelihood tends to peak around 4.0–4.7 anyway.</p>"; return; }
    var need = Math.ceil((target * n - avg * n) / (5 - target));
    var mix = Math.ceil((target * n - avg * n) / (4.5 - target));
    res.innerHTML = '<div class="big-num">' + need.toLocaleString() + '</div><p>new 5★ reviews needed to lift ' + n.toLocaleString() + ' reviews from ' + avg.toFixed(2) + '★ to ' + target.toFixed(2) + '★.</p>' +
      (target < 4.5 ? '<p class="muted">With a realistic mix averaging 4.5★, plan for about <strong>' + mix.toLocaleString() + '</strong> new reviews.</p>' : '<p class="muted">Targets above 4.5★ assume nearly every new review is 5★.</p>') +
      '<p class="muted">At 10 requests a week and a typical 10–20% response rate, that is roughly ' + Math.ceil(need / 2) + '–' + Math.ceil(need / 1) + ' weeks.</p>';
  }
  if ($("rgForm")) { $("rgForm").addEventListener("input", goal); goal(); }

  /* 4. Vendor scorecard (weighted decision matrix) */
  function scorecard() {
    var tbl = $("scTable"); if (!tbl) return;
    var vendors = [].slice.call(tbl.querySelectorAll("thead input")).map(function (i, k) { return i.value || "Vendor " + String.fromCharCode(65 + k); });
    var totals = vendors.map(function () { return 0; }), wsum = 0;
    tbl.querySelectorAll("tbody tr").forEach(function (tr) {
      var wgt = parseFloat(tr.querySelector("[data-w]").value) || 0; wsum += wgt;
      tr.querySelectorAll("[data-s]").forEach(function (inp, k) { var s = Math.min(10, Math.max(0, parseFloat(inp.value) || 0)); totals[k] += s * wgt; });
    });
    var best = Math.max.apply(null, totals);
    $("scOut").innerHTML = vendors.map(function (v, k) {
      var pct = wsum ? totals[k] / (wsum * 10) * 100 : 0;
      return '<div style="margin:10px 0"><div style="display:flex;justify-content:space-between;font-weight:600"><span>' + v.replace(/</g, "&lt;") + (totals[k] === best && best > 0 ? ' <span class="tag">Top score</span>' : "") + '</span><span>' + pct.toFixed(0) + '/100</span></div><div class="bar"><span style="width:' + pct + '%"></span></div></div>';
    }).join("") + (wsum ? "" : '<p class="muted">Give each criterion a weight from 1 to 5.</p>');
  }
  if ($("scTable")) { $("scTable").addEventListener("input", scorecard); scorecard(); }

  /* 5. SaaS total cost of ownership */
  function tco() {
    var seats = num("tcSeats"), price = num("tcPrice"), months = num("tcMonths") || 36, setup = num("tcSetup"), train = num("tcTrain"), addons = num("tcAddons"), growth = num("tcGrowth") / 100, hike = num("tcHike") / 100;
    var lic = 0, s = seats, p = price;
    for (var m = 1; m <= months; m++) { lic += s * p; if (m % 12 === 0) { s = s * (1 + growth); p = p * (1 + hike); } }
    var add = addons * months, total = lic + add + setup + train;
    var perSeat = seats ? total / seats / (months / 12) : 0;
    function f(x) { return "$" + Math.round(x).toLocaleString(); }
    $("tcOut").innerHTML = '<div class="big-num">' + f(total) + '</div><p>estimated total cost over ' + months + ' months</p>' +
      '<table class="matrix"><tr><td>Licences</td><td>' + f(lic) + '</td></tr><tr><td>Add-ons &amp; integrations</td><td>' + f(add) + '</td></tr><tr><td>Implementation</td><td>' + f(setup) + '</td></tr><tr><td>Training &amp; change management</td><td>' + f(train) + '</td></tr><tr><td><strong>Per seat, per year</strong></td><td><strong>' + f(perSeat) + '</strong></td></tr></table>' +
      '<p class="muted" style="margin-top:10px">Licence share of total: ' + (total ? Math.round(lic / total * 100) : 0) + '%. If it is under 60%, negotiate implementation and add-on pricing as hard as the licence.</p>';
  }
  if ($("tcForm")) { $("tcForm").addEventListener("input", tco); tco(); }
})();
