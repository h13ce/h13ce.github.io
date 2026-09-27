"""Validate research references and the rendered Jekyll site. Requires PyYAML."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import collections
import yaml

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_site'
works = yaml.safe_load((ROOT / '_data/works.yml').read_text())
papers = yaml.safe_load((ROOT / '_data/publications.yml').read_text())
paper_ids = [p['id'] for p in papers]
assert len(paper_ids) == len(set(paper_ids)), 'Duplicate publication IDs'
assert 4 <= sum(bool(p.get('selected')) for p in papers) <= 6
assert len({w['title'] for w in works.values()}) == len(works), 'Duplicate work records'
themes = {}
for path in (ROOT / '_research').glob('*.md'):
    data = yaml.safe_load(path.read_text().split('---', 2)[1])
    themes[path.stem] = data
    assert len(data['selected_works']) == len(set(data['selected_works']))
    for work_id in data['selected_works']:
        assert work_id in works, (path, work_id)
        assert path.stem in works[work_id]['themes'], (path, work_id, 'theme')
for work_id, work in works.items():
    assert not work.get('publication_id') or work['publication_id'] in paper_ids
    for theme in work['themes']:
        assert work_id in themes[theme]['selected_works'], (work_id, theme)
    for media in work.get('media', []):
        if media.get('web_ready'):
            assert media['path'].endswith('.mp4')
            assert media.get('poster') and media.get('width') and media.get('height')

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(); self.path = path; self.ids = []; self.refs = []; self.images = []; self.videos = []; self.sources = []; self.h1 = 0
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag == 'h1': self.h1 += 1
        for key in ['href', 'src', 'poster']:
            if a.get(key): self.refs.append(a[key])
        if tag == 'img': self.images.append(a)
        if tag == 'video': self.videos.append(a)
        if tag == 'source': self.sources.append(a)

pages = {p: Page(p) for p in SITE.rglob('*.html')}
assert pages, 'Run bundle exec jekyll build first'
count = 0
for path, page in pages.items():
    assert page.h1 == 1, (path, 'h1')
    assert len(page.ids) == len(set(page.ids)), (path, 'duplicate ID')
    for im in page.images:
        assert im.get('alt') and im.get('width') and im.get('height'), (path, im)
        assert not im['src'].lower().endswith('.gif'), (path, 'GIF embed')
    for video in page.videos:
        assert 'controls' in video and 'playsinline' in video and video.get('preload') == 'none'
        assert 'autoplay' not in video and 'loop' not in video
    for source in page.sources:
        assert source['src'].endswith('.mp4') and source.get('type') == 'video/mp4'
    for ref in page.refs:
        u = urlsplit(ref)
        if u.scheme or u.netloc: continue
        target = SITE / unquote(u.path).lstrip('/') if u.path.startswith('/') else path.parent / unquote(u.path)
        if not u.path: target = path
        if target.is_dir(): target = target / 'index.html'
        assert target.exists(), (path, ref, 'missing file')
        if u.fragment: assert unquote(u.fragment) in pages[target].ids, (path, ref, 'missing anchor')
        count += 1
home = pages[SITE / 'index.html']
assert not home.videos and not home.sources
assert not any('/assets/media/' in ref for ref in home.refs), 'Homepage loads scientific media'
for theme, data in themes.items():
    page = pages[SITE / 'research' / theme / 'index.html']
    for work_id in data['selected_works']: assert 'work-' + work_id in page.ids
    for work_id in data['selected_works'][:3]:
        assert '/research/' + theme + '/#work-' + work_id in home.refs
bib = pages[SITE / 'publications/index.html']
for paper_id in paper_ids: assert bib.ids.count('publication-' + paper_id) == 1
assert not list(SITE.rglob('*.avi')), 'Source AVI should not be published'
print(f'PASS: {len(works)} unique works, {len(papers)} publications, {len(themes)} research streams, {len(pages)} pages, {count} internal references; no homepage video payload.')
