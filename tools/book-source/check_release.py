"""Check bilingual coverage, references, generated pages, and assets."""
from pathlib import Path
from collections import Counter
import re
from bs4 import BeautifulSoup

HERE = Path(__file__).resolve().parent
SITE = HERE.parents[1]
reader = (SITE/'books/no-view-is-the-whole/index.html').read_text(encoding='utf-8')
soup = BeautifulSoup(reader, 'html.parser')
assert '第七版完整潤飾稿' not in reader
assert '完整審閱稿' not in reader
assert '結構重整審閱版' not in reader
ids = [n['id'] for n in soup.select('[id]')]
assert len(ids) == len(set(ids)), 'Duplicate element IDs'
for a in soup.select('a[href^="#"]'):
    assert a['href'][1:] in ids, a['href']
for n in soup.select('[src],a.zoom[href]'):
    value = n.get('src') or n.get('href')
    if value.startswith('/assets/'):
        assert (SITE/value.lstrip('/')).is_file(), value

def ordinary(text):
    return [line for line in text.splitlines() if line.strip() and not line.startswith('#')]

def markers(text):
    return [line.split()[0] for line in text.splitlines() if line.startswith('#')]

def references(text):
    text = '\n'.join(line for line in text.splitlines() if not line.startswith('#FN '))
    return Counter(re.findall(r'\[\^([^\]]+)\]',text))

def normal(text):
    return re.sub(r'\s+','',text)

stats = {}
for lang in ('zh','en'):
    nodes = soup.select(f'[data-lang="{lang}"]')
    visible = normal(''.join(n.get_text() for n in nodes))
    source = '\n'.join(p.read_text(encoding='utf-8') for p in sorted((HERE/lang).glob('*.txt')))
    defs = re.findall(r'^#FN ([^|]+)\|',source,re.M)
    assert len(defs) == 82 and len(set(defs)) == 82
    assert len(re.findall(r'^#PART ', source, re.M)) == 5
    assert len(re.findall(r'^#H1 (?:第.+章|\d+ —)', source, re.M)) == 16
    assert set(references(source)) == set(defs)
    checked = 0
    for line in ordinary(source):
        if '|' in line or len(line) < 35:
            continue
        for segment in re.split(r'\[\^[^\]]+\]',line.replace('**','').replace('*','')):
            assert normal(segment) in visible, (lang,segment[:90])
        checked += 1
    assert len(soup.select(f'figure[data-lang="{lang}"] img')) == 17
    assert len(soup.select(f'figure.tbl[data-lang="{lang}"]')) == 5
    stats[lang] = {'checked_paragraphs':checked, 'notes':len(defs)}

for z in sorted((HERE/'zh').glob('*.txt')):
    a = z.read_text(encoding='utf-8')
    b = (HERE/'en'/z.name).read_text(encoding='utf-8')
    assert markers(a) == markers(b), ('structure',z.name)
    assert len(ordinary(a)) == len(ordinary(b)), ('paragraph coverage',z.name)
    assert references(a) == references(b), ('references',z.name)
    za = re.findall(r'^#(?:FIG|FIG2) ([^|\s]+)',a,re.M)
    eb = re.findall(r'^#(?:FIG|FIG2) ([^|\s]+)',b,re.M)
    assert za == eb, ('figures',z.name)

for lang,path in [('zh','_posts/2026-08-25-no-view-is-the-whole.md'),('en','en/posts/no-view-is-the-whole.md')]:
    post = (SITE/path).read_text(encoding='utf-8')
    assert len(re.findall(r'^### ',post,re.M)) == 16
    assert len(re.findall(r'^## ',post,re.M)) == 8
    assert len(re.findall(r'^\[\^[^\]]+\]:',post,re.M)) == 82
    for p in (HERE/lang).glob('*.txt'):
        for line in ordinary(p.read_text(encoding='utf-8')):
            if len(line)>40 and '|' not in line:
                assert line in post, (path,line[:90])
print('PASS: all 18 source files align; complete rendered prose; 5 parts, 16 chapters, 82 notes, 17 images and 5 tables per language; valid links and article headings.')
print(stats)
