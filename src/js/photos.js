/* ==========================================================================
   photos.js — Cambridge IVF's own photography, hotlinked from media.cuh.nhs.uk.
   Only runs when the design layer (theme.css) is present. Each image is
   applied only after it has loaded, so a failed image leaves the illustrated
   brand placeholder in place. Photography © Cambridge IVF / CUH.
   ========================================================================== */
(function () {
  'use strict';
  var BASE = 'https://media.cuh.nhs.uk/images/';
  var P = {
    family: 'CIVF_Website_1.2e16d0ba.fill-764x510.png',
    team: 'CIVF_Staff-62_700x393.2e16d0ba.fill-600x400.png',
    patients: 'Website_pictures_1.2e16d0ba.fill-768x420.png',
    couple: 'couple_with_baby.2e16d0ba.fill-768x420.jpg',
    shared: 'Shared_Motherhood.2e16d0ba.fill-768x420.png',
    eggs: 'Website_pictures_17.2e16d0ba.fill-768x420.png',
    lab: 'CIVF_Lab_60_675x450.width-840.png',
    store: 'CIVF_Lab_182_675x426_lYUnxe3.width-840.png',
    building: 'Website_pictures_11.width-840.png',
    hand: 'hand-holding-newborn-babys-hand_pT.2e16d0ba.fill-768x420.png',
    semen: 'Semen_analysis.2e16d0ba.fill-768x420.png',
    andrology: 'andrology-service-3.2e16d0ba.fill-768x420.png',
    scan: '3D_scan_2.2e16d0ba.fill-768x420.png',
    embryo: 'embryo.2e16d0ba.fill-768x420.png',
    chris: 'Dr_Chris_White_1.2e16d0ba.fill-580x450.png'
  };
  // Page hero photo by file name
  var HERO = { costs: 'family', 'find-your-path': 'shared', 'your-journey': 'hand', start: 'patients', proof: 'team', 'egg-freezing': 'eggs', 'self-pay': 'andrology' };
  // Landing page thumbnails in order
  var THUMBS = ['family', 'shared', 'patients', 'team', 'eggs'];

  function load(key, cb) {
    var img = new Image();
    img.onload = function () { cb(img.src); };
    img.src = BASE + P[key];
  }
  function onPlaceholder(el, key) {
    load(key, function (src) {
      el.style.backgroundImage = 'url("' + src + '")';
      el.classList.add('has-photo');
      el.setAttribute('role', 'img');
      if (!el.getAttribute('aria-label')) el.setAttribute('aria-label', 'Photograph');
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    var on = window.getComputedStyle(document.documentElement).getPropertyValue('--civf-theme').trim();
    if (!on) return;
    var file = (window.location.pathname.split('/').pop() || 'index.html').replace('.html', '');

    var head = document.querySelector('.page-head');
    if (head && HERO[file]) {
      load(HERO[file], function (src) {
        var c = head.querySelector('.container');
        var wrap = document.createElement('div');
        while (c.firstChild) wrap.appendChild(c.firstChild);
        c.appendChild(wrap);
        var img = document.createElement('img');
        img.className = 'cv-hero-photo';
        img.alt = '';
        img.src = src;
        c.appendChild(img);
        head.classList.add('has-photo');
      });
    }

    document.querySelectorAll('.proto-thumb .wf-placeholder').forEach(function (el, i) { if (THUMBS[i]) onPlaceholder(el, THUMBS[i]); });
    document.querySelectorAll('[data-photo]').forEach(function (el) { onPlaceholder(el, el.getAttribute('data-photo')); });
  });
})();
