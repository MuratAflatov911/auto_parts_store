console.log('Automir loaded');
(function () {
  const make = document.getElementById('makeSelect');
  const model = document.getElementById('modelSelect');
  const generation = document.getElementById('generationSelect');
  if (!make || !model || !generation) return;

  make.addEventListener('change', function () {
    const url = new URL(window.location.href);
    if (this.value) url.searchParams.set('make', this.value); else url.searchParams.delete('make');
    url.searchParams.delete('model');
    url.searchParams.delete('generation');
    window.location.href = url.toString();
  });

  model.addEventListener('change', function () {
    const url = new URL(window.location.href);
    if (this.value) url.searchParams.set('model', this.value); else url.searchParams.delete('model');
    url.searchParams.delete('generation');
    window.location.href = url.toString();
  });

  generation.addEventListener('change', function () {
    const url = new URL(window.location.href);
    if (this.value) url.searchParams.set('generation', this.value); else url.searchParams.delete('generation');
    window.location.href = url.toString();
  });
})();
