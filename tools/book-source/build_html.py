# -*- coding: utf-8 -*-
"""把 book/zh + book/en 組成一頁雙語閱讀網頁（放在 site/books/<slug>/index.html）。

語言切換
  預設英文；首次造訪時偵測瀏覽器語言（zh* → 中文），之後記在 localStorage。
  沒有 JavaScript 時 CSS 預設顯示英文。
  對齊靠結構標記一對一（部、章、節、圖、表、註腳定義），
  節內的普通段落數兩種語言可以不同。

v10 起的變化
  插圖不再內嵌 base64，而是寫成 site/assets/img/book/{zh,en,shared}/ 的檔案：
  自繪圖是 SVG（中文版用套件附的輪廓化 SVG，英文版由 make_figs_v2.py 產生），
  三張歷史地圖是 JPG，網頁顯示縮圖、點開看原尺寸。
  註腳：正文 [^id] → 上標數字，卷末依首次出現順序列出，可往返。
  目錄軌：部／章／可展開的小節。

設計
  色    墨 #1B242C／紙 #F6F7F8／石板藍 #2F4858／磚紅 #A8503C
  字    中文思源宋體 TC；西文 Source Serif 4；工具性文字 Inter／思源黑體 TC
"""
import sys, io, os, re, shutil, base64
try:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
except AttributeError:
    pass
from PIL import Image
from book_config import READER_URL

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(os.path.dirname(HERE))
BOOK_SOURCE = os.environ.get("BOOK_SOURCE", HERE)
OUT = os.environ.get("BOOK_OUTPUT", os.path.join(SITE, READER_URL.strip("/"), "index.html"))
IMGDIR = os.path.join(SITE, "assets", "img", "book")
IMGURL = "/assets/img/book"
os.makedirs(os.path.dirname(OUT), exist_ok=True)

LANGS = ("en", "zh")            # 第一個是預設語言
WEB_JPG_W = 1600                # 歷史地圖的網頁顯示寬度；原尺寸另存 *.full.jpg

MARKERS = ("#PART", "#H1", "#H2", "#EPI", "#FIG2", "#FIG", "#TAB", "#ENDTAB", "#BOX",
           "#ENDBOX", "#Q", "#RG", "#REF", "#FN", "#TITLEPAGE", "#ENDTITLEPAGE",
           "#HALFTITLE", "#ENDHALFTITLE", "#TOC")


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


# ── 行內標記：[^id] 註腳、[文字](網址)、**粗體**、*斜體* ─────────────
FN_STATE = {lg: {"order": [], "count": {}} for lg in LANGS}


def fn_ref(lang, key):
    st = FN_STATE[lang]
    if key not in st["order"]:
        st["order"].append(key)
    st["count"][key] = st["count"].get(key, 0) + 1
    n = st["order"].index(key) + 1
    k = st["count"][key]
    label = ("註 %d" if lang == "zh" else "Note %d") % n
    return ('<sup class="fnref" id="fnref-%s-%s-%d"><a href="#fn-%s-%s" role="doc-noteref" '
            'aria-label="%s">%d</a></sup>' % (lang, key, k, lang, key, label, n))


def inline(t, lang="en", refs=True):
    tokens = []

    def tok(html):
        tokens.append(html)
        return "\x00%d\x00" % (len(tokens) - 1)

    t = re.sub(r"\[([^\]\n]+?)\]\((https?://[^)\s]+)\)",
               lambda m: tok('<a href="%s" rel="noopener">%s</a>' % (esc(m.group(2)), inline(m.group(1), lang, False))), t)
    if refs:
        t = re.sub(r"\[\^([A-Za-z0-9_-]+)\]", lambda m: tok(fn_ref(lang, m.group(1))), t)
    t = esc(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"<em>\1</em>", t)
    t = re.sub("\x00(\\d+)\x00", lambda m: tokens[int(m.group(1))], t)
    return t


def plain(t):
    """alt 文字用：拿掉行內標記。"""
    t = re.sub(r"\[\^[A-Za-z0-9_-]+\]", "", t)
    t = re.sub(r"\[([^\]]+?)\]\(https?://[^)\s]+\)", r"\1", t)
    return t.replace("**", "").replace("*", "").strip()


# ── 插圖：SVG 直接複製，JPG 縮圖＋原尺寸，PNG 量化 ──────────────────
_img_cache = {}


def find_src(lang, name):
    # Published assets retain the original SVGs and full-resolution historical images.
    for sub in (lang, "shared"):
        asset = os.path.join(IMGDIR, sub, name)
        if name.lower().endswith((".jpg", ".jpeg")):
            original = os.path.splitext(asset)[0] + ".full.jpg"
            if os.path.isfile(original):
                return original, sub
        if os.path.isfile(asset):
            return asset, sub
    for d in (os.path.join(HERE, "figs", lang), os.path.join(HERE, "figs", "shared")):
        p = os.path.join(d, name)
        if os.path.exists(p):
            return p, ("shared" if d.endswith("shared") else lang)
    raise SystemExit("[FAIL] 找不到插圖 %s（%s）" % (name, lang))


def svg_size(path):
    head = io.open(path, encoding="utf-8").read(4000)
    m = re.search(r'viewBox="([\d.\s-]+)"', head)
    if m:
        v = m.group(1).split()
        return round(float(v[2])), round(float(v[3]))
    w = re.search(r'width="([\d.]+)', head)
    h = re.search(r'height="([\d.]+)', head)
    return round(float(w.group(1))), round(float(h.group(1)))


