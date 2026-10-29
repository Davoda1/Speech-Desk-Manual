(function () {
  let preference = 'system';
  try { preference = localStorage.getItem('speechdesk-manual-theme') || 'system'; } catch (_) {}
  if (!['light', 'dark', 'system'].includes(preference)) preference = 'system';
  const dark = preference === 'dark' || (preference === 'system' && window.matchMedia('(prefers-color-scheme: dark)').matches);
  document.documentElement.dataset.theme = dark ? 'dark' : 'light';
  document.documentElement.dataset.preference = preference;
})();
