/* BMI helper for the package check: fills the BMI field from height and weight. */
(function () {
  'use strict';
  document.addEventListener('DOMContentLoaded', function () {
    var h = document.getElementById('bmi-h'), w = document.getElementById('bmi-w');
    if (!h || !w) return;
    function upd() {
      var hm = (+h.value) / 100, kg = +w.value;
      var out = document.getElementById('bmi-out');
      if (hm > 1 && kg > 20) {
        var b = Math.round((kg / (hm * hm)) * 10) / 10;
        out.textContent = b;
        document.getElementById('el-bmi').value = b;
      } else {
        out.textContent = '–';
      }
    }
    h.addEventListener('input', upd);
    w.addEventListener('input', upd);
  });
})();