def web_image(lang, name):
    """回傳 (url, w, h, full_url)。full_url 只有 JPG 才有。"""
    key = (lang, name)
    if key in _img_cache:
        return _img_cache[key]
    src, sub = find_src(lang, name)
    outdir = os.path.join(IMGDIR, sub)
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, name)
    stem, ext = os.path.splitext(name)
    ext = ext.lower()
    if ext == ".svg":
        if not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(src):
            shutil.copyfile(src, out)
        w, h = svg_size(src)
        res = ("%s/%s/%s" % (IMGURL, sub, name), w, h, None)
    elif ext in (".jpg", ".jpeg"):
        full = os.path.join(outdir, stem + ".full.jpg")
        if not os.path.exists(full) or os.path.getmtime(full) < os.path.getmtime(src):
            shutil.copyfile(src, full)
        im = Image.open(src).convert("RGB")
        if im.width > WEB_JPG_W:
            im = im.resize((WEB_JPG_W, round(im.height * WEB_JPG_W / im.width)), Image.LANCZOS)
        if not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(src):
            im.save(out, "JPEG", quality=84, optimize=True, progressive=True)
        res = ("%s/%s/%s" % (IMGURL, sub, name), im.width, im.height,
               "%s/%s/%s.full.jpg" % (IMGURL, sub, stem))
    else:
        im = Image.open(src).convert("RGB")
        if im.width > 1400:
            im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
        if not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(src):
            im.quantize(colors=64, method=Image.MEDIANCUT, dither=Image.NONE).save(out, "PNG", optimize=True)
        res = ("%s/%s/%s" % (IMGURL, sub, name), im.width, im.height, None)
    _img_cache[key] = res
    return res


# ── 來源解析 ─────────────────────────────────────────────
def parse(lang):
    d = os.path.join(BOOK_SOURCE, lang)
    lines = []
    for f in sorted(os.listdir(d)):
        if f.endswith(".txt"):
            lines += io.open(os.path.join(d, f), encoding="utf-8").read().split("\n")
            lines.append("")
    blocks, i, n = [], 0, len(lines)
    while i < n:
        s = lines[i].strip()
        i += 1
        if not s:
            continue
        if s in ("#TITLEPAGE", "#HALFTITLE"):
            end = "#ENDTITLEPAGE" if s == "#TITLEPAGE" else "#ENDHALFTITLE"
            buf = []
            while lines[i].strip() != end:
                if lines[i].strip():
                    buf.append(lines[i].strip())
                i += 1
            i += 1
            blocks.append(("titlepage" if s == "#TITLEPAGE" else "halftitle", buf))
        elif s == "#TOC":
            blocks.append(("toc", None))
        elif s.startswith("#PART "):
            v = s[6:].split("|")
            while len(v) < 3:
                v.append("")
            blocks.append(("part", v))
        elif s.startswith("#H1 "):
            blocks.append(("h1", s[4:]))
        elif s.startswith("#H2 "):
            blocks.append(("h2", s[4:]))
        elif s.startswith("#EPI "):
            blocks.append(("epi", s[5:]))
        elif s.startswith("#FIG2 "):
            v = s[6:].split("|")
            assert len(v) == 7, s[:60]
            blocks.append(("fig2", v))
        elif s.startswith("#FIG "):
            v = s[5:].split("|")
            if len(v) == 2:
                v.append("")
            blocks.append(("fig", v))
        elif s == "#TAB" or s.startswith("#TAB "):
            cap, rows = s[5:].strip(), []
            while lines[i].strip() != "#ENDTAB":
                if lines[i].strip():
                    rows.append(lines[i].strip().split("|"))
                i += 1
            i += 1
            blocks.append(("tab", (cap, rows)))
        elif s.startswith("#BOX "):
            title, paras = s[5:], []
            while lines[i].strip() != "#ENDBOX":
                if lines[i].strip():
                    paras.append(lines[i].strip())
                i += 1
            i += 1
            blocks.append(("box", (title, paras)))
        elif s.startswith("#Q "):
            blocks.append(("q", s[3:]))
        elif s.startswith("#RG "):
            blocks.append(("rg", s[4:]))
        elif s.startswith("#REF "):
            blocks.append(("ref", s[5:]))
        elif s.startswith("#FN "):
            key, _, text = s[4:].partition("|")
            blocks.append(("fn", (key.strip(), text.strip())))
        elif s.startswith("#"):
            print("[WARN] 未知指令：", s[:40])
        else:
            blocks.append(("p", s))
    return blocks


def split_caption(cap):
    m = re.match(r"^((?:圖|Figure|表|Table)\s*[\d]+(?:\.\d+)?)(?:　|  )(.*)$", cap)
    if m:
        return m.group(1), m.group(2)
    return "", cap


def img_tag(lang, fn, alt, cls=""):
    url, w, h, full = web_image(lang, fn)
    img = ('<img src="%s" width="%d" height="%d" alt="%s" loading="lazy" decoding="async">'
           % (url, w, h, esc(plain(alt))))
    zoom = ("放大檢視" if lang == "zh" else "Open full size")
    return '<a class="zoom%s" href="%s" aria-label="%s">%s</a>' % (
        (" " + cls) if cls else "", full or url, zoom, img)


def render(kind, val, lang, sid=None):
    L = ' data-lang="' + lang + '"'
    if kind == "h1":
        return '<h2 class="chap-h"' + L + ">" + esc(val) + "</h2>"
    if kind == "h2":
        return '<h3 id="%s"%s>%s</h3>' % (sid, L, esc(val)) if sid else "<h3" + L + ">" + esc(val) + "</h3>"
    if kind == "epi":
        return '<p class="epi"' + L + ">" + inline(val, lang) + "</p>"
    if kind == "q":
        return "<blockquote" + L + ">" + inline(val, lang) + "</blockquote>"
    if kind == "rg":
        return '<h4 class="rg"' + L + ">" + esc(val) + "</h4>"
    if kind == "ref":
        return '<p class="ref"' + L + ">" + inline(val, lang) + "</p>"
    if kind == "fig":
        fn, cap, alt = val
        num, rest = split_caption(cap)
        alt = alt or plain(rest)
        return ('<figure class="fig"' + L + '><div class="fig-ground">' + img_tag(lang, fn, alt) +
                '</div><figcaption><span class="num">' + esc(num) + "</span>" +
                inline(rest, lang) + "</figcaption></figure>")
    if kind == "fig2":
        f1, a1, h1, f2, a2, h2, cap = val
        num, rest = split_caption(cap)
        return ('<figure class="fig fig-pair"' + L + '><div class="pair">'
                '<figure><div class="fig-ground">' + img_tag(lang, f1, a1) + '</div><figcaption class="sub">' + esc(h1) + "</figcaption></figure>"
                '<figure><div class="fig-ground">' + img_tag(lang, f2, a2) + '</div><figcaption class="sub">' + esc(h2) + "</figcaption></figure>"
                '</div><figcaption><span class="num">' + esc(num) + "</span>" + inline(rest, lang) + "</figcaption></figure>")
    if kind == "tab":
        cap, rows = val
        th = "".join("<th scope=\"col\">" + inline(c, lang) + "</th>" for c in rows[0])
        tb = "".join("<tr>" + "".join("<td>" + inline(c, lang) + "</td>" for c in r) + "</tr>" for r in rows[1:])
        capt = ("<figcaption>" + inline(cap, lang) + "</figcaption>") if cap else ""
        return ('<figure class="tbl"' + L + ">" + capt +
                '<div class="scroll"><table><thead><tr>' + th + "</tr></thead><tbody>" + tb + "</tbody></table></div></figure>")
    if kind == "box":
        title, paras = val
        ps = "".join("<p>" + inline(p, lang) + "</p>" for p in paras)
        return '<aside class="box"' + L + "><h4>" + inline(title, lang) + "</h4>" + ps + "</aside>"
    if kind == "part":
        label, title, intro = val
        intro_html = ('<p class="part-intro">' + inline(intro, lang) + "</p>") if intro else ""
        return ('<section class="part"' + L + '><p class="part-label">' + esc(label) + "</p><h2>" + esc(title) + "</h2>" + intro_html + "</section>")
    return ""


