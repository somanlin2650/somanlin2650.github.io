# -*- coding: utf-8 -*-
"""把全書轉成 Jekyll post（中英各一篇），插圖寫成 site/assets/img/book/ 的檔案。

閱讀器（/books/<slug>/）自己帶 CSS 與字體、自己一套語言切換，不吃站內
深色模式，不進站內搜尋，也沒有留言。做成 post 之後，全書就跟站上其他文章一樣。

標題階層（post 本身的標題是 h1）：
    #PART              → h2   五個部
    #H1 在某一部裡面   → h3   十六章
    #H1 不在任何部裡   → h2   序、結語、思想座標與資料來源
    #H2                → h4   小節

三層都進主題的「文章摘要」。桌機版 tocbot 沒有設 collapseDepth，預設只展開目前
所在的那一支，所以八十幾個小節不會攤成一張長清單；手機的彈出目錄才全部展開。

標題 id 用 part1 / s4 / s4-1 這組固定編號（kramdown 的 {: #id }），中英兩篇一致。
語言切換因此可以把目前的錨點接到另一篇，停在同一個位置；若改回讓 kramdown 從
標題文字自動產生 id，中英就會變成兩組不同的 id，切換只能回到文章開頭。

註腳：正文 [^id] 與卷末 [^id]: 定義都直接交給 kramdown，站內主題有現成樣式。
雙圖（#FIG2）：用兩欄表格並排，跟套件預覽一致。

用法：python build_post.py
"""
import io, os, re, sys

from build_html import parse, split_caption, web_image, plain
from book_config import SLUG, READER_URL

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(os.path.dirname(HERE))
SKIP = "{: data-toc-skip='' }"
# 不要填未來時間：Jekyll 會跳過日期未到的文章。日期沿用首次發表，內容更新記在 last_modified_at。
DATE = "2026-08-25 16:00:00 +0800"
UPDATED = "2026-09-22 09:00:00 +0800"

DESC_ZH = ("理解、行動與修正的二階哲學。從登月降落、地圖與日常判斷，"
           "以保留、組合與回返，追查理解如何形成、接續與修正。全書十六章、十七張圖及八十二項來源註釋。")
DESC_EN = ("A second-order philosophy of understanding, action, and revision. "
           "Preservation, composition, and return: how understanding forms, connects, and revises itself. "
           "Sixteen chapters, seventeen images, and eighty-two source notes.")

META = {
    "zh": dict(
        path=os.path.join(SITE, "_posts", "2026-08-25-%s.md" % SLUG),
        front=[
            ('title', '"所見非全貌：理解、行動與修正的二階哲學"'),
            ('date', DATE),
            ('last_modified_at', UPDATED),
            ('lang', 'zh-TW'),
            ('alternate_url', '/en/posts/%s/' % SLUG),
            ('categories', '[書籍]'),
            ('tags', '[所見非全貌, 認知, 模型, 抽象洩漏, 科學哲學]'),
            ('description', '"%s"' % DESC_ZH),
            ('toc', 'true'),
        ],
        lead=f'本篇是全書的完整內容，與 [單頁雙語閱讀器]({READER_URL}?lang=zh) '
             '同一份文字。閱讀器可以在中英之間切換、點圖放大；這裡是站內版本，'
             '有側邊目錄、深色模式與留言。',
    ),
    "en": dict(
        path=os.path.join(SITE, "en", "posts", "%s.md" % SLUG),
        front=[
            ('layout', 'post'),
            ('title', '"No View Is the Whole: A Second-Order Philosophy of Understanding, Action, and Revision"'),
            ('date', DATE),
            ('last_modified_at', UPDATED),
            ('lang', 'en'),
            ('permalink', '/en/posts/%s/' % SLUG),
            ('alternate_url', '/posts/%s/' % SLUG),
            ('categories', '[Book]'),
            ('tags', '[No View Is the Whole, Cognition, Models, Leaky Abstractions, Philosophy of Science]'),
            ('description', '"%s"' % DESC_EN),
            ('toc', 'true'),
            ('comments', 'true'),
        ],
        lead='This is the complete text of the book, the same words as the '
             f'[single-page bilingual reader]({READER_URL}?lang=en). The reader '
             'switches between Chinese and English and opens every figure at full size; this is the site-native '
             'version, with a sidebar table of contents, dark mode, and comments.',
    ),
}


