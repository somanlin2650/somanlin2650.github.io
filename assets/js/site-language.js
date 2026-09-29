/* Shared by the Jekyll site and the standalone book reader. */
(function (root) {
  'use strict';
  var KEY = 'site_language_preference';
  function normalize(value) {
    var match = /^(zh|en)(?:-|$)/i.exec(value || '');
    return match ? match[1].toLowerCase() : null;
  }
  function read(store) {
    try { return normalize(root[store].getItem(KEY)); } catch (_) { return null; }
  }
  function remember(lang) {
    lang = normalize(lang);
    if (!lang) return;
    ['localStorage', 'sessionStorage'].forEach(function (store) {
      try { root[store].setItem(KEY, lang); } catch (_) {}
    });
  }
  function resolve() {
    var explicit = normalize(new URL(root.location.href).searchParams.get('lang'));
    if (explicit) { remember(explicit); return explicit; }
    var saved = read('localStorage') || read('sessionStorage');
    if (saved) return saved;
    var languages = root.navigator.languages || [root.navigator.language];
    for (var i = 0; i < languages.length; i++) {
      var lang = normalize(languages[i]);
      if (lang) return lang;
    }
    return 'en';
  }
  root.SiteLanguage = { resolve: resolve, remember: remember };
}(window));