def footnote_list(lang, defs):
    st = FN_STATE[lang]
    missing = [k for k in st["order"] if k not in defs]
    unused = [k for k in defs if k not in st["order"]]
    if missing or unused:
        raise SystemExit("[FAIL] %s 註腳不對應：缺定義 %r／未引用 %r" % (lang, missing, unused))
    back_label = "返回正文" if lang == "zh" else "Back to text"
    items = []
    for k in st["order"]:
        backs = " ".join('<a class="fnback" href="#fnref-%s-%s-%d" role="doc-backlink" aria-label="%s %d">↩%s</a>'
                         % (lang, k, i, back_label, i, ("<sup>%d</sup>" % i) if st["count"][k] > 1 else "")
                         for i in range(1, st["count"][k] + 1))
        items.append('<li id="fn-%s-%s">%s %s</li>' % (lang, k, inline(defs[k], lang, False), backs))
    return '<ol class="footnotes" data-lang="%s">%s</ol>' % (lang, "".join(items))


def build():
    src = {lg: parse(lg) for lg in LANGS}
    body, nav, titles = [], [], {}
    ptr = {lg: 0 for lg in LANGS}
    sec_n = part_n = sub_n = 0
    open_sec = False
    fn_defs = {lg: {} for lg in LANGS}
    cur_chap = None   # nav 中目前章的 dict

    def kind_at(lg):
        return src[lg][ptr[lg]][0] if ptr[lg] < len(src[lg]) else None

    while any(ptr[lg] < len(src[lg]) for lg in LANGS):
        flow = {}
        for lg in LANGS:
            got = []
            while kind_at(lg) == "p":
                got.append(src[lg][ptr[lg]][1])
                ptr[lg] += 1
            flow[lg] = got
        if any(flow.values()):
            for lg in LANGS:
                ps = "".join("<p>" + inline(t, lg) + "</p>" for t in flow[lg])
                body.append('<div class="flow" data-lang="' + lg + '">' + ps + "</div>")

        kinds = {lg: kind_at(lg) for lg in LANGS}
        present = set(k for k in kinds.values() if k)
        if not present:
            break
        if len(present) > 1:
            pos = {lg: (src[lg][ptr[lg]][1] if ptr[lg] < len(src[lg]) else None) for lg in LANGS}
            raise SystemExit("[FAIL] 結構錯位：%r\n%r" % (kinds, pos))
        kind = present.pop()

        if kind == "titlepage":
            for lg in LANGS:
                t, s2, s3 = src[lg][ptr[lg]][1][:3]
                titles[lg] = t
                body.append('<header class="cover" data-lang="' + lg + '"><h1>' + esc(t) +
                            '</h1><p class="sub">' + esc(s2) + '</p><p class="author">' + esc(s3) + "</p></header>")
                ptr[lg] += 1
            continue
        if kind == "halftitle":
            for lg in LANGS:
                epi = src[lg][ptr[lg]][1][1]
                q = ("「" + esc(epi) + "」") if lg == "zh" else ("&ldquo;" + esc(epi) + "&rdquo;")
                body.append('<p class="cover-quote" data-lang="' + lg + '">' + q + "</p>")
                ptr[lg] += 1
            continue
        if kind == "toc":
            for lg in LANGS:
                ptr[lg] += 1
            continue
        if kind == "part":
            part_n += 1
            pid = "part" + str(part_n)
            if open_sec:
                body.append("</section>")
                open_sec = False
            body.append('<div class="part-wrap" id="' + pid + '">')
            labels = {}
            for lg in LANGS:
                v = src[lg][ptr[lg]][1]
                body.append(render("part", v, lg))
                labels[lg] = (v[0] + "　" + v[1]) if lg == "zh" else (v[0] + " — " + v[1])
                ptr[lg] += 1
            body.append("</div>")
            nav.append({"kind": "part", "id": pid, "labels": labels})
            cur_chap = None
            continue
        if kind == "h1":
            sec_n += 1
            sub_n = 0
            sid = "s" + str(sec_n)
            if open_sec:
                body.append("</section>")
            body.append('<section class="chap" id="' + sid + '">')
            open_sec = True
            labels = {}
            for lg in LANGS:
                v = src[lg][ptr[lg]][1]
                body.append(render("h1", v, lg, sid))
                labels[lg] = v
                ptr[lg] += 1
            cur_chap = {"kind": "chap", "id": sid, "labels": labels, "secs": []}
            nav.append(cur_chap)
            continue
        if kind == "h2":
            sub_n += 1
            # 中英兩邊都會產生一個標題元素，id 必須分開：共用同一個 id 時
            # getElementById 只找得到排在前面的英文那個，切到中文時它是隱藏的，
            # 目錄裡的小節連結就會點了不動。
            labels, sids = {}, {}
            for lg in LANGS:
                v = src[lg][ptr[lg]][1]
                sids[lg] = "s%d-%d-%s" % (sec_n, sub_n, lg)
                body.append(render("h2", v, lg, sids[lg]))
                labels[lg] = v
                ptr[lg] += 1
            if cur_chap is not None:
                cur_chap["secs"].append((sids, labels))
            continue
        if kind == "fn":
            for lg in LANGS:
                k, text = src[lg][ptr[lg]][1]
                fn_defs[lg][k] = text
                ptr[lg] += 1
            continue

        for lg in LANGS:
            body.append(render(kind, src[lg][ptr[lg]][1], lg))
            ptr[lg] += 1

    if any(fn_defs.values()):
        for lg in LANGS:
            body.append(footnote_list(lg, fn_defs[lg]))
    if open_sec:
        body.append("</section>")

    # 目錄軌
    navparts = []
    for item in nav:
        if item["kind"] == "part":
            # 語言的顯示與否掛在外層 div。掛在 a 上的話，.rail a.nav-part 的
            # display:block 比 [data-book-lang] 的隱藏規則更專一，兩種語言會同時出現。
            for lg in LANGS:
                navparts.append('<div data-lang="%s"><a class="nav-part" href="#%s">%s</a></div>'
                                % (lg, item["id"], esc(item["labels"][lg])))
            continue
        for lg in LANGS:
            secs = "".join('<a href="#%s">%s</a>' % (sids[lg], esc(lab[lg])) for sids, lab in item["secs"])
            tog = ""
            if secs:
                tog = ('<button type="button" class="nav-tog" aria-expanded="false" aria-controls="secs-%s-%s" aria-label="%s"></button>'
                       % (lg, item["id"], "展開小節" if lg == "zh" else "Show sections"))
            navparts.append('<div data-lang="%s"><div class="nav-chap"><a class="nav-link" href="#%s">%s</a>%s</div>%s</div>'
                            % (lg, item["id"], esc(item["labels"][lg]), tog,
                               ('<div class="nav-secs" id="secs-%s-%s" hidden>%s</div>' % (lg, item["id"], secs)) if secs else ""))
    navhtml = "".join(navparts)

    html = (TEMPLATE
            .replace("@@NAV@@", navhtml)
            .replace("@@BODY@@", "".join(body))
            .replace("@@TITLE_EN@@", esc(titles.get("en", "")))
            .replace("@@TITLE_ZH@@", esc(titles.get("zh", "")))
            .replace("@@READER_URL@@", READER_URL))
    io.open(OUT, "w", encoding="utf-8", newline="\n").write(html)
    kb = os.path.getsize(OUT) / 1024
    print("[OK] %s  %.0f KB　目錄項 %d　插圖 %d　註腳 zh %d／en %d"
          % (OUT, kb, len(nav), len(_img_cache), len(FN_STATE["zh"]["order"]), len(FN_STATE["en"]["order"])))


TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>No View Is the Whole</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="canonical" href="https://somanlin2650.github.io@@READER_URL@@">
<meta name="description" content="No View Is the Whole: a second-order philosophy of understanding, action, and revision. Complete Chinese and English editions.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@400;600;700&family=Noto+Sans+TC:wght@400;500&family=Source+Serif+4:ital,wght@0,400;0,600;1,400&family=Inter:wght@400;500&display=swap">
<style>
:root {
  --ink:#1B242C; --ink-soft:#40505C; --mute:#667a86;
  --paper:#F6F7F8; --hair:#DBE1E5; --hair-soft:#E9EDF0;
  --slate:#2F4858; --slate-lo:#EDF1F4;
  --brick:#A8503C; --fig-bg:#FFFFFF; --fig-edge:#E4E9ED; --rail-bg:#F1F3F5;
  --serif:"Source Serif 4","Noto Serif TC",Georgia,"新細明體",serif;
  --sans:"Inter","Noto Sans TC","Segoe UI","微軟正黑體",system-ui,sans-serif;
  --measure:37rem;
  /* 不宣告的話，捲軸會依瀏覽器主題自己決定明暗，在淺色頁面上出現一條深色粗捲軸 */
  color-scheme:light;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --ink:#E3E8EB; --ink-soft:#B9C4CB; --mute:#8B9AA5;
    --paper:#14191D; --hair:#2E383F; --hair-soft:#232B31;
    --slate:#9CBACB; --slate-lo:#1E262C;
    --brick:#D08B70; --fig-bg:#F7F8F9; --fig-edge:#2E383F; --rail-bg:#171D22;
    color-scheme:dark;
  }
}
:root[data-theme="dark"] {
  --ink:#E3E8EB; --ink-soft:#B9C4CB; --mute:#8B9AA5;
  --paper:#14191D; --hair:#2E383F; --hair-soft:#232B31;
  --slate:#9CBACB; --slate-lo:#1E262C;
  --brick:#D08B70; --fig-bg:#F7F8F9; --fig-edge:#2E383F; --rail-bg:#171D22;
  color-scheme:dark;
}

/* 語言切換：沒有 JavaScript 時預設顯示英文 */
[data-lang] { display:none; }
[data-lang="en"] { display:block; }
[data-book-lang="zh"] [data-lang="en"] { display:none; }
[data-book-lang="zh"] [data-lang="zh"] { display:block; }
[data-book-lang="en"] [data-lang="en"] { display:block; }
[data-book-lang="en"] [data-lang="zh"] { display:none; }
sup.fnref { display:inline; }

* { box-sizing:border-box; }
/* 點目錄時捲過去，跟站內版一致；標題停在距頂 1.5rem 的位置。 */
html { scroll-behavior:smooth; scroll-padding-top:1.5rem; }
body {
  margin:0; background:var(--paper); color:var(--ink);
  font-family:var(--serif); font-size:17px; line-height:1.95;
  letter-spacing:.015em; -webkit-font-smoothing:antialiased;
  -webkit-text-size-adjust:100%; text-size-adjust:100%;
}
:root[data-book-lang="en"] body { letter-spacing:0; line-height:1.75; }

#bar { position:fixed; inset:0 auto auto 0; height:2px; width:0;
       background:var(--brick); z-index:60; transition:width .1s linear; }

