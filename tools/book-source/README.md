# Book source

`zh/` and `en/` contain the complete, corresponding manuscripts for *No View Is the Whole*. Edit these sources before rebuilding the reader and the site-native articles. Keep structural markers, figure filenames, table dimensions, and footnote identifiers aligned between languages; prose need not follow the same sentence structure.

From the repository root, with Python 3 and Pillow installed:

```sh
python tools/book-source/build_html.py
python tools/book-source/build_post.py
python tools/book-source/check_release.py
node tools/check-book-routes.mjs
```

The release checker also uses Beautiful Soup (`beautifulsoup4`). Existing original SVGs and full-resolution historical images are read from `assets/img/book/`; no duplicate image archive is needed. The builders write the reader under `books/no-view-is-the-whole/` and both full-text articles. `BOOK_SOURCE` and `BOOK_OUTPUT` can override the reader's input and output paths for previews.

When titles or chapter headings change, update `_data/books.yml` and `_includes/home-content.html` as well. Publication timestamps and article descriptions are in `build_post.py`.

This directory is excluded from Jekyll output by the existing `tools` exclusion. Commit generated pages together with source changes. Pushes to the default branch trigger the existing GitHub Pages build and deployment workflow.
