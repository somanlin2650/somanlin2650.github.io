"""Check article banners and in-text images in the generated site (stdlib only)."""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
HEROES = {
    "understanding-without-possessing-the-world": "aei-v2-hero.webp",
    "from-reaction-to-heterogeneous-rationality": "cognition-hero.webp",
    "you-dont-have-to-rediscover-the-world": "learning-hero.webp",
    "a-morality-we-can-revise": "morality-hero.webp",
    "when-ai-cannot-see-its-own-hypoxia": "agent-hero.webp",
    "no-view-is-the-whole": "book-hero.webp",
}
INLINE = {
    "understanding-without-possessing-the-world": ['aei-v5-embedded-inquirers.webp', 'aei-v2-query-partitions.webp', 'aei-rule110.webp', 'aei-v4-release-status.webp', 'aei-v4-evidence-tasks.webp'],
    "from-reaction-to-heterogeneous-rationality": ["cognition-flytrap.webp"],
    "a-morality-we-can-revise": ["morality-litter-context.webp"],
    "when-ai-cannot-see-its-own-hypoxia": ["agent-independent-observer.webp"],
    "no-view-is-the-whole": ["book-apollo-lander.webp", "book-apollo-control.webp"],
    "you-dont-have-to-rediscover-the-world": [],
}


class Doc(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.events = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.events.append((tag, dict(attrs)))


def article_images(text):
    # Chirpy wraps content images in a popup link, so each path appears twice.
    return list(dict.fromkeys(re.findall(r'/assets/img/articles/([\w-]+\.webp)', text)))


for prefix, cjk in (("", True), ("/en", False)):
    listing = (root / prefix.lstrip("/") / "articles" / "index.html").read_text(encoding="utf-8")
    cards = re.findall(r'<article>(.*?)</article>', listing, re.S)
    assert len(cards) == len(HEROES), (prefix, "article cards", len(cards))
    for card in cards:
        slug = re.search(r'href="[^"]*/posts/([^/"]+)/"', card).group(1)
        first = Doc(card).events[0]
        assert first[0] == "div" and "article-hero" in first[1].get("class", ""), (prefix, slug, "banner is not first")
        imgs = article_images(card)
        assert imgs == [HEROES[slug]], (prefix, slug, imgs)
        alt = re.search(r'<img[^>]*alt="([^"]+)"', card).group(1)
        assert bool(re.search(r"[一-鿿]", alt)) == cjk, (prefix, slug, "alt language")

    for slug, hero in HEROES.items():
        page = (root / prefix.lstrip("/") / "posts" / slug / "index.html").read_text(encoding="utf-8")
        assert page.count('class="post-hero"') == 1, (prefix, slug, "banner count")
        assert "preview-img" not in page, (prefix, slug, "theme preview image also rendered")
        article = page[page.index("<article"):]
        events = Doc(article).events
        assert events[1][0] == "figure" and events[1][1].get("class") == "post-hero", (prefix, slug, events[1])
        assert events[2][0] == "img" and events[2][1]["src"].endswith("/" + hero), (prefix, slug, events[2])
        h1 = next(i for i, (t, _) in enumerate(events) if t == "h1")
        assert h1 > 2, (prefix, slug, "banner after h1")
        alt = events[2][1]["alt"]
        assert alt and bool(re.search(r"[一-鿿]", alt)) == cjk, (prefix, slug, "alt language")
        body = article[article.index("</header>"):article.index("</article>")]
        assert article_images(body) == INLINE[slug], (prefix, slug, article_images(body))

# Every other place that links articles in the content area shows the banner too.
for prefix, cjk in (("", True), ("/en", False)):
    home = (root / prefix.lstrip("/") / "index.html").read_text(encoding="utf-8")
    topics = re.search(r'<ul class="home-topics">(.*?)</ul>', home, re.S).group(1)
    for li in re.findall(r"<li>(.*?)</li>", topics, re.S):
        slug = re.search(r'/posts/([^/"]+)/', li).group(1)
        assert article_images(li) == [HEROES[slug]], (prefix, "home topic", slug)
    essays = re.search(r'<div class="home-essays">(.*?)</div>\s*<p>', home, re.S).group(1)
    for card in re.findall(r"<article>(.*?)</article>", essays, re.S):
        slug = re.search(r'<h3><a href="[^"]*/posts/([^/"]+)/"', card).group(1)
        assert article_images(card) == [HEROES[slug]], (prefix, "home essay", slug)
    book = re.search(r'<section class="home-book".*?</section>', home, re.S).group(0)
    assert article_images(book) == [HEROES["no-view-is-the-whole"]], (prefix, "home book")
    books = (root / prefix.lstrip("/") / "books" / "index.html").read_text(encoding="utf-8")
    assert article_images(books) == [HEROES["no-view-is-the-whole"]], (prefix, "books list")
    for slug in HEROES:
        page = (root / prefix.lstrip("/") / "posts" / slug / "index.html").read_text(encoding="utf-8")
        related = re.search(r'<aside id="related-posts".*?</aside>', page, re.S)
        if related:
            for card in re.findall(r'<a href="[^"]*/posts/([^/"]+)/" class="post-preview[^>]*>(.*?)</a>', related.group(0), re.S):
                assert article_images(card[1]) == [HEROES[card[0]]], (prefix, slug, "related", card[0])

print(f"Article image checks passed: lists, home, books, related posts, and {2 * len(HEROES)} article pages.")
