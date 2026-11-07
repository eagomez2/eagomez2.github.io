"""One-time import of the project pages from the old WordPress site.

Usage: python3 tools/import_wordpress.py <content.json> <thumbs.txt> <dir with saved detail pages>
Writes src/content/projects/*.md and public/images/projects/<slug>/*.
"""
import json, re, sys, os, html, urllib.request, io
from datetime import datetime
from bs4 import BeautifulSoup, NavigableString, Tag
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
content = json.load(open(sys.argv[1]))
thumbs = {}
for line in open(sys.argv[2]):
    kind, page, img = line.split()
    thumbs[page] = img
pages_dir = sys.argv[3]

def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'site-migration'})
    return urllib.request.urlopen(req, timeout=60).read()

def save_image(url, dest_noext, max_w=1400):
    data = fetch(url)
    im = Image.open(io.BytesIO(data))
    has_alpha = im.mode in ('RGBA', 'LA', 'P')
    im = im.convert('RGBA' if has_alpha else 'RGB')
    if im.width > max_w:
        im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
    ext = '.png' if has_alpha else '.jpg'
    path = dest_noext + ext
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if has_alpha:
        im.save(path, optimize=True)
    else:
        im.save(path, quality=85, optimize=True, progressive=True)
    return path, im.size

SAFE_CLASSES = {'button', 'soundcloud', 'embed-credit', 'video'}
KEEP_ATTRS = {'a': ['href'], 'iframe': ['src', 'title', 'height', 'allow', 'loading', 'allowfullscreen'], 'img': ['src', 'alt', 'width', 'height'], 'ol': ['start']}

def clean(node):
    """Strip WordPress classes/styles; keep structure and text exactly."""
    for t in node.find_all(True):
        keep = KEEP_ATTRS.get(t.name, [])
        for a in list(t.attrs):
            if a == 'class' and set(t['class']) <= SAFE_CLASSES:
                continue
            if a not in keep:
                del t.attrs[a]
        if t.name == 'a' and t.get('href', '').startswith('http') and 'estebangomez.me' not in t['href']:
            t['target'] = '_blank'
            t['rel'] = 'noopener'
    return node

