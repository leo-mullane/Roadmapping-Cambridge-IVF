/* ==========================================================================
   civf.js — Cambridge IVF prototype behaviour.
   Driven by ids and data attributes on the pages. Prices are those published
   on cambridge-ivf.nhs.uk/prices; anything else is marked as sample.
   ========================================================================== */
(function () {
  'use strict';

  function $(s, r) { return (r || document).querySelector(s); }
  function $all(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function money(n) { return '£' + Math.round(n).toLocaleString('en-GB'); }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }

  /* Context between pages: ?param= with a sessionStorage fallback for hosts that strip query strings. */
  function param(name) {
    var m = new RegExp('[?&]' + name + '=([^&#]*)').exec(window.location.search);
    var v = m ? decodeURIComponent(m[1]) : null;
    try {
      if (v) window.sessionStorage.setItem('civf-' + name, v);
      else v = window.sessionStorage.getItem('civf-' + name);
    } catch (e) { /* private mode */ }
    return v;
  }
  function remember(name, v) { try { window.sessionStorage.setItem('civf-' + name, v); } catch (e) { /* private mode */ } }

  var toastEl;
  function toast(msg) {
    if (!toastEl) {
      toastEl = document.createElement('div');
      toastEl.className = 'toast';
      toastEl.setAttribute('role', 'status');
      document.body.appendChild(toastEl);
    }
    toastEl.textContent = msg;
    toastEl.hidden = false;
    window.clearTimeout(toastEl._t);
    toastEl._t = window.setTimeout(function () { toastEl.hidden = true; }, 3200);
  }

  /* --- Data: packages and add-ons (prices from the live prices page) ----- */
  var PACKAGES = {
    first:   { name: 'First IVF', price: 2900, cycles: 1, stages: [2900], icsiIncluded: true, criteria: 'No previous IVF or natural pregnancy, 37 or under, AMH 6–35, BMI below 35' },
    pure:    { name: 'PURE IVF', price: 5240, cycles: 1, stages: [5240], criteria: '37 or under, AMH 6–35, BMI below 35' },
    pureduo: { name: 'PURE Duo', price: 7265, cycles: 2, stages: [5690, 1575], criteria: '37 or under, AMH 6–35, BMI below 35' },
    plus:    { name: 'IVF Plus', price: 6290, cycles: 1, stages: [6290], criteria: 'For people not eligible for PURE' },
    plusduo: { name: 'IVF Plus Duo', price: 8265, cycles: 2, stages: [6690, 1575], criteria: 'For people not eligible for PURE' },
    multi:   { name: 'Multi-Cycle IVF', price: 11540, cycles: 3, stages: [8390, 1575, 1575], criteria: 'Under 45, AMH under 50, BMI 18–35' }
  };
  var ADDONS = {
    picsi:  { name: 'PICSI and Zymot', price: 395, hfea: 'black', note: 'With ICSI only. HFEA: PICSI has no effect on the chance of a baby for most patients.' },
    macs:   { name: 'MACS ICSI', price: 1683, hfea: 'none', note: 'Replaces standard ICSI. Not on the HFEA list.' },
    calcium:{ name: 'Calcium ionophore', price: 127, hfea: 'none', note: 'For a small group with fertilisation failure. Your embryologist will say if it applies.' },
    era:    { name: 'Endometrial receptivity test', price: 1308, hfea: 'red', note: 'Includes a mock transfer cycle. HFEA: may reduce effectiveness or has safety concerns.' },
    dna:    { name: 'Sperm DNA fragmentation test', price: 462, hfea: 'grey', note: 'HFEA: not enough good evidence to rate.' }
  };
  var HFEA_LABEL = { green: 'Green: effective', amber: 'Amber: conflicting evidence', grey: 'Grey: not enough evidence', black: 'Black: no effect', red: 'Red: may reduce success or safety concerns', none: 'Not rated by the HFEA' };
  function badge(c) { return '<span class="hfea ' + c + '">' + HFEA_LABEL[c] + '</span>'; }

  /* --- 1 Clear costs: estimator --------------------------------------- */
  function initEstimator() {
    var form = $('#estimator');
    if (!form) return;
    var pre = param('package');
    if (pre && PACKAGES[pre]) { var r = $('input[name=pkg][value="' + pre + '"]', form); if (r) r.checked = true; }

    // Build add-on rows from data so the badges stay consistent with the evidence table.
    var host = $('#est-addons');
    host.innerHTML = Object.keys(ADDONS).map(function (k) {
      var a = ADDONS[k];
      return '<label class="cv-addon"><input type="checkbox" name="addon" value="' + k + '"><span><b>' + esc(a.name) + '</b> · ' + money(a.price) + '<br><span class="cv-muted">' + esc(a.note) + '</span></span>' + badge(a.hfea) + '</label>';
    }).join('');

    function val(name) { var c = $('input[name=' + name + ']:checked', form); return c ? c.value : null; }
    function update() {
      var p = PACKAGES[val('pkg') || 'pure'];
      remember('package', val('pkg') || 'pure');
      var icsi = val('icsi'), freeze = val('freeze');
      var lines = [], low = p.price, high = p.price;
      lines.push([p.name + (p.cycles > 1 ? ' (' + p.cycles + ' cycles)' : ''), money(p.price)]);
      if (p.icsiIncluded) {
        lines.push(['ICSI if needed', 'Included']);
      } else if (icsi === 'yes') {
        low += 1323 * p.cycles; high += 1323 * p.cycles;
        lines.push(['ICSI × ' + p.cycles, money(1323 * p.cycles)]);
      } else if (icsi === 'unsure') {
        high += 1323 * p.cycles;
        lines.push(['ICSI, if needed', 'up to ' + money(1323 * p.cycles)]);
      }
      if (freeze === 'yes') {
        low += 765; high += 765;
        lines.push(['Freezing spare embryos, first year storage', money(765)]);
      } else if (freeze === 'unsure') {
        high += 765;
        lines.push(['Freezing, if you have spare embryos', 'up to ' + money(765)]);
      }
      $all('input[name=addon]:checked', form).forEach(function (c) {
        var a = ADDONS[c.value];
        low += a.price; high += a.price;
        lines.push([a.name, money(a.price)]);
      });
      lines.push(['Lubion (progesterone), if prescribed', 'Not included', 'sub']);
      lines.push(['Storage from year two', '£346 a year', 'sub']);

      $('#est-total').textContent = low === high ? money(low) : money(low) + ' to ' + money(high);
      $('#est-lines').innerHTML = lines.map(function (l) { return '<li' + (l[2] ? ' class="sub"' : '') + '><span>' + esc(l[0]) + '</span><b>' + esc(l[1]) + '</b></li>'; }).join('');
      var extra = low - p.price;
      $('#est-stages').innerHTML = p.stages.map(function (s, i) {
        var amt = i === 0 ? s + extra : s;
        return '<li><span>' + (i === 0 ? 'Before cycle 1 starts' : 'Only if you go ahead with cycle ' + (i + 1)) + '</span><b>' + money(amt) + (i === 0 && high > low ? ' to ' + money(s + (high - p.price)) : '') + '</b></li>';
      }).join('');
      $('#est-criteria').textContent = p.criteria;
      var link = $('#est-book');
      if (link) link.setAttribute('href', link.getAttribute('data-base') + '?topic=costs&package=' + (val('pkg') || 'pure'));
    }
    form.addEventListener('change', update);
    update();

    var send = $('#est-send');
    if (send) send.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = $('#est-email');
      var err = $('#est-email-err');
      var ok = /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email.value);
      err.hidden = ok;
      email.setAttribute('aria-invalid', ok ? 'false' : 'true');
      if (ok) toast('Estimate sent to ' + email.value + ' (prototype: nothing is sent)');
    });
  }

  /* Comparison table: total or per cycle */
  function initCompare() {
    var t = $('#cmp');
    if (!t) return;
    $all('[data-cmp-mode]').forEach(function (b) {
      b.addEventListener('click', function () {
        var mode = b.getAttribute('data-cmp-mode');
        $all('[data-cmp-mode]').forEach(function (o) { o.setAttribute('aria-pressed', o === b ? 'true' : 'false'); });
        $all('[data-total]', t).forEach(function (td) {
          var total = +td.getAttribute('data-total'), cyc = +td.getAttribute('data-cycles');
          td.textContent = mode === 'cycle' ? money(total / cyc) + ' a cycle' : money(total);
        });
      });
    });
    var pre = param('package');
    if (pre) { var col = $all('[data-col="' + pre + '"]', t); col.forEach(function (c) { c.classList.add('hl'); }); }
  }

  /* Evidence table filter */
  function initEvidence() {
    var rows = $all('[data-hfea-row]');
    if (!rows.length) return;
    $all('[data-hfea-filter]').forEach(function (b) {
      b.addEventListener('click', function () {
        var v = b.getAttribute('data-hfea-filter');
        $all('[data-hfea-filter]').forEach(function (o) { o.setAttribute('aria-pressed', o === b ? 'true' : 'false'); });
        rows.forEach(function (r) { r.hidden = v !== 'all' && r.getAttribute('data-hfea-row') !== v; });
      });
    });
  }

  /* --- 2 Find your path ---------------------------------------------- */
  var ROUTES = {
    couple: { t: 'Heterosexual couples', from: 475, intro: 'Most couples start with a joint fertility assessment, then a consultation to agree a plan.', steps: ['Free information session', 'Couples fertility assessment (£475)', 'Results with a consultant', 'Treatment, often IVF or IUI'], pkg: 'pure' },
    female: { t: 'Female couples', from: 595, intro: 'You can choose donor IUI, IVF, or Shared Motherhood, where one partner provides the eggs and the other carries the pregnancy.', steps: ['Free information session', 'Assessment for both of you (£595)', 'Choose a donor', 'Implications counselling', 'Shared Motherhood or donor IVF'], pkg: 'pure' },
    single: { t: 'Single women', from: 375, intro: 'Treatment with donor sperm, by IUI or IVF depending on your assessment.', steps: ['Free information session', 'Fertility assessment (£375)', 'Choose a donor', 'Implications counselling', 'IUI or IVF'], pkg: 'pure' },
    men: { t: 'Single men and male couples', from: 189, intro: 'Start with a semen analysis and a consultation. We can talk you through surrogacy and donor eggs, and refer you on where we can\'t help directly.', steps: ['Semen analysis (£189)', 'Initial consultation (£220)', 'Plan, including donor eggs or referral'], pkg: null },
    trans: { t: 'Trans and non-binary people', from: 220, intro: 'Fertility preservation before transition, or treatment afterwards, planned around your care.', steps: ['Initial consultation (£220)', 'Egg or sperm freezing', 'Annual storage (£346)'], pkg: null },
    ahead: { t: 'Planning ahead', from: 3675, intro: 'Egg freezing for people who want to keep their options open.', steps: ['Free information session', 'Fertility assessment (£375)', 'Egg freezing cycle (from £3,675)', 'Storage from year two (£346 a year)'], pkg: null, link: 'egg-freezing.html' },
    nhs: { t: 'Referred by the NHS', from: 0, intro: 'Your GP or consultant refers you. Check whether your area funds treatment, and what to do if it doesn\'t.', steps: ['GP or consultant referral', 'NHS funding check', 'Assessment and consultation', 'NHS-funded cycle'], pkg: null },
    elsewhere: { t: 'Started treatment elsewhere', from: 220, intro: 'Moving clinics is more common than people think. Bring your records and we can transfer any frozen eggs or embryos.', steps: ['Send us your records', 'Review consultation (£220)', 'Transfer of eggs or embryos (if any)', 'Continue treatment'], pkg: null }
  };
  function initPath() {
    var tiles = $all('[data-route]');
    if (!tiles.length) return;
    var panel = $('#route-panel');
    function show(k, scroll) {
      var r = ROUTES[k];
      tiles.forEach(function (t) { t.setAttribute('aria-pressed', t.getAttribute('data-route') === k ? 'true' : 'false'); });
      remember('route', k);
      var next = r.link ? '<a class="btn" href="' + r.link + '">Explore egg freezing</a>'
        : r.pkg ? '<a class="btn" href="costs.html?package=' + r.pkg + '">See likely costs</a>'
        : '<a class="btn" href="start.html?topic=' + k + '">Talk to the team</a>';
      panel.innerHTML = '<p class="cv-eyebrow">Your likely route</p><h3>' + esc(r.t) + '</h3><p>' + esc(r.intro) + '</p>' +
        '<ol class="cv-route-steps">' + r.steps.map(function (s) { return '<li>' + esc(s) + '</li>'; }).join('') + '</ol>' +
        '<p class="cv-muted">' + (r.from ? 'First paid step from ' + money(r.from) + '.' : 'NHS-funded if you meet your area\'s criteria.') + ' Your consultant confirms the plan.</p>' +
        '<div class="row" style="margin-top:0.75rem">' + next + '<a class="btn btn-secondary" href="start.html?topic=session">Book a free information session</a></div>';
      panel.hidden = false;
      if (scroll) panel.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
    }
    tiles.forEach(function (t) { t.addEventListener('click', function () { show(t.getAttribute('data-route'), true); }); });
    var pre = param('route');
    if (pre && ROUTES[pre]) show(pre, false);
  }

  function initEligibility() {
    var f = $('#elig');
    if (!f) return;
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var age = +$('#el-age').value, amh = $('#el-amh').value, bmi = +$('#el-bmi').value;
      var prev = $('input[name=el-prev]:checked', f), err = $('#el-err');
      var bad = !age || age < 18 || age > 60 || !bmi || bmi < 12 || bmi > 70 || !prev;
      err.hidden = !bad;
      if (bad) { err.focus(); return; }
      prev = prev.value;
      var amhN = amh === '' ? null : +amh;
      var out, pkg;
      if (age <= 37 && bmi < 35 && (amhN === null || (amhN >= 6 && amhN <= 35))) {
        pkg = prev === 'none' ? 'first' : 'pure';
        out = prev === 'none'
          ? 'You may be eligible for <b>First IVF (£2,900)</b>, our package for people who haven\'t had IVF or a natural pregnancy before.'
          : 'You may be eligible for <b>PURE IVF (£5,240)</b> or <b>PURE Duo (£7,265 for two cycles)</b>.';
        if (amhN === null) out += ' We\'ll need an AMH blood test (£121) to confirm.';
      } else if (age < 45 && bmi <= 35 && (amhN === null || amhN < 50)) {
        pkg = 'plus';
        out = 'You\'re likely to be offered <b>IVF Plus (£6,290)</b> or <b>Multi-Cycle IVF (£11,540 for three cycles)</b>, which allow a higher dose of medication.';
      } else {
        pkg = null;
        out = 'Our packages may not fit, but treatment may still be possible. A consultation (£220) is the best next step, and some people are better served by donor eggs.';
      }
      if (bmi >= 35) out += ' Most packages need a BMI below 35; we can talk about support to get there.';
      $('#el-text').innerHTML = out;
      var a = $('#el-link');
      if (pkg) { a.hidden = false; a.setAttribute('href', 'costs.html?package=' + pkg); remember('package', pkg); } else { a.hidden = true; }
      var res = $('#el-result');
      res.hidden = false;
      res.focus();
    });
  }

  function initNhsCheck() {
    var sel = $('#nhs-area');
    if (!sel) return;
    var AREAS = {
      cp: 'Cambridgeshire and Peterborough ICB funds NHS IVF for people who meet its criteria. [Criteria to be confirmed from the ICB\'s current policy.]',
      herts: 'Hertfordshire and West Essex ICB funds NHS IVF for people who meet its criteria. [Criteria to be confirmed.]',
      suffolk: 'Suffolk and North East Essex ICB: we see NHS patients through our Ipswich satellite. [Criteria to be confirmed.]',
      other: 'We can\'t provide NHS-funded IVF for your area, but you can self-fund with us from £2,900, or ask your GP which clinics your ICB contracts with.'
    };
    function upd() {
      var out = $('#nhs-out');
      if (!sel.value) { out.hidden = true; return; }
      out.hidden = false;
      $('#nhs-text').textContent = AREAS[sel.value];
    }
    sel.addEventListener('change', upd);
  }

  /* Journey timeline: one step open at a time, NHS/self-funded view */
  function initJourney() {
    var steps = $all('.cv-step > button');
    if (!steps.length) return;
    steps.forEach(function (b) {
      b.addEventListener('click', function () {
        var body = b.nextElementSibling;
        var open = b.getAttribute('aria-expanded') === 'true';
        b.setAttribute('aria-expanded', open ? 'false' : 'true');
        body.hidden = open;
      });
    });
    $all('[data-fund]').forEach(function (b) {
      b.addEventListener('click', function () {
        var v = b.getAttribute('data-fund');
        $all('[data-fund]').forEach(function (o) { o.setAttribute('aria-pressed', o === b ? 'true' : 'false'); });
        $all('[data-fund-show]').forEach(function (el) { el.hidden = el.getAttribute('data-fund-show') !== v; });
      });
    });
  }

  /* --- 3 Start today ------------------------------------------------- */
  function validate(form) {
    var ok = true, first = null;
    $all('[data-req]', form).forEach(function (el) {
      var v = el.type === 'checkbox' ? el.checked : el.value.trim();
      var good = !!v;
      if (good && el.type === 'email') good = /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(el.value);
      if (good && el.getAttribute('data-req') === 'phone') good = /^[0-9 +()]{10,}$/.test(el.value);
      var err = document.getElementById(el.id + '-err');
      if (err) err.hidden = good;
      el.setAttribute('aria-invalid', good ? 'false' : 'true');
      if (!good && !first) first = el;
      ok = ok && good;
    });
    if (first) first.focus();
    return ok;
  }

  function initEnquiry() {
    var f = $('#enquiry');
    if (!f) return;
    var topic = param('topic');
    var map = { costs: 'ivf', couple: 'ivf', female: 'ivf', single: 'ivf', ahead: 'egg', men: 'andrology', trans: 'preserve', nhs: 'nhs', elsewhere: 'switch', session: '' };
    if (topic && map[topic]) $('#enq-topic').value = map[topic];
    var pkg = param('package');
    if (pkg && PACKAGES[pkg]) { var note = $('#enq-pkg'); note.hidden = false; note.textContent = 'You were looking at ' + PACKAGES[pkg].name + '. We\'ll include that with your enquiry.'; }
    if (topic === 'session') { var tab = $('[data-tab="tab-sessions"]'); if (tab) tab.click(); }
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!validate(f)) return;
      f.hidden = true;
      var c = $('#enq-done');
      $('#enq-name-out').textContent = $('#enq-name').value.split(' ')[0];
      c.hidden = false;
      c.focus();
    });
  }

  function nextDates(dow, n, startOffset) {
    var out = [], d = new Date();
    d.setHours(12, 0, 0, 0);
    d.setDate(d.getDate() + (startOffset || 1));
    while (out.length < n) {
      if (dow === null ? (d.getDay() !== 0 && d.getDay() !== 6) : d.getDay() === dow) out.push(new Date(d));
      d.setDate(d.getDate() + 1);
    }
    return out;
  }
  var DAY = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  var MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  function longDate(d) { return ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][d.getDay()] + ' ' + d.getDate() + ' ' + MON[d.getMonth()]; }

  function initCallBooking() {
    var days = $('#call-days');
    if (!days) return;
    var dates = nextDates(null, 8, 1), chosenDay = null, chosenTime = null;
    days.innerHTML = dates.map(function (d, i) { return '<button type="button" class="cv-day" data-i="' + i + '" aria-pressed="false">' + DAY[d.getDay()] + '<b>' + d.getDate() + '</b>' + MON[d.getMonth()] + '</button>'; }).join('');
    var slots = $('#call-slots');
    var TIMES = ['09:00', '09:30', '10:30', '11:00', '12:30', '14:00', '15:30', '16:30', '17:30'];
    function renderSlots(i) {
      slots.innerHTML = TIMES.map(function (t, k) {
        var taken = (i * 3 + k) % 4 === 0;
        return '<button type="button" class="cv-slot" data-t="' + t + '" aria-pressed="false"' + (taken ? ' disabled aria-label="' + t + ' taken"' : '') + '>' + t + '</button>';
      }).join('');
    }
    days.addEventListener('click', function (e) {
      var b = e.target.closest('.cv-day'); if (!b) return;
      $all('.cv-day', days).forEach(function (o) { o.setAttribute('aria-pressed', o === b ? 'true' : 'false'); });
      chosenDay = dates[+b.getAttribute('data-i')]; chosenTime = null;
      renderSlots(+b.getAttribute('data-i'));
      $('#call-slot-h').hidden = false;
      $('#call-form').hidden = true;
    });
    slots.addEventListener('click', function (e) {
      var b = e.target.closest('.cv-slot'); if (!b || b.disabled) return;
      $all('.cv-slot', slots).forEach(function (o) { o.setAttribute('aria-pressed', o === b ? 'true' : 'false'); });
      chosenTime = b.getAttribute('data-t');
      $('#call-when').textContent = longDate(chosenDay) + ' at ' + chosenTime;
      $('#call-form').hidden = false;
    });
    $('#call-form').addEventListener('submit', function (e) {
      e.preventDefault();
      if (!validate(e.target)) return;
      e.target.hidden = true;
      $('#call-done-when').textContent = longDate(chosenDay) + ' at ' + chosenTime;
      $('#call-done').hidden = false;
      $('#call-done').focus();
    });
  }

  function initSessions() {
    var host = $('#sessions');
    if (!host) return;
    var tues = nextDates(2, 3, 1);
    var items = tues.map(function (d) { return { d: d, t: 'Information session by phone', s: 'Tuesday evening · 15 minutes each with an embryologist, a fertility nurse and our finance manager', fmt: 'Phone' }; });
    var thu = nextDates(4, 3, 10)[2];
    items.splice(2, 0, { d: thu, t: 'Open evening at Kefford House', s: '6.30pm to 8pm · meet the team and see the clinic · [sample: proposed new format]', fmt: 'In person' });
    host.innerHTML = items.map(function (it, i) {
      return '<li class="cv-session"><div class="d">' + DAY[it.d.getDay()] + '<b>' + it.d.getDate() + '</b>' + MON[it.d.getMonth()] + '</div><div><b>' + esc(it.t) + '</b><br><span class="cv-muted">' + esc(it.s) + '</span><br><span class="badge">' + it.fmt + '</span></div>' +
        '<button type="button" class="btn" data-book-session="' + i + '" aria-expanded="false" aria-controls="sess-form-' + i + '">Book a place</button>' +
        '<form class="cv-inline-book cv-form" id="sess-form-' + i + '" hidden novalidate><div class="two"><div class="field"><label for="sn-' + i + '">Name</label><input id="sn-' + i + '" data-req autocomplete="name"><p class="field-error" id="sn-' + i + '-err" hidden>Enter your name</p></div>' +
        '<div class="field"><label for="se-' + i + '">Email</label><input id="se-' + i + '" type="email" data-req autocomplete="email"><p class="field-error" id="se-' + i + '-err" hidden>Enter a valid email address</p></div></div>' +
        '<div class="row"><button class="btn" type="submit">Confirm place</button><span class="cv-muted">We\'ll email a reminder the day before.</span></div></form></li>';
    }).join('');
    host.addEventListener('click', function (e) {
      var b = e.target.closest('[data-book-session]'); if (!b) return;
      var f = document.getElementById('sess-form-' + b.getAttribute('data-book-session'));
      var open = f.hidden;
      f.hidden = !open;
      b.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (open) f.querySelector('input').focus();
    });
    host.addEventListener('submit', function (e) {
      e.preventDefault();
      var f = e.target;
      if (!validate(f)) return;
      var li = f.closest('.cv-session');
      f.outerHTML = '<p class="cv-inline-book" role="status"><b>You\'re booked.</b> A confirmation is on its way. (Prototype: nothing is sent.)</p>';
      var btn = li.querySelector('[data-book-session]');
      btn.disabled = true; btn.textContent = 'Booked';
    });
  }

  function initReferral() {
    var f = $('#referral');
    if (!f) return;
    var steps = $all('[data-ref-step]', f), at = 0;
    function go(n) {
      at = n;
      steps.forEach(function (s, i) { s.hidden = i !== n; });
      $all('#ref-progress li').forEach(function (li, i) { li.classList.toggle('on', i <= n); });
      var h = steps[n].querySelector('h3'); if (h) { h.setAttribute('tabindex', '-1'); h.focus(); }
    }
    f.addEventListener('click', function (e) {
      if (e.target.matches('[data-ref-next]')) { if (validate(steps[at])) go(at + 1); }
      if (e.target.matches('[data-ref-back]')) go(at - 1);
    });
    $('#ref-files').addEventListener('change', function (e) {
      var names = Array.prototype.map.call(e.target.files, function (x) { return x.name; });
      $('#ref-file-list').textContent = names.length ? names.join(', ') : 'No files chosen';
    });
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!validate(steps[at])) return;
      f.hidden = true;
      $('#ref-done').hidden = false;
      $('#ref-done').focus();
    });
    go(0);
  }

  function initGuide() {
    var f = $('#guide');
    if (!f) return;
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!validate(f)) return;
      f.innerHTML = '<p role="status"><b>Thanks.</b> The guide is on its way, with the next information session dates. (Prototype: nothing is sent.)</p>';
    });
  }

  /* --- 4 Proof ------------------------------------------------------- */
  var RATES = {
    transfer: { label: 'Births per embryo transferred', rows: [['Under 35', 38, 41], ['35 to 37', 31, 34], ['38 to 39', 24, 27], ['40 to 42', 14, 16], ['43 and over', 5, 6]] },
    collection: { label: 'Births per egg collection (all transfers from it)', rows: [['Under 35', 49, 47], ['35 to 37', 38, 39], ['38 to 39', 27, 28], ['40 to 42', 15, 16], ['43 and over', 5, 5]] }
  };
  function initRates() {
    var host = $('#rates');
    if (!host) return;
    function render(k) {
      var d = RATES[k];
      $('#rates-label').textContent = d.label;
      host.innerHTML = d.rows.map(function (r) {
        return '<div class="cv-bar-row"><span>' + r[0] + '</span><div class="cv-bar-track" role="img" aria-label="' + r[0] + ': clinic ' + r[1] + '%, national ' + r[2] + '% (sample)"><div class="cv-bar-fill" style="width:' + r[1] + '%">' + r[1] + '%</div><span class="cv-bar-nat" style="left:' + r[2] + '%"></span></div></div>';
      }).join('');
      $('#rates-table').innerHTML = '<thead><tr><th>Age</th><th>Cambridge IVF</th><th>National</th></tr></thead><tbody>' + d.rows.map(function (r) { return '<tr><th>' + r[0] + '</th><td>' + r[1] + '%</td><td>' + r[2] + '%</td></tr>'; }).join('') + '</tbody>';
    }
    $all('[data-rate]').forEach(function (b) {
      b.addEventListener('click', function () {
        $all('[data-rate]').forEach(function (o) { o.setAttribute('aria-pressed', o === b ? 'true' : 'false'); });
        render(b.getAttribute('data-rate'));
      });
    });
    render('transfer');
  }

  function initFilterGroup(attr, itemAttr) {
    var btns = $all('[' + attr + ']');
    if (!btns.length) return;
    btns.forEach(function (b) {
      b.addEventListener('click', function () {
        var v = b.getAttribute(attr);
        btns.forEach(function (o) { o.setAttribute('aria-pressed', o === b ? 'true' : 'false'); });
        $all('[' + itemAttr + ']').forEach(function (el) { el.hidden = v !== 'all' && el.getAttribute(itemAttr).split(' ').indexOf(v) === -1; });
      });
    });
  }

  function initPeople() {
    var modal = $('#person-modal');
    if (!modal) return;
    $all('[data-person]').forEach(function (b) {
      b.addEventListener('click', function () {
        $('#pm-name').textContent = b.getAttribute('data-name');
        $('#pm-role').textContent = b.getAttribute('data-role-label');
        $('#pm-bio').textContent = b.getAttribute('data-bio');
        modal.hidden = false;
        modal._return = b;
        $('#pm-close').focus();
      });
    });
    function close() { modal.hidden = true; if (modal._return) modal._return.focus(); }
    $('#pm-close').addEventListener('click', close);
    modal.addEventListener('click', function (e) { if (e.target === modal) close(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !modal.hidden) close(); });
  }

  /* --- 5 Self-pay services ------------------------------------------- */
  function initStorageCalc() {
    var f = $('#ef-calc');
    if (!f) return;
    function upd() {
      var pkg = +$('#ef-pkg').value, yrs = +$('#ef-years').value;
      var storage = Math.max(0, yrs - 1) * 346;
      $('#ef-years-out').textContent = yrs + (yrs === 1 ? ' year' : ' years');
      $('#ef-total').textContent = money(pkg + storage);
      $('#ef-break').innerHTML = '<li><span>Freezing package (includes first year of storage)</span><b>' + money(pkg) + '</b></li><li><span>Storage, years 2 to ' + yrs + '</span><b>' + (yrs > 1 ? money(storage) : '£0') + '</b></li><li class="sub"><span>Later, to use your eggs (not in this total): thaw, embryo creation and transfer</span><b>£3,675</b></li>';
    }
    f.addEventListener('input', upd);
    upd();
  }

  var WAITS = { cambridge: 26, ipswich: 34, peterborough: 32 };
  function addWorkingDays(n) {
    var d = new Date(); d.setHours(12, 0, 0, 0);
    while (n > 0) { d.setDate(d.getDate() + 1); if (d.getDay() !== 0 && d.getDay() !== 6) n--; }
    return d;
  }
  function initSemen() {
    var f = $('#sa-book');
    if (!f) return;
    var loc = $('#sa-loc'), test = $('#sa-test');
    function upd() {
      var w = WAITS[loc.value];
      var dna = test.value === 'dna';
      if (dna && loc.value === 'peterborough') { $('#sa-dna-warn').hidden = false; } else { $('#sa-dna-warn').hidden = true; }
      var days = dna ? 4 : w;
      var first = addWorkingDays(days);
      $('#sa-wait').textContent = days + ' working days';
      $('#sa-first').textContent = longDate(first);
      $('#sa-price').textContent = dna ? '£462' : '£189';
      var host = $('#sa-dates'), ds = [];
      var d = new Date(first);
      while (ds.length < 6) { if (d.getDay() !== 0 && d.getDay() !== 6) ds.push(new Date(d)); d.setDate(d.getDate() + 1); }
      host.innerHTML = ds.map(function (x, i) { return '<button type="button" class="cv-day" data-i="' + i + '" data-d="' + longDate(x) + '" aria-pressed="false">' + DAY[x.getDay()] + '<b>' + x.getDate() + '</b>' + MON[x.getMonth()] + '</button>'; }).join('');
      $('#sa-pay').hidden = true;
    }
    loc.addEventListener('change', upd);
    test.addEventListener('change', upd);
    $('#sa-dates').addEventListener('click', function (e) {
      var b = e.target.closest('.cv-day'); if (!b) return;
      $all('.cv-day', $('#sa-dates')).forEach(function (o) { o.setAttribute('aria-pressed', o === b ? 'true' : 'false'); });
      $('#sa-when').textContent = b.getAttribute('data-d') + ', ' + loc.options[loc.selectedIndex].text;
      $('#sa-pay').hidden = false;
    });
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!validate(f)) return;
      f.hidden = true;
      $('#sa-done-when').textContent = $('#sa-when').textContent;
      $('#sa-done').hidden = false;
      $('#sa-done').focus();
    });
    upd();
  }

  function initDonor() {
    var f = $('#donor');
    if (!f) return;
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var age = +$('#dn-age').value;
      var smoke = $('input[name=dn-smoke]:checked', f), fam = $('input[name=dn-fam]:checked', f);
      var err = $('#dn-err');
      if (!age || !smoke || !fam) { err.hidden = false; err.focus(); return; }
      err.hidden = true;
      var ok = age >= 18 && age <= 45 && smoke.value === 'no' && fam.value === 'no';
      var out = $('#dn-result');
      out.hidden = false;
      $('#dn-text').innerHTML = ok
        ? '<b>You look like a good fit.</b> Leave your details and our donor team will call you within five working days to explain the next steps and the tests involved.'
        : '<b>Thank you for wanting to help.</b> Based on your answers we can\'t take you forward as a donor right now. ' + (age > 45 ? 'Donors need to be 18 to 45. ' : '') + (smoke.value === 'yes' ? 'Donors need to have been non-smokers for at least three months, so you could try again then. ' : '') + (fam.value === 'yes' ? 'A family history of genetic conditions usually rules out donation. ' : '');
      $('#dn-contact').hidden = !ok;
      out.focus();
    });
    $('#dn-contact').addEventListener('submit', function (e) {
      e.preventDefault();
      if (!validate(e.target)) return;
      e.target.innerHTML = '<p role="status"><b>Thanks.</b> The donor team will be in touch. (Prototype: nothing is sent.)</p>';
    });
  }

  function initStoragePay() {
    var f = $('#pay-form');
    if (!f) return;
    $('#pay-ref').addEventListener('input', function () {
      var ok = /^CIVF-?\d{5}$/i.test(this.value.trim());
      $('#pay-found').hidden = !ok;
    });
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!validate(f)) return;
      if ($('#pay-found').hidden) { $('#pay-ref-err').hidden = false; $('#pay-ref').focus(); return; }
      f.hidden = true;
      $('#pay-done').hidden = false;
      $('#pay-done').focus();
    });
  }

  /* --- Quick-win demos ------------------------------------------------ */
  function initQuickWins() {
    // Generic toggles inside demos: [data-qw-toggle] shows/hides #id
    $all('[data-qw-toggle]').forEach(function (b) {
      b.addEventListener('click', function () {
        var t = document.getElementById(b.getAttribute('data-qw-toggle'));
        var open = t.hidden;
        t.hidden = !open;
        b.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
    });
    var copy = $('[data-copy]');
    if (copy) copy.addEventListener('click', function () {
      var src = document.getElementById(copy.getAttribute('data-copy'));
      try { navigator.clipboard.writeText(src.textContent).then(function () { toast('Copied'); }, function () { toast('Copy blocked: select the text instead'); }); } catch (e) { toast('Copy blocked: select the text instead'); }
    });
  }

  /* Before / after switch on quick-win pages */
  function initBeforeAfter() {
    var stored = null;
    try { stored = window.sessionStorage.getItem('civf-ba'); } catch (e) { /* private mode */ }
    $all('[data-ba]').forEach(function (box) {
      var buttons = $all('[data-ba-show]', box);
      function show(which, rem) {
        $all('.ba-before', box).forEach(function (p) { p.hidden = which !== 'before'; });
        $all('.ba-after', box).forEach(function (p) { p.hidden = which !== 'after'; });
        buttons.forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-ba-show') === which ? 'true' : 'false'); });
        if (rem) { try { window.sessionStorage.setItem('civf-ba', which); } catch (e) { /* private mode */ } }
      }
      buttons.forEach(function (b) { b.addEventListener('click', function () { show(b.getAttribute('data-ba-show'), true); }); });
      show(stored === 'after' ? 'after' : 'before', false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.target.closest && e.target.closest('input, select, textarea')) return;
      if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
      var b = $('[data-ba-show="' + (e.key === 'ArrowLeft' ? 'before' : 'after') + '"]');
      if (b) b.click();
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    if ($('.cv-actionbar')) document.body.classList.add('has-actionbar');
    initEstimator();
    initCompare();
    initEvidence();
    initPath();
    initEligibility();
    initNhsCheck();
    initJourney();
    initEnquiry();
    initCallBooking();
    initSessions();
    initReferral();
    initGuide();
    initRates();
    initFilterGroup('data-role-filter', 'data-role');
    initFilterGroup('data-story-filter', 'data-story');
    initPeople();
    initStorageCalc();
    initSemen();
    initDonor();
    initStoragePay();
    initQuickWins();
    initBeforeAfter();
    $all('[data-tab-jump]').forEach(function (b) {
      b.addEventListener('click', function () { var t = $('[data-tab="' + b.getAttribute('data-tab-jump') + '"]'); if (t) { t.click(); t.focus(); } });
    });
  });
})();