def md_img(lang, fn, alt):
    url, w, h, full = web_image(lang, fn)
    alt = plain(alt).replace("[", "(").replace("]", ")").replace('"', "'")
    img = '![%s](%s){: width="%d" height="%d" }' % (alt, url, w, h)
    if full:
        return "[%s](%s)" % (img, full)
    return img


def convert(blocks, lang):
    out, in_part = [], False
    fns = []
    part_n = sec_n = sub_n = 0

    def add(s=""):
        out.append(s)

    for kind, val in blocks:
        if kind in ("titlepage", "halftitle", "toc"):
            continue
        if kind == "part":
            label, title, intro = val
            in_part = True
            part_n += 1
            add("## %s　%s" % (label, title) if lang == "zh" else "## %s — %s" % (label, title))
            add("{: #part%d }" % part_n)
            add()
            if intro:
                add("> %s" % intro)
                add("{: .prompt-info }")
                add()
        elif kind == "h1":
            top = not in_part or re.match(r'^(結語|Afterword|思想座標|Coordinates|Intellectual Bearings)', val)
            sec_n += 1
            sub_n = 0
            add("%s %s" % ("##" if top else "###", val))
            add("{: #s%d }" % sec_n)
            add()
        elif kind == "h2":
            sub_n += 1
            add("#### %s" % val)
            add("{: #s%d-%d }" % (sec_n, sub_n))
            add()
        elif kind == "epi":
            add("> *%s*" % val.replace("*", ""))
            add()
        elif kind == "q":
            add("> %s" % val)
            add("{: .prompt-tip }")
            add()
        elif kind == "rg":
            add("#### %s" % val)
            add(SKIP)
            add()
        elif kind == "ref":
            add(val)
            add()
        elif kind == "fig":
            fn, cap, alt = val
            num, rest = split_caption(cap)
            add(md_img(lang, fn, alt or rest))
            add("_%s%s%s_" % (num, "　" if num else "", rest))
            add()
        elif kind == "fig2":
            f1, a1, h1, f2, a2, h2, cap = val
            num, rest = split_caption(cap)
            add("| %s | %s |" % (h1, h2))
            add("|---|---|")
            add("| %s | %s |" % (md_img(lang, f1, a1), md_img(lang, f2, a2)))
            add()
            add("_%s%s%s_" % (num, "　" if num else "", rest))
            add()
        elif kind == "tab":
            cap, rows = val
            add("| " + " | ".join(rows[0]) + " |")
            add("|" + "|".join(["---"] * len(rows[0])) + "|")
            for r in rows[1:]:
                add("| " + " | ".join(r) + " |")
            add()
            if cap:
                add("_%s_" % cap)
                add()
        elif kind == "box":
            title, paras = val
            add("> **%s**" % title)
            add(">")
            for i, p in enumerate(paras):
                add("> %s" % p)
                if i != len(paras) - 1:
                    add(">")
            add()
        elif kind == "fn":
            key, text = val
            fns.append("[^%s]: %s" % (key, text))
        elif kind == "p":
            add(val)
            add()
    if fns:
        for line in fns:          # 每條定義之間留空行，kramdown 才不會把相鄰定義黏在一起
            add(line)
            add()
    return "\n".join(out).rstrip() + "\n"


def check_footnotes(text, lang):
    refs = set(re.findall(r"\[\^([A-Za-z0-9_-]+)\](?!:)", text))
    defs = set(re.findall(r"^\[\^([A-Za-z0-9_-]+)\]:", text, re.M))
    if refs != defs:
        raise SystemExit("[FAIL] %s 註腳不對應：缺定義 %r／未引用 %r" % (lang, sorted(refs - defs), sorted(defs - refs)))
    return len(defs)


def build():
    for lang in ("zh", "en"):
        m = META[lang]
        body = convert(parse(lang), lang)
        fm = "---\n" + "".join("%s: %s\n" % kv for kv in m["front"]) + "---\n"
        text = fm + "\n" + m["lead"] + "\n\n" + body
        n_fn = check_footnotes(body, lang)
        os.makedirs(os.path.dirname(m["path"]), exist_ok=True)
        io.open(m["path"], "w", encoding="utf-8", newline="\n").write(text)
        h2 = len(re.findall(r'^## ', body, re.M))
        h3 = len(re.findall(r'^### ', body, re.M))
        h4 = len(re.findall(r'^#### ', body, re.M))
        print("[OK] %s  %.0f KB　h2 %d／h3 %d／h4 %d／註腳 %d"
              % (os.path.relpath(m["path"], SITE), len(text.encode()) / 1024, h2, h3, h4, n_fn))


if __name__ == "__main__":
    build()