.shell { display:grid; grid-template-columns:18.5rem minmax(0,1fr); }
.rail {
  position:sticky; top:0; height:100vh; overflow-y:auto; background:var(--rail-bg);
  border-right:1px solid var(--hair); padding:1.6rem 1rem 3rem 1.4rem;
  font-family:var(--sans); font-size:.8rem; line-height:1.55;
  /* 目錄軌自己會捲。預設捲軸有 16px 寬，正好卡在目錄與內文中間，很礙眼；
     改成細捲軸，滑鼠移進來才顯出滑塊。scrollbar-gutter 讓寬度保持一致，
     捲軸出現時不會把目錄文字推一下。 */
  scrollbar-width:thin; scrollbar-color:transparent transparent;
  scrollbar-gutter:stable;
}
.rail:hover, .rail:focus-within { scrollbar-color:var(--hair) transparent; }
.rail::-webkit-scrollbar { width:6px; }
.rail::-webkit-scrollbar-track { background:transparent; }
.rail::-webkit-scrollbar-thumb { background:transparent; border-radius:3px; }
.rail:hover::-webkit-scrollbar-thumb, .rail:focus-within::-webkit-scrollbar-thumb {
  background:var(--hair);
}
.langsw { display:flex; gap:.4rem; margin-bottom:1.4rem; }
.langsw button {
  flex:1; font-family:var(--sans); font-size:.76rem; cursor:pointer;
  padding:.42rem .3rem; border-radius:3px; border:1px solid var(--hair);
  background:transparent; color:var(--ink-soft);
}
.langsw button:hover { color:var(--ink); }
.langsw button[aria-pressed="true"] {
  background:var(--slate); border-color:var(--slate);
  color:var(--paper); font-weight:500;
}
.langsw button:focus-visible, .nav-tog:focus-visible { outline:2px solid var(--brick); outline-offset:2px; }
.rail-head {
  font-family:var(--sans); font-size:.68rem; letter-spacing:.16em;
  text-transform:uppercase; color:var(--mute);
  padding-bottom:.9rem; margin-bottom:1rem; border-bottom:1px solid var(--hair);
}
.rail-head span { display:inline; }
[data-book-lang="zh"] .rail-head span[data-lang="en"] { display:none; }
[data-book-lang="en"] .rail-head span[data-lang="zh"] { display:none; }
.rail nav { display:flex; flex-direction:column; }
.rail a { color:var(--ink-soft); text-decoration:none; border-radius:2px; }
.rail a:hover { color:var(--ink); }
.rail a:focus-visible { outline:2px solid var(--brick); outline-offset:2px; }
.rail a.nav-part { margin-top:1.5rem; margin-bottom:.3rem; font-weight:500; color:var(--slate);
                   font-size:.84rem; padding:.2rem 0; display:block; }
.nav-chap { display:flex; align-items:flex-start; gap:.3rem; }
.nav-chap .nav-link { flex:1; display:block; padding:.34rem 0 .34rem .95rem; position:relative; }
.nav-chap .nav-link::before { content:""; position:absolute; left:0; top:1.05em;
                  width:4px; height:4px; border-radius:50%; background:var(--hair); }
.nav-chap.here .nav-link { color:var(--brick); font-weight:500; }
.nav-chap.here .nav-link::before { background:var(--brick); }
.nav-tog { flex:0 0 auto; width:1.5rem; height:1.5rem; margin-top:.3rem; border:0; background:transparent;
           cursor:pointer; color:var(--mute); border-radius:3px; position:relative; }
.nav-tog::before { content:""; position:absolute; left:50%; top:50%; width:.4rem; height:.4rem;
                   border-right:1.5px solid currentColor; border-bottom:1.5px solid currentColor;
                   transform:translate(-50%,-65%) rotate(45deg); transition:transform .18s ease; }
.nav-tog[aria-expanded="true"]::before { transform:translate(-50%,-35%) rotate(225deg); }
.nav-tog:hover { color:var(--ink); background:var(--hair-soft); }
.nav-secs { padding:.1rem 0 .5rem 1.15rem; border-left:1px solid var(--hair); margin:0 0 .3rem .1rem; }
.nav-secs a { display:block; font-size:.74rem; line-height:1.5; padding:.22rem 0 .22rem .6rem; color:var(--mute); }
.nav-secs a:hover { color:var(--ink); }
.nav-secs a.here { color:var(--brick); font-weight:500; box-shadow:-1px 0 0 0 var(--brick); }

main { padding:0 2rem 8rem; min-width:0; }
.cover { max-width:var(--measure); margin:0 auto; padding:7rem 0 4.5rem; }
.cover h1 {
  font-family:"Noto Serif TC",var(--serif);
  font-size:clamp(2.4rem,6.5vw,3.5rem); font-weight:700; line-height:1.25;
  letter-spacing:.02em; margin:0 0 1.4rem; text-wrap:balance;
}
.cover[data-lang="en"] h1 { text-transform:uppercase; letter-spacing:.05em; }
.cover .sub { font-size:1.08rem; color:var(--slate); margin:0 0 .5rem; line-height:1.75; }
.cover .author { font-size:.98rem; color:var(--mute); margin:2.2rem 0 0; letter-spacing:.05em; }
.part-wrap { max-width:var(--measure); margin:6.5rem auto 4rem;
             border-top:1px solid var(--hair); border-bottom:1px solid var(--hair); }
.part { padding:3rem 0; text-align:center; }
.part-label { font-family:var(--sans); font-size:.72rem; letter-spacing:.2em; color:var(--mute); margin:0 0 .9rem; }
.part h2 { font-family:"Noto Serif TC",var(--serif); font-size:clamp(1.7rem,4.5vw,2.15rem); font-weight:700;
           color:var(--slate); margin:0; letter-spacing:.04em; }
.part-intro { font-size:.95rem; color:var(--mute); text-align:justify; margin:1.5rem auto 0; max-width:30rem; line-height:1.9; }

