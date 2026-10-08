"""Check the generated site's indexing metadata before deployment (stdlib only)."""
import json
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.tags = []
        self.json_blocks = []
        self.in_json = False
        self.scripts = []
        self.in_script = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self.in_json = True
            self.json_blocks.append("")
        elif tag == "script" and not attrs.get("src") and attrs.get("type", "text/javascript") in ("text/javascript", "module"):
            self.in_script = True
            self.scripts.append("")

    def handle_endtag(self, tag):
        if tag == "script":
            self.in_json = False
            self.in_script = False

    def handle_data(self, data):
        if self.in_json:
            self.json_blocks[-1] += data
        if self.in_script:
            self.scripts[-1] += data


root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
origin = "https://somanlin2650.github.io"
slugs = ["understanding-without-possessing-the-world", "from-reaction-to-heterogeneous-rationality", "when-ai-cannot-see-its-own-hypoxia", "a-morality-we-can-revise",
         "you-dont-have-to-rediscover-the-world", "no-view-is-the-whole"]
paths = ["/", "/en/", "/articles/", "/en/articles/", "/books/", "/en/books/"]
paths += [f"{prefix}/posts/{slug}/" for prefix in ("", "/en") for slug in slugs]
ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
sitemap = ElementTree.parse(root / "sitemap.xml")
locations = {node.text for node in sitemap.findall("s:url/s:loc", ns)}
assert f"Sitemap: {origin}/sitemap.xml" in (root / "robots.txt").read_text()
for path in paths:
    page = Page((root / path.lstrip("/") / "index.html").read_text(encoding="utf-8"))
    assert sum(tag == "h1" for tag, _ in page.tags) == 1, (path, "Expected one H1")
    descriptions = [a.get("content") for t, a in page.tags if t == "meta" and a.get("name") == "description"]
    assert len(descriptions) == 1 and descriptions[0], (path, "Missing description")
    canonicals = [a.get("href") for t, a in page.tags if t == "link" and a.get("rel") == "canonical"]
    assert canonicals == [origin + path], (path, "Incorrect canonical", canonicals)
    alternates = {a.get("hreflang"): a.get("href") for t, a in page.tags if t == "link" and a.get("rel") == "alternate" and a.get("hreflang")}
    assert {"zh-Hant", "en"} <= alternates.keys(), (path, "Missing language pair")
    partner = path[3:] if path.startswith("/en/") else "/en" + path
    assert alternates["zh-Hant"] == origin + (partner if path.startswith("/en/") else path)
    assert alternates["en"] == origin + (path if path.startswith("/en/") else partner)
    assert any(t == "a" and a.get("hreflang") for t, a in page.tags), (path, "No static translation link")
    assert origin + path in locations, (path, "Missing from sitemap")
    data = [json.loads(block) for block in page.json_blocks]
    assert data, (path, "No structured data")
    if "/posts/" in path:
        assert any(d.get("@type") == "BlogPosting" and d.get("author") for d in data), (path, "Missing article/author metadata")
    if path in ("/", "/en/"):
        assert alternates.get("x-default") == origin + "/"
        for script in page.scripts:
            subprocess.run(["node", "--check"], input=script, text=True, encoding="utf-8", check=True)
print(f"SEO checks passed for {len(paths)} core pages, sitemap, and robots.txt.")
