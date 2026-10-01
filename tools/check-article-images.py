"""Check article banners and in-text images in the generated site (stdlib only)."""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
HEROES = {
    "from-reaction-to-heterogeneous-rationality": "cognition-hero.webp",
    "you-dont-have-to-rediscover-the-world": "learning-hero.webp",
    "a-morality-we-can-revise": "morality-hero.webp",
    "when-ai-cannot-see-its-own-hypoxia": "agent-hero.webp",
    "no-view-is-the-whole": "book-hero.webp",
}
INLINE = {
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
        body = article[article.index("</header>"):]
        assert article_images(body) == INLINE[slug], (prefix, slug, article_images(body))

print("Article image checks passed: 2 lists and 10 article pages.")