.chap { max-width:var(--measure); margin:0 auto; padding-top:5.5rem; }
.chap-h {
  font-family:"Noto Serif TC",var(--serif);
  font-size:clamp(1.5rem,4vw,1.95rem); font-weight:700; color:var(--slate);
  line-height:1.4; letter-spacing:.02em; margin:0 0 1.2rem;
  padding-bottom:.9rem; border-bottom:2px solid var(--slate); text-wrap:balance;
}
main h3 {
  font-family:"Noto Sans TC",var(--sans); font-size:1.06rem; font-weight:500;
  color:var(--slate); letter-spacing:.03em; line-height:1.6;
  margin:3.1rem 0 1rem; text-wrap:balance; scroll-margin-top:1.5rem;
}
h4.rg { font-family:var(--sans); font-size:.95rem; font-weight:500; color:var(--slate); letter-spacing:.05em;
        margin:2.6rem 0 1rem; padding-bottom:.5rem; border-bottom:1px solid var(--hair-soft); }
.flow { max-width:var(--measure); margin-left:auto; margin-right:auto; }
p { margin:0 0 1.15em; text-align:justify; text-wrap:pretty; }
:root[data-book-lang="en"] p { text-align:left; }
em { font-style:italic; }
strong { font-weight:600; color:var(--slate); }
a { color:var(--slate); text-decoration-color:var(--hair); text-underline-offset:.15em; }
a:hover { text-decoration-color:var(--brick); }
sup.fnref { line-height:0; font-size:.7em; vertical-align:super; margin-left:.08em; }
sup.fnref a { text-decoration:none; color:var(--brick); font-family:var(--sans); padding:0 .12em; }
sup.fnref a:hover { text-decoration:underline; }
sup.fnref:target a, li:target { background:var(--slate-lo); border-radius:2px; }
.footnotes { max-width:var(--measure); margin:1.5rem auto 0; padding-left:1.6rem;
             font-size:.88rem; line-height:1.75; color:var(--ink-soft); }
.footnotes li { margin:0 0 .9em; padding-left:.2rem; scroll-margin-top:1.5rem; text-align:left; }
.footnotes li::marker { color:var(--brick); font-family:var(--sans); font-size:.85em; }
.footnotes .fnback { text-decoration:none; color:var(--brick); font-family:var(--sans); margin-left:.3em; }
.footnotes .fnback sup { font-size:.7em; }
.epi { margin:0 0 2.6em; padding:.1rem 0 .1rem 1.1rem; border-left:2px solid var(--brick);
       color:var(--ink-soft); font-size:1rem; line-height:1.85; }
blockquote { margin:2.2em 0; padding:0; text-align:center; font-family:"Noto Serif TC",var(--serif);
             font-size:1.14rem; font-weight:600; color:var(--slate); line-height:1.8; }
.ref { font-size:.9rem; line-height:1.8; color:var(--ink-soft); margin:0 0 .8em; padding-left:1.4rem; text-indent:-1.4rem; text-align:left; }
.box { margin:2.4em 0; padding:1.4rem 1.5rem .4rem; background:var(--slate-lo); border-left:3px solid var(--slate); border-radius:0 3px 3px 0; }
.box h4 { font-family:var(--sans); font-size:.95rem; font-weight:500; color:var(--slate); margin:0 0 .9rem; letter-spacing:.03em; }
.box p { font-size:.96rem; line-height:1.85; margin-bottom:1em; }
.fig { margin:2.8em calc(-1 * clamp(0rem,4vw,3.5rem)); }
.fig-ground { background:var(--fig-bg); border:1px solid var(--fig-edge); border-radius:3px; padding:.6rem .8rem; }
.fig img { display:block; width:100%; height:auto; }
.fig a.zoom { display:block; cursor:zoom-in; }
.fig figcaption, .tbl figcaption { font-family:var(--sans); font-size:.8rem; line-height:1.7; color:var(--mute); margin-top:.8rem; text-align:center; }
.fig figcaption sup.fnref a { color:var(--brick); }
.fig .num { color:var(--brick); font-weight:500; margin-right:.5em; }
.fig-pair .pair { display:grid; grid-template-columns:1fr 1fr; gap:1rem; }
.fig-pair .pair figure { margin:0; }
.fig-pair .pair figcaption.sub { margin-top:.5rem; color:var(--ink-soft); font-size:.78rem; }
.tbl { margin:2.4em 0; }
.tbl figcaption { text-align:left; margin:0 0 .6rem; color:var(--slate); font-weight:500; font-size:.85rem; }
.scroll { overflow-x:auto; }
table { width:100%; border-collapse:collapse; font-family:var(--sans); font-size:.84rem; line-height:1.65; font-variant-numeric:tabular-nums; }
th, td { text-align:left; padding:.62rem .8rem .62rem .55rem; vertical-align:top; }
thead th { color:var(--slate); font-weight:500; background:var(--slate-lo); border-top:2px solid var(--slate); border-bottom:1px solid var(--slate); }
tbody td { border-bottom:1px solid var(--hair-soft); }
tbody tr:last-child td { border-bottom:1px solid var(--slate); }
.colophon { max-width:var(--measure); margin:4rem auto 0; padding-top:1.4rem; border-top:1px solid var(--hair);
            font-family:var(--sans); font-size:.76rem; line-height:1.7; color:var(--mute); }
.library-link { margin:0 0 1rem; font-family:var(--sans); font-size:.85rem; }

/* 圖片放大檢視 */
dialog#viewer { border:1px solid var(--hair); background:var(--paper); color:var(--ink); width:min(96vw,1700px);
                max-height:94vh; padding:.8rem; border-radius:4px; }
dialog#viewer::backdrop { background:rgba(10,14,18,.78); }
.viewer-bar { display:flex; gap:.6rem; justify-content:flex-end; align-items:center; margin-bottom:.6rem; font-family:var(--sans); font-size:.8rem; }
.viewer-bar .viewer-cap { flex:1; color:var(--mute); text-align:left; line-height:1.5; }
.viewer-bar button { font-family:var(--sans); font-size:.78rem; padding:.35rem .8rem; border:1px solid var(--hair);
                     background:transparent; color:var(--slate); cursor:pointer; border-radius:3px; }