def video_embed(url):
    url = html.unescape(url)
    m = re.search(r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([\w-]+)', url)
    if m:
        return f'https://www.youtube-nocookie.com/embed/{m.group(1)}'
    m = re.search(r'vimeo\.com/(?:video/)?(\d+)', url)
    if m:
        return f'https://player.vimeo.com/video/{m.group(1)}?dnt=1'
    return None

FRACTIONS = {'av_one_full': '1', 'av_one_half': '1-2', 'av_one_third': '1-3', 'av_two_third': '2-3',
             'av_one_fourth': '1-4', 'av_three_fourth': '3-4', 'av_one_fifth': '1-5', 'av_three_fifth': '3-5'}

def convert(slug, page_html, title):
    soup = BeautifulSoup(page_html, 'html.parser')
    main = soup.find('main')
    wrapper = main.find(class_='entry-content-wrapper')
    rows, row = [], None
    img_n = 0
    for col in wrapper.find_all(class_='flex_column', recursive=False):
        classes = col.get('class', [])
        frac = next((FRACTIONS[c] for c in classes if c in FRACTIONS), '1')
        if row is None or 'first' in classes:
            row = []
            rows.append(row)
        parts = []
        for el in col.find_all(recursive=False):
            parts.extend(convert_el(el, slug, title, lambda: None))
        row.append((frac, parts))
    out = []
    for r in rows:
        cols = [(f, p) for f, p in r if p]
        if not cols:
            continue
        if len(cols) == 1 and cols[0][0] == '1':
            out.append('\n'.join(cols[0][1]))
        else:
            inner = ''.join(f'<div class="col col-{f}">\n' + '\n'.join(p) + '\n</div>\n' for f, p in cols)
            out.append(f'<div class="cols">\n{inner}</div>')
    return '\n\n'.join(out)

counter = {}
headings = {}
def convert_el(el, slug, title, _):
    global counter
    res = []
    cls = el.get('class', []) if isinstance(el, Tag) else []
    if 'av-special-heading' in cls:
        h = el.find(class_='av-special-heading-tag')
        text = h.get_text(' ', strip=True)
        level = int(h.name[1])
        if level <= 4 and slug not in headings:
            headings[slug] = text  # page title, rendered by the layout
            return []
        res.append(f'<h2>{html.escape(text, quote=False)}</h2>' if level <= 5 else f'<h3>{html.escape(text, quote=False)}</h3>')
    elif 'avia-image-container' in cls:
        img = el.find('img')
        src = img.get('src')
        if img.get('srcset'):
            cands = [c.strip().split(' ') for c in img['srcset'].split(',')]
            src = max(cands, key=lambda c: int(c[1].rstrip('w')))[0]
        counter[slug] = counter.get(slug, 0) + 1
        path, (w, h) = save_image(src, os.path.join(ROOT, 'public/images/projects', slug, f'image-{counter[slug]}'))
        rel = '/' + os.path.relpath(path, os.path.join(ROOT, 'public'))
        a = el.find('a')
        alt = img.get('alt') or ''
        tag = f'<img src="{rel}" alt="{html.escape(alt)}" width="{w}" height="{h}" loading="lazy">'
        if a and a.get('href') and not re.search(r'\.(jpe?g|png|webp|gif)$', a['href']):
            tag = f'<a href="{html.escape(a["href"])}" target="_blank" rel="noopener">{tag}</a>'
        res.append(f'<figure>{tag}</figure>')
    elif 'avia-video' in cls:
        res.append(video_html(el.get('data-original_url', ''), el))
    elif 'av_textblock_section' in cls:
        tb = el.find(class_='avia_textblock')
        # replace video blocks and buttons inside text
        for v in tb.find_all(class_='avia-video'):
            v.replace_with(BeautifulSoup(video_html(v.get('data-original_url', ''), v), 'html.parser'))
        for b in tb.find_all(class_='avia-button-wrap'):
            a = b.find('a')
            label = a.get_text(' ', strip=True)
            b.replace_with(BeautifulSoup(f'<p><a class="button" href="{html.escape(a["href"])}" target="_blank" rel="noopener">{html.escape(label, quote=False)}</a></p>', 'html.parser'))
        for f in tb.find_all('iframe'):
            if 'soundcloud.com' in f.get('src', ''):
                f.attrs = {'src': f['src'], 'title': 'SoundCloud player', 'height': f.get('height', '166'), 'loading': 'lazy', 'allow': 'autoplay', 'class': ['soundcloud']}
        # SoundCloud attribution line under the player: keep, but style via class
        for d in tb.find_all('div'):
            if d.get('style', '').startswith('font-size: 10px'):
                d.attrs = {'class': ['embed-credit']}
        clean(tb)
        body = tb.decode_contents().strip()
        body = re.sub(r'<p>\s*</p>', '', body)
        if body:
            res.append(body)
    elif 'avia-button-wrap' in cls:
        a = el.find('a')
        res.append(f'<p><a class="button" href="{html.escape(a["href"])}" target="_blank" rel="noopener">{html.escape(a.get_text(" ", strip=True), quote=False)}</a></p>')
    elif el.name in ('br',):
        pass
    else:
        txt = el.get_text(' ', strip=True) if isinstance(el, Tag) else str(el).strip()
        if txt:
            print('UNHANDLED', slug, cls, txt[:80], file=sys.stderr)
    return res

def video_html(url, el):
    src = video_embed(url)
    if not src:
        sc = el.find('script')
        f = el.find('iframe') or (BeautifulSoup(sc.string or '', 'html.parser').find('iframe') if sc else None)
        src = video_embed(f['src']) if f else None
    if not src:
        print('NO VIDEO', url, file=sys.stderr)
        return ''
    return f'<div class="video"><iframe src="{src}" title="Video player" loading="lazy" allow="fullscreen; picture-in-picture" allowfullscreen></iframe></div>'

def main():
    os.makedirs(os.path.join(ROOT, 'src/content/projects'), exist_ok=True)
    for cat in ('software', 'sound'):
        for i, x in enumerate(content[cat]):
            slug = x['href'].rstrip('/').split('/')[-1]
            y, mo, d = x['href'].rstrip('/').split('/')[-4:-1]
            page_html = open(os.path.join(pages_dir, slug + '.html'), encoding='utf-8').read()
            body = convert(slug, page_html, x['title'])
            cover_path, _ = save_image(thumbs[x['href']], os.path.join(ROOT, 'public/images/projects', slug, 'cover'), max_w=900)
            cover = '/' + os.path.relpath(cover_path, os.path.join(ROOT, 'public'))
            fm = {
                'title': x['title'], 'heading': headings.get(slug, x['title']), 'subtitle': x['subtitle'], 'category': cat,
                'date': f'{y}-{mo}-{d}', 'order': i + 1, 'cover': cover,
            }
            lines = ['---'] + [f'{k}: {json.dumps(v, ensure_ascii=False)}' for k, v in fm.items()] + ['---', '', body, '']
            open(os.path.join(ROOT, 'src/content/projects', slug + '.md'), 'w', encoding='utf-8').write('\n'.join(lines))
            print('ok', slug)

main()
