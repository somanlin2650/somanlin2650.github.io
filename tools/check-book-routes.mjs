// Regression checks for the book reader pages. Run: node tools/check-book-routes.mjs
import assert from 'node:assert/strict';
import { readFileSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import vm from 'node:vm';

const root = fileURLToPath(new URL('../', import.meta.url));
const read = name => readFileSync(path.join(root, name), 'utf8');
const target = '/books/no-view-is-the-whole/';
const reader = read(target.slice(1) + 'index.html');

// Explicit language must work even when storage is blocked.
const scripts = [...reader.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
for (const script of scripts) new vm.Script(script);
for (const lang of ['zh', 'en']) {
  const attributes = {};
  vm.runInNewContext(scripts[0], {
    location: { search: '?lang=' + lang },
    localStorage: { getItem() { throw new Error('Storage blocked'); } },
    navigator: { language: lang === 'zh' ? 'en-US' : 'zh-TW' },
    document: { documentElement: { setAttribute(k, v) { attributes[k] = v; } } }
  });
  assert.equal(attributes['data-book-lang'], lang);
}

const apply = scripts[1].match(/function apply\(L\) \{([\s\S]*?)\n  \}/)[0];
for (const lang of ['zh', 'en']) {
  let updated;
  vm.runInNewContext(apply + `\napply('${lang}');`, {
    root: { setAttribute() {} }, TITLES: {}, sw: [],
    document: {}, localStorage: { setItem() {} }, URL,
    location: { href: 'https://example.test' + target + '?lang=zh&source=bookmark#s11-4-zh' },
    history: { replaceState(_state, _title, url) { updated = url; } }
  });
  assert.equal(updated, target + '?lang=' + lang + '&source=bookmark#s11-4-' + lang);
}

assert.ok(reader.includes('rel="canonical" href="https://somanlin2650.github.io' + target + '"'));
assert.ok(reader.includes('href="/books/"'));
assert.ok(reader.includes('href="/en/books/"'));
for (const match of reader.matchAll(/(?:src|href)="(\/assets\/[^"?#]+)"/g)) {
  assert.ok(existsSync(path.join(root, match[1])), 'Missing asset: ' + match[1]);
}
for (const [name, permalink] of [['books.md', '/books/'], ['books-en.md', '/en/books/']]) {
  assert.ok(read('_tabs/' + name).includes('permalink: ' + permalink));
}
assert.ok(!existsSync(path.join(root, 'book')), 'The retired /book/read/ entry is back.');
for (const name of ['_includes/home-content.html', '_posts/2026-08-25-no-view-is-the-whole.md', 'en/posts/no-view-is-the-whole.md']) {
  assert.ok(!read(name).includes('/book/read/'), 'Old reader link: ' + name);
}
assert.ok(read('_data/books.yml').includes('slug: no-view-is-the-whole'));
console.log('PASS: language selection and URL updates, canonical URL, images, and entry links.');