.viewer-bar button:hover { border-color:var(--slate); }
.viewer-scroll { overflow:auto; max-height:80vh; background:#fff; border-radius:3px; }
.viewer-scroll img { display:block; margin:0 auto; max-width:100%; height:auto; }
.viewer-scroll.zoomed img { max-width:none; width:auto; }

#scrim { display:none; position:fixed; inset:0; z-index:57; background:rgba(10,14,18,.45); touch-action:none;
         opacity:0; pointer-events:none; transition:opacity .22s ease; }
#toggle { display:none; position:fixed; z-index:55; left:1rem; bottom:1rem; font-family:var(--sans); font-size:.82rem;
  padding:.6rem 1rem; border-radius:999px; cursor:pointer; background:var(--slate); color:var(--paper); border:none;
  box-shadow:0 3px 14px rgba(0,0,0,.22); }
@media (max-width:900px) {
  body { font-size:16.5px; }
  .shell { grid-template-columns:minmax(0,1fr); }
  .rail { position:fixed; inset:0 auto 0 0; width:min(21rem,86vw); z-index:58;
          transform:translateX(-101%); transition:transform .26s ease; box-shadow:0 0 30px rgba(0,0,0,.2); }
  .rail.open { transform:none; }
  #scrim { display:block; }
  #scrim.show { opacity:1; pointer-events:auto; }
  #toggle { display:block; }
  main { padding:0 1.2rem 6rem; }
  .cover { padding-top:4rem; }
  .chap { padding-top:3.5rem; }
  .fig { margin-left:0; margin-right:0; }
  .fig-pair .pair { grid-template-columns:1fr; }
}
@media (prefers-reduced-motion: reduce) {
  * { transition:none !important; }
  html { scroll-behavior:auto; }
}
@media print { .rail, #toggle, #scrim, #bar, dialog { display:none !important; } .shell { display:block; } }
</style>

<script>
(function () {
  var L = "en";
  var q = /[?&]lang=(zh|en)\b/.exec(location.search);
  var saved = null;
  try {
    saved = localStorage.getItem("booklang");
  } catch (e) {}
  if (q) L = q[1];
  else if (saved === "zh" || saved === "en") L = saved;
  else if (/^zh/i.test(navigator.language || "")) L = "zh";
  var r = document.documentElement;
  r.setAttribute("data-book-lang", L);
  r.setAttribute("lang", L === "zh" ? "zh-TW" : "en");
}());
</script>
</head>
<body>
<div id="bar"></div>
<button id="toggle" aria-expanded="false" aria-controls="rail">目錄 / Contents</button>
<div id="scrim" aria-hidden="true"></div>

<div class="shell">
  <aside class="rail" id="rail">
    <p class="library-link"><a data-lang="zh" href="/books/">← 所有書籍</a><a data-lang="en" href="/en/books/">← All books</a></p>
    <div class="langsw" role="group" aria-label="Language">
      <button type="button" data-set="en">English</button>
      <button type="button" data-set="zh">中文</button>
    </div>
    <div class="rail-head"><span data-lang="en">Contents</span><span data-lang="zh">目錄</span></div>
    <nav>@@NAV@@</nav>
  </aside>
  <main>
@@BODY@@
  <footer class="colophon">
    <p data-lang="en">Figure 4.1, right: David Rumsey Map Collection, David Rumsey Map Center, Stanford Libraries, used under CC BY-NC-SA 3.0. Other historical images are in the public domain as marked by their sources; diagrams were drawn for this book. Click any figure to open it at full size.</p>
    <p data-lang="zh">圖 4.1 右圖依 David Rumsey Map Collection, David Rumsey Map Center, Stanford Libraries 所列 CC BY-NC-SA 3.0 使用；其他歷史圖檔依來源標示為公有領域，示意圖為本書自繪。點任一張圖可放大檢視。</p>
  </footer>
  </main>
</div>

<dialog id="viewer" aria-label="Image viewer">
  <div class="viewer-bar"><span class="viewer-cap"></span><button type="button" id="v-zoom">100%</button><button type="button" id="v-close">✕</button></div>
  <div class="viewer-scroll"><img id="v-img" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='1' height='1'/%3E" alt=""></div>
</dialog>

<script>
(function () {
  var root = document.documentElement;
  var rail = document.getElementById("rail");
  var btn  = document.getElementById("toggle");
  var bar  = document.getElementById("bar");
  var TITLES = { en: "@@TITLE_EN@@", zh: "@@TITLE_ZH@@" };

  var sw = [].slice.call(document.querySelectorAll(".langsw button"));
  function apply(L) {
    root.setAttribute("data-book-lang", L);
    root.setAttribute("lang", L === "zh" ? "zh-TW" : "en");
    if (TITLES[L]) document.title = TITLES[L];
    sw.forEach(function (b) {
      b.setAttribute("aria-pressed", b.getAttribute("data-set") === L ? "true" : "false");
    });
    try { localStorage.setItem("booklang", L); } catch (e) {}
    var url = new URL(location.href);
    url.searchParams.set("lang", L);
    url.hash = url.hash.replace(/-(zh|en)$/, "-" + L);
    history.replaceState(null, "", url.pathname + url.search + url.hash);
  }
  sw.forEach(function (b) {
    b.addEventListener("click", function () {
      var anchor = null, best = Infinity;
      [].forEach.call(document.querySelectorAll("section[id],.part-wrap[id],main h3[id]"),
        function (s) {
          if (!s.getClientRects().length) return;
          var t = Math.abs(s.getBoundingClientRect().top);
          if (t < best) { best = t; anchor = s; }
        });
      apply(b.getAttribute("data-set"));
      if (anchor) {
        var translated = anchor.id.replace(/-(zh|en)$/, "-" + b.getAttribute("data-set"));
        anchor = document.getElementById(translated) || anchor;
        var previous = root.style.scrollBehavior;
        root.style.scrollBehavior = "auto";   // 回到原處要立刻到位，不要再捲一次
        anchor.scrollIntoView();
        root.style.scrollBehavior = previous;
      }
      markSection();
    });
  });
  apply(root.getAttribute("data-book-lang") || "en");

  var scrim = document.getElementById("scrim");
  function setDrawer(open) {
    rail.classList.toggle("open", open);
    btn.setAttribute("aria-expanded", open ? "true" : "false");
    scrim.classList.toggle("show", open);
  }
  btn.addEventListener("click", function () { setDrawer(!rail.classList.contains("open")); });
  scrim.addEventListener("click", function () { setDrawer(false); });
  rail.addEventListener("click", function (e) {
    var t = e.target.closest ? e.target.closest("a, button.nav-tog") : null;
    if (t && t.classList.contains("nav-tog")) {
      var open = t.getAttribute("aria-expanded") === "true";
      t.setAttribute("aria-expanded", open ? "false" : "true");
      var secs = document.getElementById(t.getAttribute("aria-controls"));
      if (secs) secs.hidden = open;
      /* 自己按開的章，捲動時不要被自動收合關掉 */
      if (open) { delete t.dataset.manual; } else { t.dataset.manual = "1"; }
      return;
    }
    if (t && t.tagName === "A") {
      /* 平滑捲動可能要走上兩秒，捲到停下來以前都不要自動開合；
         scrollend 沒有支援時，靠三秒的上限收尾。 */
      settleUntil = Date.now() + 3000;
      window.addEventListener("scrollend", releaseSettle, { once: true });
      if (window.innerWidth <= 900) setDrawer(false);
    }
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && rail.classList.contains("open")) setDrawer(false);
  });
  window.addEventListener("resize", function () {
    if (window.innerWidth > 900 && rail.classList.contains("open")) setDrawer(false);
  });

  function progress() {
    var h = document.documentElement;
    var max = h.scrollHeight - h.clientHeight;
    bar.style.width = (max > 0 ? (h.scrollTop / max) * 100 : 0) + "%";
  }
  document.addEventListener("scroll", progress, { passive: true });
  progress();

  /* 目前章節：標記目錄，並自動展開該章的小節 */
  var chapRows = {};
  [].forEach.call(rail.querySelectorAll(".nav-chap"), function (row) {
    var id = row.querySelector(".nav-link").getAttribute("href").slice(1);
    (chapRows[id] = chapRows[id] || []).push(row);
  });
  var secLinks = {};
  [].forEach.call(rail.querySelectorAll(".nav-secs a"), function (a) {
    var id = a.getAttribute("href").slice(1);
    (secLinks[id] = secLinks[id] || []).push(a);
  });
  /* 點完目錄的那段平滑捲動裡，沿途的章不要跟著一路開開關關 */
  var settleUntil = 0;
  var releaseSettle = function () { settleUntil = 0; };

  function setOpen(row, open) {
    var t = row.querySelector(".nav-tog");
    if (!t) return;
    if (Date.now() < settleUntil) return;
    if (!open && t.dataset.manual) return;
    t.setAttribute("aria-expanded", open ? "true" : "false");
    var secs = document.getElementById(t.getAttribute("aria-controls"));
    if (secs) secs.hidden = !open;
  }
  var seen = [];

  function markChapters() {
    if (!seen.length) return;
    var top = seen.slice().sort(function (a, b) {
      return document.getElementById(a).offsetTop - document.getElementById(b).offsetTop;
    })[0];
    for (var k in chapRows) chapRows[k].forEach(function (row) {
      var here = k === top;
      row.classList.toggle("here", here);
      setOpen(row, here);
    });
  }

  releaseSettle = function () {
    settleUntil = 0;
    markChapters();
  };

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      var id = en.target.id, k = seen.indexOf(id);
      if (en.isIntersecting) { if (k < 0) seen.push(id); }
      else if (k >= 0) seen.splice(k, 1);
    });
    markChapters();
  }, { rootMargin: "-25% 0px -65% 0px" });
  [].forEach.call(document.querySelectorAll("section[id],.part-wrap[id]"), function (s) { io.observe(s); });

  /* 目前讀到哪一節，直接由捲動位置算出來。原本用 IntersectionObserver 的進出
     事件：平滑捲動或長距離跳轉時，標題可能在兩個影格之間就掠過觀察帶，事件不會
     發生，小節索引因此一直停在舊的位置，甚至從頭到尾沒有高亮過。
     隱藏那一種語言的標題量到的尺寸全是零，所以先比對語言再算。 */
  var secHeads = [].slice.call(document.querySelectorAll("main h3[id]"));
  var secQueued = false;

  function markSection() {
    secQueued = false;
    var lang = root.getAttribute("data-book-lang");
    var current = null;
    for (var i = 0; i < secHeads.length; i++) {
      var h = secHeads[i];
      if (h.getAttribute("data-lang") !== lang) continue;
      if (h.getBoundingClientRect().top > 140) break;
      current = h.id;
    }
    for (var k in secLinks) {
      secLinks[k].forEach(function (a) { a.classList.toggle("here", k === current); });
    }
  }

  function queueSection() {
    if (secQueued) return;
    secQueued = true;
    requestAnimationFrame(markSection);
  }

  document.addEventListener("scroll", queueSection, { passive: true });
  window.addEventListener("resize", queueSection);
  markSection();

  /* 圖片放大檢視 */
  var dlg = document.getElementById("viewer");
  if (dlg && typeof dlg.showModal === "function") {
    var vimg = document.getElementById("v-img"), vcap = dlg.querySelector(".viewer-cap");
    var vzoom = document.getElementById("v-zoom"), pane = dlg.querySelector(".viewer-scroll");
    document.addEventListener("click", function (e) {
      var a = e.target.closest ? e.target.closest("a.zoom") : null;
      if (!a || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      e.preventDefault();
      var src = a.querySelector("img");
      vimg.src = a.getAttribute("href");
      vimg.alt = src.alt;
      vcap.textContent = src.alt;
      pane.classList.remove("zoomed");
      vzoom.textContent = "100%";
      dlg.showModal();
    });
    document.getElementById("v-close").onclick = function () { dlg.close(); };
    vzoom.onclick = function () {
      pane.classList.toggle("zoomed");
      vzoom.textContent = pane.classList.contains("zoomed") ? (root.getAttribute("data-book-lang") === "zh" ? "適合畫面" : "Fit") : "100%";
    };
    dlg.addEventListener("click", function (e) { if (e.target === dlg) dlg.close(); });
  }
}());
</script>
</body>
</html>
"""

if __name__ == "__main__":
    build()
