#!/usr/bin/env python3
"""Check built manual pages, local links, fragments and deployment assets."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
import json
import re

ROOT=Path(__file__).resolve().parents[1]/'dist'
class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.ids=set();self.links=[];self.h1=0;self.lang=False;self.title=False;self.main=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:
            assert a['id'] not in self.ids,'Duplicate HTML ID: '+a['id']
            self.ids.add(a['id'])
        if tag=='html':self.lang=a.get('lang')=='en'
        if tag=='title':self.title=True
        if tag=='main':self.main=True
        if tag=='h1':self.h1+=1
        if tag=='img':assert 'alt' in a,'Image without alternative text'
        for key in ['href','src']:
            if key in a:self.links.append(a[key])

def main():
    pages={}
    for file in ROOT.glob('*.html'):
        if file.name=='404.html':continue
        parsed=Page();parsed.feed(file.read_text());pages[file.resolve()]=parsed
        assert parsed.lang and parsed.title and parsed.main and parsed.h1==1,file.name+' lacks page structure'
    for file,page in pages.items():
        for href in page.links:
            url=urlsplit(href)
            if url.scheme or url.netloc:continue
            assert not url.path.startswith('/'),'Root-relative link breaks project hosting: '+href
            target=(file.parent/unquote(url.path)).resolve() if url.path else file
            assert target.is_relative_to(ROOT.resolve()),'Link escapes website: '+href
            assert target.is_file(),f'{file.name}: missing link {href}'
            if url.fragment and target in pages:assert unquote(url.fragment) in pages[target].ids,f'{file.name}: missing fragment {href}'
    index=(ROOT/'assets/search-index.js').read_text()
    entries=json.loads(index.removeprefix('window.MANUAL_SEARCH = ').rstrip(';\n'))
    assert len(entries)==len(pages)==13
    for entry in entries:
        assert (ROOT/entry['url']).is_file()
        assert entry['text'] and entry['title']
    for file in ROOT.rglob('*'):
        if file.suffix in {'.html','.js','.css'}:
            text=file.read_text()
            assert not re.search(r'github_pat_[A-Za-z0-9_]{20,}|sk-or-v1-[a-f0-9]{30,}',text),'Credential pattern in '+file.name
    print(f'Validated {len(pages)} pages, their local links and anchors, and the search index.')

if __name__=='__main__':main()
